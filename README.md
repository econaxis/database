# Toy JSON Object Database

## Motivations

I made this database to experiment with concepts from CMU's Youtube Databases Course. I was also curious how databases like Firebase implemented infinitely nested objects or lists. 

Another goal (that I didn't get to yet with this project) was exploring how databases could be scaled across multiple nodes, while still maintaining consistency. This led me to read about two-phase commit, Calvin protocol, consistency models. I learned about complex ideas to store data in a geo-distributed manner, and the fundamental limitation of the speed of light on information transfer. I hope to implement these concepts in another project someday. Old design decisions have made layering on partitioning or distributed replication very difficult for this project.

## Resources

I learned much of my knowledge from:
 - Andy Pavlo's CMU 15-721 Database Systems course on Youtube
 - CockroachDB's transactions documentation
 - VLDB papers on concurrent transaction protocols

I also learned from CockroachDB's Slack group, blog posts from database researchers and other database companies', and Jepsen blog posts.


## Features

This database uses multi-version concurrency control (MVCC) to support concurrent transactions. Under this scheme, only transactions that concurrently modify or read tuples will be aborted. 

 - Strictly serializable (highest level of consistency) transactions
 - ACID transactions
 - Client-side, interactive transactions. Rather than writing SQL, write transactional logic in Python/Javascript/other languages
 - All committed transactions are durable even after a crash through a write-ahead log
 - Very primitive support for replication to follower nodes via gRPC and Protobufs
 - JSON Object-Like API supporting infinite nesting and lists. Locking is performed only for values (floats, strings), not objects. This allows fine-grain locking and reduces transaction abort chance.

## Implementation Notes

### Storing JSON

To store JSON, containing nested lists and objects with no set schema, I flatten the JSON into a series of key: value pairs. The key is the materialized JSON path. Objects and lists are recursively converted into key and values. Values can only be floats, strings, Nulls, or booleans. 

The problem of storing nested data is now converted to a key-value problem, which is easy to solve. This technique allows fine-grained locking. Updates made to one part of a nested object won't abort an update made to another part of the same object. 

This conversion process is all done transparently. Upon query time, the results are reconstructed back into the tree-like JSON structure, and returned to the user.

### MVCC

MVCC requires storing multiple versions of the same value. There are multiple ways to do this. One could store the version number in the key itself. Thus, we can use range queries to get the latest or specific version of a key. However, upon trying this, the database became unusably slow after many updates. The database became clogged with previous versions that slowed down every query. Even garbage collection would be very slow as garbage keys are spread throughout the BTree. 

I instead stored old versions in a separate, array-backed data structure. Old keys and their values would be appended as tuples in an array. Updates happen as normal on the BTree, but a pointer to the old key is stored alongside the updated value. Thus, to reach previous versions, we simply have to traverse backwards the links. 

While traversing a linked list is an O(n) operation, most queries only care about the most recent version. Therefore, this solution optimizes for most recent queries (which happen 99% of the time) over queries for old values.

### Testing

A database has many strong constraints and invariants. This makes it extremely easy to test and find bugs. For example, we can simulate a bank as an object of 100 users and their money balances. Then, we run transactions from multiple threads to transfer money from one user to another. We can add in occasional aborts, slowdowns, or crashes. At the end, the sum of balances must remain the same. If this invariant is broken, then some transaction must have violated consistency.

Another test I run is the counters test. The database stores N counters, starting at 0. A transaction selects a random counter and increments it monotonically, ten times. After each increment, the thread pauses for a random amount. We start M threads (M > N) running these transactions. Another thread then runs continuous read queries on those N counters. If there is ever a counter that is not divisible by ten, then that read must have violated ACID. Since we must only see completed transactions in the read, all counters must be divisible by 10.

These tests are inspired from Jepsen's tests. Running them helped me find many concurrency bugs.



### (Primitive) Replication

A highly available database must be replicated. This database can do very primitive replication to other follower nodes. Upon a transaction's request to commit, the leader sends the changelist to all follower nodes. If all follower nodes reply positively, then the leader node returns to the client, promising a committed transaction. Now, even upon node failure, that transaction has been durably replicated.

### To-Do
 - garbage collection
 - performance issues
 - better user API for high level languages



## Lessons Learned

Building this database has taught me so much about distributed systems, concurrent transactions, and fixing concurrency bugs. However, implementing all these features made the database slower and slower. MVCC, locking, WAL, and a rich data model all add overhead that grows to be unacceptable. 

I am currently building a new database based on the lessons learned here. It removes all the features that make this database slow. There will be no transactional support, nor MVCC, nor a rich data model. It will only support homogenous, fixed-size data types. The data type will be defined as a struct in Rust and compiled straight into the binary. This allows for more optimizations.

Removing the above features would remove almost all overhead. Range queries will, instead of traversing a BTree, just use direct memory access. More complex analytical queries can be easily compiled and read the data as if it was a C style array, without locking or pointer chasing.

In addition, supporting only a single data type allows very efficient compression. If we shuffle the array of structs to be like a columnar database, compression would be even better.


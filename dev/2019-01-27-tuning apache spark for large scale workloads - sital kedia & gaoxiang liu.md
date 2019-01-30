Title: Tuning Apache Spark for Large Scale Workloads - Sital Kedia & Gaoxiang Liu  
Date: 2019-01-27 6:40 PM
Category: Spark     

Spark Architecture  
Driver --> Cluster Manager --> Executor1 & Shuffle Service1
                           --> Executor2 & Shuffle Service2  
                           --> Executor3 & Shuffle Service3  

### Scaling the Spark Driver  
- Hosts Spark context  
- Coordinates with cluster manager to launch executors  
- Schedules tasks   

The Spark driver can become the bottleneck when launching many Spark jobs.  

Scheduler --> Cluster Manager --> Executor1, Executor2, Executor3, Shuffle Service1  
                              --> Executor4, Executor5, Executor6, Shuffle Service2   
                              --> Executor7, Executor8, Executor9, Shuffle Service3  
1. Dynamic Executor Allocation  
- enables the Spark driver to add and remove executors on the fly  
- traditional approach is static (resources must be requested and reserved beforehand)  
- when the task queue is high, the driver talks to the cluster manager and requests more and more resources    
- when the task queue decreases, the driver coordinates with the cluster manager to release the idle executors  
- useful in a shared environment when resources are shared  
spark.dynamicAllocation.enabled = true  
spark.dynamicAllocation.executorIdleTimeout = 2m  
spark.dynamocAllocation.minExecutors = 1  
spark.dynamicAllocation.maxExecutors = 2000  

2. Tune RPC (Remote Procedure Call) Server Threads  
https://www.waitingforcode.com/apache-spark/rpc-apache-spark/read  
- frequent driver OOM when running many tasks in parallel  
- huge backlog of RPC requests built on Netty server of the driver  
- increate RCP server thread to fix OOM (default value is 8)
spark.rpc.io.serverThreads = 64  

### Scaling the Spark Executor  
Executor Memory Layout  
- divided into four sections:  
shuffle memory + user memory + reserved memory (300 MB) + memory buffer
- need to tune shuffle memory and user memory   
- spark.memory.fraction is used to configure both shuffle memory and user memory
 - by default 40% of executor memory is allocated to user memory  
 - in applications that don't need much user memory, increase spark.memory.fraction to trade user memory for shuffle memory   
- shuffle memory spark.memory.fraction * (spark.executor.memory - 300 MB)  
 - used to buffer the shuffle internal data structure  
 - as the map task runs, it stores read in data into the shuffle memory  
 - when shuffle memory is out, the data is spilled to disk  
 - increasing shuffle memory --> avoid spilling to disk  
- user memory (1 - spark.memory.fraction) * (spark.executor.memory - 300 MB)  
 - used for user specific data structure  
 - memory allocation depends on application  
- reserved memory (300 MB)  
- memory buffer spark.yarn.executor.memoryOverhead = 0.1 * (spark.executor.memory)

Enable off-heap memory  
- enables you to allocate the shuffle data structure off heap in native memory
- not allocated or managed by JVM memory manager  
- not subjected to garbage collection  
- shuffle memory  
 - spark.memory.offHeap.enabled = true  
 - spark.memory.offHeap.size = 3g  
- user memory  
 - spark.executor.memory = 3g  
- reserved memory (300 MB)  
- memory buffer  
 - spark.yarn.executor.memoryOverhead = 0.1 * (spark.executor.memory + spark.memory.offHeadp.size)

Garbage collection tuning  
- shuffle internals allocates large contiguous in-memory buffers  
 - G1GC suffers from fragmentation due to large allocations, if object size is more than the maximum region size (32 MB)   
- use parallel GC instead of G1GC  
spark.executor.extraJavaOptions = -XX:ParallelGCThreads=4 -XX:+UseParallelGC  

Eliminating disk I/O bottleneck  

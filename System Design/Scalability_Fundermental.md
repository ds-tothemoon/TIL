# Why Do Scalability Need?

### Assumption : If your services grow up and up explosively, how to deal with a lot of traffics ?

**Conception 1 - Vertical Scaling**

Vertical Scaling means adding more resources (CPU/RAM/DISK) to your server as on demand.

For example, buying more expensive and more powerful hardware (e.g. SSD), or Using virtual machine hypervisor ( e.g. VMWare ESX)

*However, your sever is still only one.* 



**Conception 2 - Horizontal Scaling**

Horizontal Scaling means adding more processing units or physical machines to your server or database.

It involves 

- growing the number of nodes in the cluster
- reducing the responsibilities of each member node by spreading the key space wider
- providing additional end-points for client connections

For example, Load Balancer makes each server  distribute load. So your servers maintain fast speed, although capacity of each server can't change.



**Conception 3 - Caching**

It doesn't mean file system cache. In roughly definition, caching is temporary data saving.

We can apply it to WEB and DB and so on. In WEB, to reduce server latency, web cache is used as saving WEB Docs  (including web pages, images, other type multi-media). 

( deep thinking - Proxy Server)

Also, It can deal with cookies and session management.



**Conception 4 - Load Balancing**

Load Balancing means the process of distributing a set of tasks over a set of resources.

- Scalability
- Fault Tolerance

Algorithm

- Round Robin - equivalent distribution (Fastest)
- Least Connection - Weight based Allocation
- Fastest Response Time
- Adaptive 
- Fixed, Hashing, Random, URL-based, Cookie and so on.

**Conception 5 - Database Replication**

Database Replication means the process of storing data in more than on site or node.

- Improving the availability of data
- The result is distributed database
- For example, Master-Slave System. Master (Write), Slave(Read)

c.f ) Redundancy means the duplication of server or node, not data copy!

**Conception 6 - Database Partitioning**

Database Partitioning means division of a logical database or its constituent elements into distinct independent parts. 

Why Partitioning?

- Manageability, Performance or availability



Sharding - horizontal partitioning
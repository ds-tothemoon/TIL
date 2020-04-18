# NoSQL (Not Only SQL)

## Part 1. 기본개요 및 이론

#### 1. 등장배경

1. 대량의 데이터를 Read/Write할 필요성 증가
2. 지속적으로 증가하는 사용자에 대한 신속한 증가
3. 빠르게 변화하는 비즈니스에 대한 신속한 대응
4. 비정형 데이터의 폭발적 증가

관계형 데이터베이스의 한계가 커짐

데이터는 커져만 가는데, RDBMS로는 저장/관리가 힘듦 

scale out하기에 기존 RDB는 많은 비용을 지불해야함.



##### RDBMS에서의 Scale Out 방법

- master-slave replication ( read from slave, wirte from matser) 구조로 변경
- RAM을 추가
- Sharding, 비정규화, SQL Tunning



#### 2. 개념

Not Only SQL은 비관계형 데이터 스토리지 시스템, 비정형 데이베이스들을 통칭

고정된 테이블 스키마와 조인 개념을 사용하지 않도록 모델링

ACID (원자성, 일관성, 고립성, 지속성) 속성은 '유연하게' 적용함

자동화된 장애 극복, 복구 가능

NoSQL에서도 스키마는 존재하나, application이 가지고 있음 (application side shema)



##### NoSQL 종류

- Key-Value : Dynamo, Redis, Voldemort, Riak
- Column Oriented : Cassandra, HBase, Big Table
- Document : MongoDB,  Couchbase
- Graph : Neo4j



##### Big Data와 NoSQL의 관계

필수는 아니나 Bigdata 활용시, 

- 대용량 데이터 처리, 정형&비정형 데이터, 실시간&스트리밍 처리 시 필요

(NoSQL이 더 적합하다고 봄)

대량의 데이터를 효과적으로 저장하기 위해 샤딩하거나 Ring 형태의 노드에 멀티 복제하는 방법을 사용함. 대부분의 RDB는 수동 샤딩이다. (Cassandra는 Ring 혀앹의 Gossip 프로토콜을 이용한 다중복제)



#### 3. 기본 이론

BASE - Basically Available, Soft state, Eventually consistency

- Sote state : 데이터의 사본은 inconsistent 할 수 있음. 노드의 상태는 외부에 전달된 데이터의 의해 결정된다.
- Eventually Consistent : 데이터의 복사본은 더 이상의 업데이트가 없다면 약간의 지연시간 후에 consistent 하게 된다.
- Basically Available : Falut의 가능성은 있지만, 전체 시스템의 fault가 되지는 않음





#### 4. NoSQL vs RDBMS

| 구분     | NoSQL                                                        | RDBMS                              |
| -------- | ------------------------------------------------------------ | ---------------------------------- |
| 장단점   | 데이터 무결성, 정합성 보장하지 않음 <br />비정형, 반정형 데이터 처리 | 데이터 무결성 보장(CA)             |
| 특징     | 약한 consistency<br/> schema 없거나 변경 용이                | JOIN, ACID                         |
| use case | 대량 데이터 처리, 빠른 성능 요구                             | 중요한 트랜젝션 처리 요구되는 경우 |



# 

## Part 2. 데이터 모델 종류 및 설명

### 1. NoSQL Data Model

기존 RDBMS와는 다른 관점에서 봐라봐야함. 

NoSQL 대부분은 ACID를 지원하지 않고, 원자적 트랜잭션을 지원한다.

가능하다면 원자성이 필요한 범위를 하나의 집합 내로 한정하는 것이 바람직.

집합 지향적으로 모델링하게 되면 자연스럽게 데이터 중복이 발생.

데이터 중복을 허용함으로써, 어플리케이션에서의 쿼리 효율성에 집중하다록 설계해야함



### 2. Key-Value Model

**Key를 이용해 Value에 접근하는 구조.** 어떠한 형태 (List,Set)의 데이터든 저장이 가능, 각 DB별로 value의 최고 저장 size가 있으므로 유의, Key를 기반으로 정렬/비정렬 가능한 점이 다르다.

<img src="https://k.kakaocdn.net/dn/pF5r4/btqwWeUIrnk/cqOWdKIkcByGMuKnBmMDfk/img.png" alt="img" style="zoom: 33%;" />

<center>Redis의 Key-Value Models</center>

### 3. Document 모델

집합 구조를 문서형태로 확인 가능. document 하나의 크기 제한이있음. 집합 내의 필드를 이용해 쿼리 할 수 있음. 문서는 주로 JSON or BSON(Binary JSON), 문서 내의 값들은  필드라는 형태로 존재.

<img src="https://k.kakaocdn.net/dn/Dl20n/btqwVDOa8R8/SAAW01jpyY22Oak2Nw2S9k/img.png" alt="img" style="zoom:50%;" />



<center>mongoDB의 document model</center>



### 4. Column Family 모델

두 단계의 집합(Map) 구조, Row Key에 다수의 column & value가 들어감. Row Key로 자동 정렬, column key로 자동 정렬 가능.

<img src="https://k.kakaocdn.net/dn/b7llEJ/btqwXd1DWf3/D2iZntiwkrESJfqzrxCVh1/img.png" alt="img" style="zoom:33%;" />

<center>cassandrDB의 column family 모델</center>

### 5. Graph 모델

Entity와 Entity 사의 관계를 저장하는 형태. 대부분 분산DB가 아님. RDB처럼 ACID를 지원




# Key-value Database 개요

Key와 Value의 쌍으로 이루어진 저장소. Key가 이미 존재하는 경우 기존 값을 덮어쓴다.

Value는 BLOB(Binary Large Object) 즉, **어떤 형식(type)이든 저장 가능**. 

### 특징

\- **일관성** : Eventual Consistency 

\- **트랜잭션** : 정족수 기반임. 정족수3이면 강한 consistency를 가짐

\- **조회** : 키로만 조회 가능, 대부분 secondary index 지원하지 않음

\- **데이터 구조** : BLOB, JSON, XML 무엇이든 저장 가능

\- **확장성** : 대부분 샤딩을 이용한 확장. 샤드키 설정 중요. 샤드노드 + RF(Replication Factor) 조정 ☞ 일관성 vs 가용성 조절

#### 사용하기 적합한 경우

- 세션정보 저장, 사용자 정보 저장, 관계정보(follow, follower ▷ Redis의 Set정보)때 사용하기 적합

- 읽기 캐쉬, 쓰기 캐쉬 용도로 많이 사용. 

 

#### 사용 부적합한 경우

- 데이터 간의 관계가 있는 경우, key가 아닌 data로 조회하는 경우(일부 NoSQL은 검색엔진(Lucene, Solr)과 연동 가능)

- 집합처리(필요하다면 application layer에서 수행)

- 여러개 값에 대한 다중 트랜젝션 필요할 경우(RDB 사용)
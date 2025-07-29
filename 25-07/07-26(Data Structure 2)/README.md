# 목차

1. 비시퀀스 데이터 구조
    1. 딕셔너리
    2. 세트
2. 참고
    1. 해시 테이블
    2. 파이썬 문법 규격

# 1. 딕셔너리

키와 값을 짝지어 저장하는 자료구조

내부적으로 해시 테이블을 사용하여 키-값쌍을 관리

키 값은 hasable 정해져있지만 값에는 어떤 자료형이든 넣을 수 있음.

### .get(key[, default])

```python
# get
person = {'name': 'Alice', 'age': 25}
print(person.key) # error
print(person.get(key)) # error
print(person.get('name')) # Alice

print(person['country'])  # KeyError: 'country'
print(person.get('coountry', '해당 키는 존재하지 않습니다')) # 해당 키는 존재하지 않습니다.

print(person['name']) # Alice
```

그럼 도대체 get 메서드를 왜 씀?

에러가 발생할 수도 있기 때문임.

### .keys()

```python
# keys
person = {'name': 'Alice', 'age': 25}
print(person.keys)  # <built-in method keys of dict object at 0x0000024C162D8A80>
print(person.keys())  # dict_keys(['name', 'age'])
```

dict_keys([’name’, ‘age’])

실시간으로 동기화되는 확인 창 (view)

```python
person = {'name': 'Alice', 'age': 25}
person_keys = person.keys()
person['country'] = 'KOREA'

print(person.keys())  # dict_keys(['name', 'age', 'country'])

for key in person.keys():
    print(key, end= ' ')

# name agen country
```

### .values()

```python
# values
person = {'name': 'Alice', 'age': 25}
print(person.values())  # dict_values(['Alice', 25])
for value in person.values():
    print(value, end= ' ')
```

### .items()

```python
# items
person = {'name': 'Alice', 'age': 25}
print(person.items())  # dict_items([('name', 'Alice'), ('age', 25)])
for key, value in person.items():
    print(key, value) 
    
# name Alice 
# age 25
```

### .pop(key[,default])

```python
# pop
person = {'name': 'Alice', 'age': 25}
print(person.pop('age'))  # 25
print(person)  # {'name': 'Alice'}
print(person.pop('country'))  # KeyError: 'country'
print(person.pop('country', None))  # None 
```

### .clear()

```python
# clear
person = {'name': 'Alice', 'age': 25}
person.clear()
print(person) # {}
```

### .setdefault(key[,default])

키와 연결된 값을 반환

키가 없다면 default와 연결한 키를 딕셔너리에 추가하고 default를 반환

`get` 기능 + `추가`

```python
# setdefault
person = {'name': 'Alice', 'age': 25}
print(person.setdefault('country', 'KOREA'))  # KOREA
print(person)  # {'name': 'Alice', 'age': 25, 'country': 'KOREA'} 
```

### .update([other])

other가 제공하는 키/값 쌍으로 딕셔너리를 갱신하고 기존 키는 덮어씀

```python
# update
person = {'name': 'Alice', 'age': 25}
other_person = {'name': 'Jane', 'country': 'KOREA'}

person.update(other_person)
print(person)  # {'name': 'Jane', 'age': 25, 'country': 'KOREA'}

person.update(age=100, address='SEOUL')
print(
    person
)  # {'name': 'Jane', 'age': 100, 'country': 'KOREA', 'address': 'SEOUL'}
```

# 2. 세트

고유한 항목들의 정렬되지 않은 컬렉션

내부적으로 `해시 테이블`을 사용하여 데이터를 저장.

중복제거 문제일 때

순서 상관 없을 때 : [] → () → []

순서 상관 있을 때 : 위 방식대로 진행하면 안됨

### .add(x)

```python
# add
my_set = {'a', 'b', 'c', 1, 2, 3}
my_set.add(4)
print(my_set) # {1, 2, 3, 4, 'c', 'a', 'b'}
```

### .update(iterable)

```python
# update
my_set = {'a', 'b', 'c', 1, 2, 3}
my_set.update([1, 4, 5])
print(my_set)  # {'c', 2, 3, 1, 'b', 4, 5, 'a'}
```

### .clear()

```python
# clear
my_set = {'a', 'b', 'c', 1, 2, 3}
my_set.clear()
print(my_set)  # set()
```

`{}` 표현이 안됨 `set()` 으로 표현

### .remove(x)

```python
# remove
my_set = {'a', 'b', 'c', 1, 2, 3}
my_set.remove(2)
print(my_set)
my_set.remove(10)  # KeyError: 10
```

### .pop()

세트에서 임의의 요소를 제거하고 반환소

random 무작위의 개념은 아님

```python
# pop
my_set = {'a', 'b', 'c', 1, 2, 3}
element = my_set.pop() # 1
print(element) # {1, 2, 3, 4, 'c', 5, 'b', 'a'}
```

### .discord(x)

`remove` 와 다르게 에러가 없음

```python
# discard
my_set = {'a', 'b', 'c', 1, 2, 3}
my_set.discard(2)
print(my_set) # {1, 3, 'b', 'c', 'a'}
my_set.discard(10)
```

### 집합 메서드

```python
# 집합 메서드
set1 = {0, 1, 2, 3, 4}
set2 = {1, 3, 5, 7, 9}
set3 = {0, 1}

print(set1.difference(set2))  # {0, 2, 4}
print(set1.intersection(set2))  # {1, 3}
print(set1.issubset(set2))  # False
print(set3.issubset(set1))  # True
print(set1.issuperset(set2))  # False
print(set1.union(set2))  # {0, 1, 2, 3, 4, 5, 7, 9}

```

# 3. 해시 테이블

자료구조의 테이블을 의미함.

엑셀에서 보는 스프레드시트

해시 테이블은 키와 값을 짝지어 저장하는 자료구조임.

| 키 | 값 |
| --- | --- |
| name | 양한빈 |
| age | 26 |

책 제목(키)을 색인(해시 함수)에서 찾아 몇 번째 착장(인덱스)에 있는지 알아낸다.



### 해시

임의의 크기를 가진 데이터를 고정된 크기의 고유한 값으로 변환하는 것

생성된 해시 값(고유한 정수)은 해당 데이터를 식별하는 ‘지문’ 역할을 함

파이썬에서는 이 해시 값을 이용해 해시 테이블에 데이터를 저장

이 변환을 수행하는 것이 해시 함수 

### 해시 함수

임의 길이 데이터를 입력 받아 고정 길이(정수)로 변환해 주는 함수.

이 ‘정수’가 바로 해시 값

### 해시 테이블이 매우 빠른 이유 :

해시 함수는 키(key)를 입력받아 데이터를 저장하거나 찾을 배역의 정확한 인덱스를, 즉시 계산

리스트는 각 항목을 순차적으로 확인해야함에 비해 매우 빠름.

### set의 요소 & dict의 키와 해시 테이블 관계

- set
    - 각 요소를 해시 함수로 변환해 나온 해시 값에 맞춰 해시 테이블 내부 버킷(bucket)에 위치시킴
    - 그래서 순서 라기보다 버킷  위치(인덱스)가 요소 위치를 변경
    - 따라서 set는 순서를 보장하지 않음
- dict
    - 키 → 해시 함수 → 해시 값 → 해시 테이블에 저장
    - 단 set와 달리 “삽입 순서”는 유지한다는 것이 언어 사양에 따라 보장 됨 (python 3.7 이상)
        - 즉, 키를 추가한 순서대로 반복문 순회할 때 나오게 됨ㅅ
        - 개발자를 위해 추가된 기능



해시 함수의 결과 값은 정수를 뱉음

지연 평가와 마찬가지로 파이썬은 게으른 똑똑이라서 정수 값을 그대로 써버림.



문자열은 항상 난수화의 과정을 거침.

### 파이썬에서의 해시 함수

- 정수
    - 같은 정수는 항상 같은 해시 값을 가짐
    - hash(1)은 여러 번 호출해도 결과가 동일
- 문자열
    - 문자열 해시 시, 파이썬 인터프리터 시작 때 설정되는 난수 시드(seed)가 달라질 수 있음
    - 보안상 이유로 해시 난수화 도입
    - 각 실행마다 달라질 수 있어 ‘a’의 해시 값도 매번 바뀔 수 있음

### 해시 난수화와 난수 시드

파이썬 프로세스가 새로 시작될 때마다 해시를 계산할 때 사용하는 난수 시드가 달라짐

→ 해시 함수가 매번 바뀌는 것이 아니라, 해시 계산에 쓰이는 시드 값이 실행마다 달라지는 것.

이로 인해 동일한 데이터라도 매번 해시 값이 달라져 결과적으로 버킷 배치가 달라짐.

<aside>
💡
결론 : 결과가 항상 다른 이유는 난수 시드 번호가 달라지기 때문임.

</aside>

### set의 요소 & dict의 키와 해시테이블 관계

- set의 pop()은 ‘임의의 요소’를 제거하고 반환
    - 실행할 때마다 다른 요소를 얻는다는 의미에서 무작위가 아니라 임이라는 의미에서의 무작위
    
      → 버킷 배치 순서에 따라서 결정되기 때문임.
    

- 내부적으로 해시 테이블(버킷)을 참조하기 때문에, 실행 때마다 다른 요소가 먼저 나올 수 있음
    - 해시 난수화로 인해 문자열 같은 해시 값이 실행마다 달라질 수 있고, 
    따라서 set 내부 요소의 배치가 달라질 수 있음
    - 정수는 해시 값이 항상 동일하기 때문에, 파이썬을 동일 프로세스에서 연속 실행할 때는 
    결과가 일정해 보이기도 하지만, 여전히 set은 순서가 없으므로 pop되는 순서도 예측 불가

### hashable

- hash() 함수에 넣어 해시 값을 구할 수 있는 객체를 의미
- 대부분의 불변 타입은 해시 가능 (int, float, str, tuple 등) (내부에도 불변만 있어야함)
- 가변형 객체는 기본적으로 해시 불가능 (list, dict, set 등)

  → 가변형 객체가 hasable 하지 않은 이유는 값이 변경될 수 있으므로, 해시 테이블에서 동일 값 → 동일 키 원칙 깨짐

# 4. 파이썬 문법 규격

### EBNF

`[]` 선택적 요소

`{}` 0번 이상 반복

`()` 그룹화
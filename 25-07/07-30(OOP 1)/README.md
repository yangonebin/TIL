# 목차

1. 프로그래밍 패러다임
    1. 절차 지향과 객체 지향
    2. 객체와 클래스
2. 클래스 기초
    1. 클래스
    2. 인스턴스
    3. 클래스와 인스턴스
    4. 클래스 구성요소
    5. 클래스 변수와 인스턴스 변수
3. 메서드
    1. 인스턴스 메서드
    2. 클래스 메서드
    3. 스태틱 메서드
    4. 메서드 활용
    5. 메서드 정리
4. 참고
    1. 클래스와 인스턴스 간 이름 공간
    2. 매직 메서드
    3. 데코레이터

# 1. 절차 지향과 객체 지향

### 절차 지향 프로그래밍

데이터를 순차적으로 처리

한계 

1.  프로그램 규모가 커질 수록 데이터의 함수의 관리가 어려움
2. 전역 변수의 증가로 인한 관리의 어려움

### 객체 지향 프로그래밍

클래스는 설계도

인스턴스는 실제 물건.

프로그램 데이터(변수)와 그 데이터를 처리하는 함수(메서드)를

하나의 단위(객체)로 묶어서 조직적으로 관리

<aside>
💡
객체지향은 데이터와 메서드의 결합

</aside>

| 절차 지향 | 객체 지향 |
| --- | --- |
| 데이터와 해당 데이터를 처리하는 함수(절차)가 분리 | 데이터와 해당 데이터를 처리하는 메서드를 하나의 객체로 묶음 |
| 함수 호출의 흐름이 중요 | 객체 간 상호작용과 메세지 전달이 중요 |

객체지향은 수동적인 데이터가 능동적인 객체로 변화한 것.

스스로 기능을 수행하는 능동적인 존재가 됨

함수(데이터)    → 수동적

데이터.메서드()  → 능동적

### 절차 지향과 객체 지향은 VS 개념이 아니다.

객체 지향은 기존 절차 지향을 기반으로 두고 보완하기 위해 객체라는 개념을 도입.

# 2. 객체와 클래스

### 객체 정의

실제 존재하는 사물을 추상화한 것

속성과 동작을 가짐

예를 들어 강아지라는 객체는

이름,종,나이 (속성)과 짖기(), 꼬리흔들기() (동작)을 가짐

### 클래스

객체를 만들기 위한 설계도

클래스로부터 여러개의 객체를 쉽게 만들 수 있습니다.

가수(클래스) → 객체(아이유, BTS .. )

### 객체 특징

속성        —-

                          > 두가지를 가짐

메서드    —-

고유성

### 클래스 정의

```python
class MyClass:
	pass
```

클래스 이름은 파스칼 케이스 방식으로 작성 MyClass

변수랑 함수는 스네이크 케이스 my_class

```python
class Person:
    # 생성자 메서드
    def __init__(self, name, age):
        # 인스턴스 속성
        self.name = name
        self.age = age

    def introduce(self):
        print(f'반갑습니다. 저는 { self.name }이고, 나이는 { self.age }살입니다.')

```

# 3. 인스턴스

클래스를 통해 생성된 객체

```python
class Person:
    def __init__(self, name, age):
        self.name = name  # 인스턴스 속성
        self.age = age  # 인스턴스 속성

    def introduce(self):
        print(f'안녕하세요. 저는 {self.name}, 나이는 {self.age}살입니다.')

# 인스턴스 생성
# 인스턴스 = 클래스 호출
p1 = Person('Alice', 25)
p2 = Person('Bella', 30)

# 인스턴스 변수 접근 및 호출
print(p1.name) # Alice
print(p2.name) # Bella

p1.introduce() # 안녕하세요. 저는 Alice, 나이는 25살입니다.
p2.introduce() # 안녕하세요. 저는 Bella, 나이는 30살입니다.
```

아이유는 객체다 ⭕

아이유는 인스턴스다 ❌

아이유는 가수의 인스턴스다 ⭕

- 그렇다면 아이유의 클래스는?
    
    가수
    

### 클래스와 인스턴스

클래스를 정의한다는 것은 공통된 특성과 기능을 가진 틀을 만드는 것

실제 활동하는 개별 객체들은 이 틀에서 생성된 인스턴스

공통된 특성과 기능을 가진 틀을 만드는 것은 곧 새로운 타입을 만드는 행위

```python
name = "Alice"

print(type(name)) # <class 'str'>
```

변수 name의 타입은 str 클래스다.

변수 name은 str 클래스의 인스턴스이다.

문자열 타입(클래스)의 

객체(인스턴스)

따라서 capitalize() 등 메서드 함수 사용 가능.

```python
"hello".upper()
```

문자열.대문자로()

객체.행동()

인스턴스.메서드()

```python
class Circle:
    pi = 3.141592
    # 생성자 메서드
    def __init__(self, radius):
        self.radius = radius
        
        
# 인스턴스 생성
c1 = Circle(1)
c2 = Circle(2)

# 인스턴스 변수(속성) 접근
print(c1.radius)
print(c2.radius)

# 클래스 변수(공통 속성) 접근
print(c1.pi)
print(c2.pi)
```

# 4. 클래스 변수와 인스턴스 변수

```python
class Circle:
    pi = 3.14

    def __init__(self, radius):
        self.radius = radius

c1 = Circle(5)
c2 = Circle(10)

print(c1.radius)  # 5
print(c2.radius)  # 10

# c1이 본인 인스턴스 변수 pi를 생성
c1.pi = 100

print(c1.pi) # 100
```

클래스 변수와 동일한 이름으로 인스턴스 변수 생성 시

클래스 변수가 아닌 인스턴스 변수에 먼저 참조하게 됨.

# 5. 인스턴스 메서드

인스턴스의 상태를 조작하거나 동작을 수행

인스턴스가 호출한다.

### 인스턴스 메서드 구조

클래스 내부에 정의되는 메서드의 기본

반드시 첫 번째 인자로 인스턴스 자신(self)을 받음

```python
‘hello’.upper() 는 사실
str.upper('hello') 임.
```

인스턴스 메서드의 첫번째 인자가 반드시 인스턴스 자기 자신인 이유

`'hello'` 라는 문자열 객체가

단순히 어딘가의 함수로 들어가는 인자로 활용되는 것이 아닌

객체 스스로가 메서드를 호출하여 코드를 동작하는 객체 지향적인 표현인 것

```python
class Counter:
    def __init__(self):
        self.count = 0

    # 인스턴스 메서드
    def increment(self):
        self.count += 1

c1 = Counter()
c2 = Counter()
# 인스턴스 메서드 호출

c1.increment()
print(c1.count) # 1
print(c2.count) # 0
```

# 6. 생성자 메서드

인스턴스 객체가 생성될 때 자동으로 호출되는 메서드

→ 인스턴스 변수들의 초기값을 설정

```python
class Person:
    # 생성자 메서드
    def __init__(self, name):
        self.name = name
        print("인스턴스가 생성되었습니다.")

    def greeting(self):
        print(f'안녕하세요 {self.name}입니다.')

Person1 = Person("지민")
print(Person1.name)
print(Person1.greeting())

# 인스턴스가 생성되었습니다.
# 지민
# 안녕하세요 지민입니다.
# None
```

# 7. 클래스 메서드

클래스 변수를 조작하거나

클래스 레벨의 동작을 수행

```python
class Person:
    population = 0

    def __init__(self, name):
        self.name = name
        Person.increse_population()

    # 클래스 메서드
    @classmethod
    def increse_population(cls):
        cls.population += 1

# 인스턴스 생성
person1 = Person('Alice')
person2 = Person('Bob')

# 클래스 변수 접근
print(Person.population)  # 2

```

# 8. 스태틱 메서드

클래스,인스턴스와 상관없이

독립적으로 동작하는 메서드

호출 주체

| 인스턴스 | 클래스  |
| --- | --- |
| 인스턴스 메서드 | 클래스 메서드 |
|  | 스태틱 메서드 |

### 메서드 정리

인스턴스 메서드 - 인스턴스 상태 변경

클래스 메서드 - 클래스 변수 변경

스태틱 메서드 - 인자를 받을 필요가 없음

# 9. 참고

객체 지향 프로그래밍은 독립적인 이름 공간을 가짐

따라서, 서로 충돌하지 않고 사용할 수 있음

### 매직 메서드

### 데코레이터
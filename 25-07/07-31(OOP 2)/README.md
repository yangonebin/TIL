# 목차

1. 상속
    1. 상속 기본 개념
    2. 부모 클래스와 자식 클래스
    3. 메서드 오버라이딩
    4. 다중 상속
    5. super() 메서드
2. 에러와 예외
    1. 디버깅
    2. 에러
    3. 예외
3. 예외 처리
    1. try & except
    2. 복수 예외 처리
    3. else & finally
4. 참고
    1. 예외 처리 주의사항
    2. 예외 객체 다루기
    3. EAFP & LBYL
    4. 클래스의 의미와 활용

# 1. 상속의 기본 개념

한 클래스(부모)의 속성과 메서드를

다른 클래스(자식)가 물려받는 것

```python
class Animal:
    def eat(self):
        print('먹는 중')

class Dog(Animal):
    def bark(self):
        print('멍멍')

my_dog = Dog()
my_dog.bark() # 멍멍

# 부모 클래스 메서드 사용 가능
my_dog.eat() # 먹는 중
```

# 2. 부모 클래스와 자식 클래스

상속을 하는 이유는 중복을 최소화하기 위함임.

```python
# 상속 없는 경우 - 1
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def talk(self):
        print(f'반갑습니다. {self.name}입니다.')

s1 = Person('김학생', 23)
s1.talk()  # 반갑습니다. 김학생입니다.

p1 = Person('박교수', 59)
p1.talk()  # 반갑습니다. 박교수입니다.

# 상속 없는 경우 - 2
class Professor:
    def __init__(self, name, age, department):
        self.name = name
        self.age = age
        self.department = department

    def talk(self):  # 중복
        print(f'반갑습니다. {self.name}입니다.')

class Student:
    def __init__(self, name, age, gpa):
        self.name = name
        self.age = age
        self.gpa = gpa

    def talk(self):  # 중복
        print(f'반갑습니다. {self.name}입니다.')

# 상속을 사용한 계층구조 변경
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        

    def talk(self):  # 메서드 재사용
        print(f'반갑습니다. {self.name}입니다.')

class Professor(Person):
    def __init__(self, name, age, department):
        self.name = name
        self.age = age
        self.department = department

class Student(Person):
    def __init__(self, name, age, gpa):
        self.name = name
        self.age = age
        self.gpa = gpa

# 부모 Person 클래스의 talk 메서드를 활용
p1 = Professor('김교수', 50, '컴퓨터공학과')
s1 = Student('김학생', 20, 3.5)

# 부모 Person 클래스의 talk 메서드를 활용
p1.talk()
s1.talk()
```

# 3. 메서드 오버라이딩

부모 클래스의 메서드를 같은 이름, 같은 파라미터 구조로 재정의하는 것

자식 클래스에서 메서드를 다시 정의하면, 부모 클래스의 메서드 대신 자식 클래스의 메서드가 실행됩니다.

```python
class Animal:
    def eat(self):
        print('Animal이 먹는 중')

class Dog(Animal):
    # 오버라이딩 (부모 클래스 Animal의 eat 메서드를 재정의)
    def eat(self):
        print('Dog가 먹는 중')

my_dog = Dog()
my_dog.eat() # Dog가 먹는중
```

### 참고: 파이썬은 오버로딩을 지원하지 않음.

같은 이름, 다른 파라미터를 가진 여러 메서드를 정의하는 것.

파이썬은 실제로 하느이 메서드만 인식. 인자의 형태가 다르다는 이유로 메서드를 여러 개 구분하여 불러주지 않음

```python
# 오버로딩 (파이썬 미지원)
class Example:
    def do_something(self, x):
        print('첫 번째 do_something 메서드:', x)

    # 파이썬에서는 메서드가 "이름"이 같으면 앞선 정의를 덮어써버림
    def do_something(self, x, y):
        print('두 번째 do_something 메서드:', x, y)

example = Example()
# # TypeError: do_something() missing 1 required positional argument: 'y'
example.do_something(10)
```

# 4. 다중 상속

둘 이상의 상위 클래스로부터 여러 행동이나 특징을 상속받을 수 있습니다.

```python
# 다중 상속 예시
class Person:
    def __init__(self, name):
        self.name = name

    def greeting(self):
        return f'안녕, {self.name}'

class Mom(Person):
    gene = 'XX'

    def swim(self):
        return '엄마가 수영'

class Dad(Person):
    gene = 'XY'

    def walk(self):
        return '아빠가 걷기'

class FirstChild(Dad, Mom):
    def swim(self):
        return '첫째가 수영'

    def cry(self):
        return '첫째가 응애'

baby1 = FirstChild('아가')
print(baby1.cry())  # 첫째가 응애
print(baby1.swim())  # 첫째가 수영
print(baby1.walk())  # 아빠가 걷기
print(baby1.gene)  # XY
```

`FirstChild(Dad, Mom)` 이기 때문에 `Dad`의 `gene` 을 가져감

### MRO (Method Resolution Order)

파이썬이 메서드를 찾는 순서에 대한 규칙.

메서드 결정 순서 

Dad → Mom → Person 순으로 참조하는 것.

# 5. super()

메서드 해석 순서(MRO)에 따라,

현재 클래스의 부모(상위) 클랫의 메서드나 속성에 접근할 수 있게 해주는 내장 함수

### 단일 상속에서 super()

```python
# 단일 상속

# super를 사용하지 않았을 때
class Person:
    def __init__(self, name, age, number, email):
        self.name = name
        self.age = age
        self.number = number
        self.email = email

class Student(Person):
    def __init__(self, name, age, number, email, student_id):
        self.name = name
        self.age = age
        self.number = number
        self.email = email
        self.student_id = student_id

# super를 사용했을 때
class Person:
    def __init__(self, name, age, number, email):
        self.name = name
        self.age = age
        self.number = number
        self.email = email

class Student(Person):
    def __init__(self, name, age, number, email, student_id):
        # super()를 통해 Person의 __init__ 메서드 호출
        pass
        self.student_id = student_id

```

단일 상속에서 super()가 굳이? 라고 느껴질 수 있지만,

부모 클래스의 이름이 변경될 경우 자식 클래스도 전부 수정해야하는 반면

super()는 유지보수성이 우수함

### 다중 상속일 때 super()

```python
# 다중 상속
class ParentA:
    def __init__(self):
        # super().__init__()
        self.value_a = 'ParentA'

    def show_value(self):
        print(f'Value from ParentA: {self.value_a}')

class ParentB:
    def __init__(self):
        self.value_b = 'ParentB'

    def show_value(self):
        print(f'Value from ParentB: {self.value_b}')

class Child(ParentA, ParentB):
    def __init__(self):
        super().__init__()  # ParentA 클래스의 __init__ 메서드 호출
        self.value_c = 'Child'

    def show_value(self):
        super().show_value()  # ParentA 클래스의 show_value 메서드 호출
        print(f'Value from Child: {self.value_c}')

child = Child()
child.show_value()
"""
Value from ParentA: ParentA
Value from Child: Child
"""
```

### super()는 단순히 부모 클래스를 호출한다는 의미가 아니다.

```python
# 다중 상속
class ParentA:
    def __init__(self):
        # super().__init__()
        self.value_a = 'ParentA'

    def show_value(self):
        print(f'Value from ParentA: {self.value_a}')

class ParentB:
    def __init__(self):
        self.value_b = 'ParentB'

    def show_value(self):
        print(f'Value from ParentB: {self.value_b}')

class Child(ParentA, ParentB):
    def __init__(self):
        super().__init__()  # ParentA 클래스의 __init__ 메서드 호출
        self.value_c = 'Child'

    def show_value(self):
        super().show_value()  # ParentA 클래스의 show_value 메서드 호출
        print(f'Value from Child: {self.value_c}')

child = Child()
child.show_value()
"""
Value from ParentA: ParentA
Value from Child: Child
"""

print(child.value_c)  # Child
print(child.value_a)  # ParentA
print(
    child.value_b
)  # AttributeError: 'Child' object has no attribute 'value_b'

"""
<ParentA에 super().__init__()를 추가하면?>
그 다음으로 ParentB의 __init__가 실행되어 value_b도 초기화할 수 있음
그러면 print(child.value_b)는 ParentB를 출력하게 됨

print(child.value_b)  # ParentB
"""

"""
<Child 클래스의 MRO>
Child -> ParentA -> ParentB

super()는 단순히 “직계 부모 클래스를 가리킨다”가 아니라, 
MRO 순서를 기반으로 “현재 클래스의 다음 순서” 클래스(또는 메서드)를 가리킴

따라서 ParentA에서 super()를 부르면 MRO상 다음 클래스인 ParentB.__init__()가 호출됨
"""

"""
1.1 Child 클래스의 인스턴스를 생성할 때 일어나는 일
    1.	child = Child() 호출 시, Child.__init__()가 실행
    2.	Child.__init__() 내부에서 super().__init__()를 호출
        - 여기서 Child의 super()는 MRO에 의해 ParentA의 __init__()를 가리킴
    3.	ParentA.__init__()로 진입

1.2. ParentA.__init__() 내부
	1.	ParentA.__init__()에는 다시 super().__init__()가 있음
	2.	ParentA를 기준으로 MRO에서 “다음 클래스”는 ParentB, 따라서 ParentA의 super().__init__()는 ParentB.__init__() 호출
    3.	ParentB.__init__()가 실행되면서 self.value_b = 'ParentB'가 설정됨
	4.	ParentB.__init__()가 종료된 후, 다시 ParentA.__init__()로 돌아와 self.value_a = 'ParentA'가 설정됨
	5.	ParentA.__init__() 종료 후, 다시 Child.__init__()로 돌아감
	6.	마지막으로 Child.__init__() 내에서 self.value_c = 'Child'가 설정되고 종료

1.3 결과적으로 child 인스턴스는 value_a, value_b, value_c 세 속성을 모두 갖게 됨
	- child.value_a → 'ParentA'
	- child.value_b → 'ParentB' 
	- child.value_c → 'Child'
"""

```

MRO 는 시작점이 중요함

1. Child → 2. ParentA → 3. ParentB

```python
# mro() , __mro__ 사용 예시

class A:
    def __init__(self):
        print('A Constructor')

class B(A):
    def __init__(self):
        super().__init__()
        print('B Constructor')

class C(A):
    def __init__(self):
        super().__init__()
        print('C Constructor')

class D(B, C):
    def __init__(self):
        super().__init__()
        print('D Constructor')

# [<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]
print(D.mro())

# (<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>)
print(D.__mro__)

```

 

# 6. 디버깅

### 에러

1. 문법 에러 : 프로그램의 구문이 올바르지 않은 경우 발생 (오타, 괄호 및 콜론 누락 등의 문법적인 오류)
2. 예외 : 프로그램 실행 중에 감지되는 에러

### Unterminated string literal - 문법 에러

문자열이나 문장을 제대로 닫지 않은 경우

# 7. 예외

프로그램 실행 중에 감지되는 에러

### 내장 예외  Built-in Exception

예외 상황을 나타내는 예외 클래스들



# 8. 예외 처리

예외가 발생했을 때 프로그램이 비정상적으로 종료되지 않고, 적절하게 처리할 수 있도록 하는 방법

`try` : 예외가 발생할 수 있는 코드 작성 (일단 실행)

`except` : 예외가 발생했을 때 실행할 코드

`else` : 예외가 발생하지 않았을 때 실행할 코드

`finally` : 예외 발생 여부 상관없이 항상 실행할 코드

```python
# try-except
try:
    result = 10 / 0
except ZeroDivisionError:
    print('0으로 나눌 수 없습니다.')
else:
    print(f'결과: {result}')
finally:
    print('프로그램이 종료되었습니다.')
```

```python
# 복수 예외처리
try:
    num = int(input('100을 나눌 값을 입력하시오 : '))
    print(100 / num)
except (ValueError, ZeroDivisionError):
    print('제대로 입력해주세요.')

try:
    num = int(input('100을 나눌 값을 입력하시오 : '))
    print(100 / num)
except ValueError:
    print('숫자를 넣어주세요.')
except ZeroDivisionError:
    print('0으로 나눌 수 없습니다.')
except:
    print('에러가 발생했습니다.')

```

`except Exception`이 모든 예외를 먼저 가로채기 때문에, 그 아래에 있는 `ZeroDivisionError` 전용 처리 코드는 절대 실행되지 않습니다.

항상 범용적인 예외 처리 `Exception`는 마지막에 두어야 합니다.

# 9. 예외 객체 다루기

```python
my_list = []

try:
    number = my_list[1]
except IndexError as error:
    # list index out of range가 발생했습니다.
    print(f'{error}가 발생했습니다.')
```

`as` 사용 가능

### EAFP & LBYL

```python
my_dict = {
    'key': 'value',
}

# EAFP (Easier to Ask for Forgiveness than Permission)
try:
    result = my_dict['key']
    print(result)
except KeyError:
    print('Key가 존재하지 않습니다.')

# LBYL (Look Before You Leap)
if 'key' in my_dict:
    result = my_dict['key']
    print(result)
else:
    print('Key가 존재하지 않습니다.')

```

| EAFP | LBYL |
| --- | --- |
| 일단 실행하고 예외 처리 | 실행하기 전에 조건을 검사 |
| 예외 상황을 예측하기 어려운 경우 | 예외 상황을 미리 방지하고 싶을 때 유용 |
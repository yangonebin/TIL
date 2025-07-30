# 목차

1. Data Structure
    1. 메서드
2. 시퀀스 데이터 구조
    1. 문자열
    2. 리스트
3. 복사
    1. 객체와 참조
    2. 얕은 복사
    3. 깊은 복사
    
4. 참고
    1. List Comprehension
    2. 메서드 체이닝
    3. 문자 유형 판별 메서드

# 1. Data Structure

여러 데이터를 효과적으로 사용 관리하기 위한 구조 (`str`, `list`, `dict` 등)

= 자료 구조



데이터 구조의 활용은 메서드

문자열, 리스트, 딕셔너리 등 각 **데이터 구조**의 메서드를 호출하여 다양한 기능을 활용

# 2. 메서드

객체에 속한 함수

메서드는 클래스 내부에 저장된 함수이다.

메서드 호출 방법

데이터 타입 객체. 메서드()

```python
‘hello’.capitalize()
```

# 3. 문자열

### .find(x)

x의 첫 번째 위치를 반환. 없으면, -1을 반환

```python
# find
text = 'banana'
print(text.find('a'))  # 1
print(text.find('z'))  # -1
```

### .index(a)

x의 첫 번째 위치를 변환. 없으면, 오류 발생

```python
# index
print(text.index('a'))  # 1
print(text.index('z'))  # ValueError: substring not found
```

### .isupper(x), islower(x)

```python
# isupper
string1 = 'HELLO'
string2 = 'Hello'

print(string1.isupper) # <built-in method isupper of str object at 0x000001B22A295730>
print(string1.isupper())  # True
print(string2.islower())  # False
```

### .isalpha(x)

```python
# isalpha
string1 = 'Hello'
string2 = '123heis98576ssh'
print(string1.isalpha())  # True
print(string2.isalpha())  # False
```

## 문자열 조작 메서드

### .replace(old, new[,count])

```python
# replace
text = 'Hello, world! world world'
new_text1 = text
new_text2 = text
print(new_text1.replace('world', 'Python'))  # Hello, Python! Python Python
print(new_text2.replace('world', 'Python'[1]))  # Hello, y! y y 
print(new_text2.replace('world', 'Python', 1)) # Hello, Python! world world
```

### .strip([chars])

```python
# strip
text = '  Hello, world!  '
new_text = text
print(new_text.strip(''))  #    Hello, world!  
print(new_text.strip())  # Hello, world!
print(new_text.strip('H'))  #    Hello, world! 

# strip 2
text = '  Hello, world!  '
new_text = text.strip()

print(new_text.strip('H'))  # ello, world! 
```

`strip` 은 단계별로 진행해야함

### .split(sep = None, maxsplit = -1)

```python
# split
text = 'Hello, world!'
words1 = text
words2 = text
print(words1.split(','))  # ['Hello', ' world!']
print(words2.split())  # ['Hello,', 'world!']
```

`sep` 기본 값 `none` 은 공백을 기준으로 나누어짐 

### ’separator’.join(iterable)

```python
# join
words = ['Hello', 'world!']
new_text = '-'.join(words)
new_text1 = '-'.join(new_text) # Hello-world!
print(new_text1)  # H-e-l-l-o---w-o-r-l-d-!
```

`separator` 는 내가 정하는 거임 (예시:  `-` )

문자열은 불변 시퀀스다 ! 

### 기타

```python
# capitalize
text = 'heLLo, woRld!'
new_text1 = text.capitalize()
print(new_text1)  # Hello, world!

# title
new_text2 = text.title()
print(new_text2)  # Hello, World!

# upper
new_text3 = text.upper()
print(new_text3)  # HELLO, WORLD!

# lower
new_text4 = text.lower()
print(new_text4)  # hello, world!

# swapcase
new_text5 = text.swapcase()
print(new_text5)  # HEllO, WOrLD!

```

# 4. 리스트

### 리스트 값 추가 및 삭제 메서드

가변 →  원본 값을 바꿈 → 반환 값 없음!

### .append(x)

```python
# append
my_list = [1, 2, 3]
my_list.append(4)
print(my_list)  # [1, 2, 3, 4]

# append는 None을 반환합니다.
print(my_list.append(5))  # None
print(my_list) # [1, 2, 3, 4, 5]
```

### .extend(iterable)

```python
# extend
my_list = [1, 2, 3]
my_list.extend([4, 5, 6])
print(my_list)  # [1, 2, 3, 4, 5, 6]

# extend와 append의 비교
my_list.append([5, 6, 7])
print(my_list)  # [1, 2, 3, 4, 5, 6, [5, 6, 7]]

my_list.extend(100)  # TypeError: 'int' object is not iterable
```

### .insert(i, x)

```python
# insert
my_list = [1, 2, 3]
my_list.insert(1, 5)
print(my_list)  # [1, 5, 2, 3]
```

### .remove(x)

```python
# remove
my_list = [1, 2, 3, 2, 2, 2]
my_list.remove(2)
print(my_list)  # [1, 3, 2, 2, 2]
```

### .pop(i)

리스트에서 지정한 인덱스의 항목을 제거하고 반환

```python
# pop
my_list = [1, 2, 3, 4, 5]
item1 = my_list.pop()
item2 = my_list.pop(0)

print(item1)  # 5
print(item2)  # 1
print(my_list)  # [2, 3, 4]
```

`pop` 은 반환 값이 있음 !!!

### .clear()

```python
# clear
my_list = [1, 2, 3]
my_list
print(my_list)  # []
```

## 리스트 탐색 및 정렬 메서드

### .index(x)

리스트에서 첫 번째로 일치하는 항목 x의 인덱스를 반환

```python
# index
my_list = [1, 2, 3]
index = my_list.index(2)
print(index)  # 1
```

### .count(x)

리스트에서 항목 x의 개수를 반환

```python
# count
my_list = [1, 2, 2, 3, 3, 3]
counting_number = my_list.count(3)
print(counting_number)  # 3
```

### .reverse()

리스트의 순서를 역순으로 정렬한다 ❌

정렬하지는 않는다. 

리스트의 순서를 역순으로 변경한다.

```python
# reverse
my_list = [1, 3, 2, 8, 1, 9]
my_list.reverse()
# reverse는 None을 반환합니다.
print(my_list.reverse())  # None
# reverse는 원본 리스트를 변경합니다.
print(my_list)  # [9, 1, 8, 2, 3, 1]
```

### .sort()

원본 리스트를 오름차순으로 변경

```python
# sort
my_list = [3, 2, 100, 1]
my_list.sort()

# sort는 None을 반환합니다.
print(my_list.sort())  # None

# sort는 원본 리스트를 변경합니다.
print(my_list)  # [1, 2, 3, 100]

my_list.sort(reverse=True)
print(my_list)  # [100, 3, 2, 1]
```

# 5. 객체와 참조

가변 객체 : 리스트, 딕셔너리, 집합

불변 객체 : 정수, 실수, 문자열, 튜플

### 변수 할당의 의미

파이썬에서 변수 할당은 객체에 대한 참조를 생성하는 과정

변수는 객체의 메모리 주소를 가리키는 라벨 역할을 함.

‘=’ 연산자를 사용하여 변수에 값을 할당할 시:

1. 새로운 객체 생성 후 참조
2. 기존 객체에 대한 참조

```python
# 가변(mutable) 객체 예시
print('가변(mutable) 객체 예시')
a = [1, 2, 3, 4]
b = a
b[0] = 100

print(f'a의 값: {a}')  # [100, 2, 3, 4]
print(f'b의 값: {b}')  # [100, 2, 3, 4]
print(f'a와 b가 같은 객체를 참조하는가? {a is b}')  # True 
```

```python
# 불변(immutable) 객체 예시
print('\n불변(immutable) 객체 예시')
a = 20
b = a
b = 10

print(f'a의 값: {a}')  # 20
print(f'b의 값: {b}')  # 10
print(a is b)  # False
```

```python
# id() 함수를 사용한 메모리 주소 확인
print('\n메모리 주소 확인')
x = [1, 2, 3]
y = x
z = [1, 2, 3]

print(f'x의 id: {id(x)}')
print(f'y의 id: {id(y)}')
print(f'z의 id: {id(z)}')
print(f'x와 y는 같은 객체인가? {x is y}')
print(f'x와 z는 같은 객체인가? {x is z}')
```

왜 이 지랄하는 거지에 대한 답변

1. 성능 최적화
2. 메모리 효율성

# 6. 얕은 복사

객체의 최상위 요소만 새로운 메모리에 복사되는 방법

내부의 중첩된 객체가 있다면 그 객체의 참조만 복사됨

 

얕은 복사 구현 방법

1. 리스트 슬라이싱
2. copy() 메서드
3. list() 함수

```python
# 얕은 복사
print('\n얕은 복사 예시')

# 1차원 리스트에서의 얕은 복사 (리스트 슬라이싱)
a = [1, 2, 3]
b = a[:]

print(a)  # [1, 2, 3]
print(b)  # [1, 2, 3]

# 1차원 리스트에서의 얕은 복사 (copy 메서드)
a = [1, 2, 3]
b = a.copy()

print(a)  # [1, 2, 3]
print(b)  # [1, 2, 3]

# 1차원 리스트에서의 얕은 복사 (list() 함수)
a = [1, 2, 3]
d = list(a)
a[0] = 100

print(a)  # [100, 2, 3]
print(d)  # [1, 2, 3]

# 얕은 복사의 한계
print('\n다차원 리스트 얕은 복사의 한계')
a = [1, 2, [3, 4, 5]]
b = a[:]

b[0] = 999

print(a)  # [1, 2, [3, 4, 5]]
print(b)  # [999, 2, [3, 4, 5]]

b[2][1] = 100

print(a)  # [1, 2, [3, 100, 5]]
print(b)  # [999, 2, [3, 100, 5]]

print(f'a[2]와 b[2]가 같은 객체인가? {a[2] is b[2]}')  # True
print(f'a[1]와 b[1]가 같은 객체인가? {a[1] is b[1]}')  # True
print(f'a[1]와 b[1]가 같은 객체인가? {a[0] is b[0]}')  # False
```

얕은 복사는 1차원 리스트에서는 문제가 없지만

다차원 리스트에서 문제가 발생한다!

# 7. 깊은 복사

객체의 모든 수준의 요소를 새로운 메모리에 복사하는 방법 

중첩된 객체까지 모든 새로운 객체로 생성됨

```python
# 깊은 복사

import copy

print('깊은 복사 예시')
a = [1, 2, [3, 4, 5]]
b = copy.deepcopy(a)

b[2][1] = 100

print(a)  # [1, 2, [3, 4, 5]]
print(b)  # [1, 2, [3, 100, 5]]
print(f'a[2]와 b[2]가 같은 객체인가? {a[2] is b[2]}')  # False
```

```python
# 복잡한 중첩 객체 예시
print('복잡한 중첩 객체 깊은 복사')
original = {
    'a': [1, 2, 3],
    'b': {'c': 4, 'd': [5, 6]},
}
copied = copy.deepcopy(original)

copied['a'][1] = 100
copied['b']['d'][0] = 500

print(f'원본: {original}')  # {'a': [1, 2, 3], 'b': {'c': 4, 'd': [5, 6]}}
print(f'복사본: {copied}')  # {'a': [1, 100, 3], 'b': {'c': 4, 'd': [500, 6]}}
print(
    f"original['b']와 copied['b']가 같은 객체인가? {original['b'] is copied['b']}"
)  # False
```

# 참고

# 1. List Comprehension

간결하고 효율적인 리스트 생성 방법

```python
# 사용 전
numbers = [1, 2, 3, 4, 5]
squared_numbers = []

for num in numbers:
    squared_numbers.append(num**2)

print(squared_numbers)
```

`squared_numbers.append(num**2)` 에서 `[]` 먼저 쓰고, `append` 삭제 

```python
# 사용 후

squared_numbers = [numbers**2 for i in numbers]
squared_numbers = list(numbers**2 for i in numbers) # [] 대신 list() 써도 무방
```

```python
# List Comprehension 활용 예시
# "2차원 배열 생성 시 (인접행렬 생성 시)"
data1 = [[0] * 5 for i in range(5)]
data2 = [[0 for i in range(5)] for j in range(5)]
data3 = []
for i in range(5):
    data3.append([0]*5)
    
print(data1)
print(data2)
print(data3)

"""
[[0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0]]
"""
```

# 2. 메서드 체이닝

메서드().   (반환)  /  메서드()

주의사항 None.메서드()

```python
# 문자열 메서드 체이닝
text = 'heLLo, woRld!'
new_text = text
print(new_text)  # HEzzO, WOrLD!
```

```python
# 1. 단계별로 실행하기
text = 'heLLo, woRld!'
step1 = text.swapcase()
print('1단계 결과:', step1)  # HEllO, WOrLD!

step2 = step1.replace('l', 'z')
print('2단계 결과:', step2)  # HEzzO, WOrLD!

# 2. 한 줄로 실행하기 (위와 동일한 결과)
new_text = text
print('최종 결과:', new_text)  # HEzzO, WOrLD!
```

문자열 메서드는 None 주의 안해도 됨~

```python
numbers = [3, 1, 4, 1, 5, 9, 2]
result = numbers.copy().sort()
print(numbers)  # [3, 1, 4, 1, 5, 9, 2] (원본은 변경되지 않음)
print(result)  # None (sort() 메서드는 None을 반환하기 때문)

# 잘못된 체이닝 방식 2
result = numbers.append(7).extend([8, 9])  # AttributeError

# 개선된 방식
# 필요한 경우 새로운 리스트 객체를 반환하는 함수를 사용하는 것이 좋음
sorted_numbers = sorted(numbers.copy())
print(sorted_numbers)  # [1, 1, 2, 3, 4, 5, 9]
```

`numbers.append(7)` 의 반환값은 `None` 임

# 3. 문자 유형 판별 메서드

### isdecimal()

- 문자열이 모두 숫자 문자(0~9)로만 이루어져 있어야 True

### isdigit()

- + 유니코드 문자까지 인식 (예 : 1️⃣)

### isnumeric()

- ++ 분수, 지수, 루트 기호도 인식

```python
isdecimal(-1)
'1'.isdecimal
print('1'.isdecimal)
'1'.isdecimal()
'-1'.isdecimal()

a = -1
a.isdecimal # error 
```

문자 판별만 가능함! `-` 기호가 아니라 문자로 판별함.
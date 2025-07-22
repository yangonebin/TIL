
# 목차
1. list
2. tuple
3. range
4. dict
5. set
6. other type
7. collection
8. 형 변환
9. 연산자
10. 참고

# list
`[]`안에 `,` 로 구분

시퀀스 자료형 = 순서대로 저장 = 인덱싱. 슬라이싱, 길이 확인, 반복 가능

mutuable = 수정 가능

중첩 리스트 가능

```python
my_list = [1,2,3,'python',['hello','world','!!!']]

print(len(my_list)) # 5
print(my_list[-1][1][0]) # w
```

**⚠️ 문자열도 시퀀스임**

```
my_list = [1, 2, 3, 4, 5]
my_list[2:4] = ['three', 'four', 'five']
print(my_list) # [1, 2, 'three, 'four', 'five', 5] 
```


슬라이싱으로 값 수정할 때, 인덱스 초과할 경우 방이 밀린다.




💡리스트는 신이야! 문자열도 시퀀스다! 

# tuple

`()` 안에 값들을 `,` 로 구분하여 생성

시퀀스 자료형 = 순서대로 저장 = 인덱싱. 슬라이싱, 길이 확인, 반복 가능

immutuble (수정 불가능)
```
my_tuple_1 = ()
my_tuple_2 = (1)

print(type(my_tuple_2))
# <class 'int'>
```

단일 요소 튜플일 때, `,` 사용하지 않으면 `int` 로 저장됨!


튜플은 왜 쓰는 걸까? 
```
x, y = 1, 2
x, y = y, x

# 실제 내부 동작
temp = (y,x)
x, y = temp
print(x, y) 
```


내부 동작에서 사용한다! 


💡튜플은 파이썬 내부동작에서 사용된다! 우리는 안 쓴다. 수정불가능한 리스트.

# range

`range(start, stop, step)`

엄밀히 말하면 `range`는 함수임.

연속된 정수 시퀀스를 생성하는, immutuable 자료형.

range(n) : 0 부터 n-1 까지 

```python
my_range_1 = range(5)

print(my_range_1) # range(0, 5)
print(list(my_range_1)) # [0,1,2,3,4]

my_range_3 = range(5,0,-1)
print(list(my_range_1)) # [5, 4, 3, 2, 1] 
```

역순이더라도, start는 항상 포함! stop은 불포함!

```
print(list(range(1, 5, -1))) # []
```

에러가 발생되지는 않으나, 결과가 나오지 않음
```
for i in range(1, 10):
  print(i)

# 
1
2
3
4
5
6
7
8
9

```

파이썬은 결과마다 `\n`


# dict

`{}` 안에 값들이 `,` 로 구분

비시퀀스 = 순서와 중복이 없는 = 인덱스x, 슬라이싱x, `len` 은 가능

mutuable 한 

key -value 쌍으로 이루어짐.

```
my_dict = {'apple' = 1, 'banana' = 2, 'kiwi' = 3}

print(my_mydict[1]) #error
print(len(my_dict)) # 3
```

`len` 은 가능!

```
my_dict = {'how much' : 100, 'how much' : 200} 

print(my_dict['how much']) #200
```



💡dict 은 mutubable 가변 자료형임! 따라서 오류가 발생하지 않고, 맨 마지막 변경된 key의 value가 출력!


# set

`{}` 안에 값들이 `,` 로 구분

비시퀀스 = 순서와 중복이 없는 = 인덱스x, 슬라이싱x, `len` 은 가능

mutuable 한  ← *여기까지 딕셔너리와 완전히 일치함* (key -value 쌍이 없음)

```python
my_set_1 = set()
my_set_2 = {1,2,3}
my_set_3 = {1,1,1}

print(my_set_1)  # set()
print(my_set_2)  # {1, 2, 3}
print(my_set_3)  # {1}
```

<aside>
💡세트는 집합이다! 중복 문제는 세트로 쉽게 해결될 수 있다!





# other type

### none

값이 없음을 표현하는 특별한 타입

### boolean

True / False 단 두 가지 값만 가지는 데이터 타입


# collection

여러 개의 값을 하나로 묶어 관리하는 자료형들을 통칭하는 말

str, list, tuple, range, set, dict 데이터 타입 모두 collection 포함



# 불변과 가변


가변 자료는 메모리 주소를 저장하고 있기 때문에 주소만 변경하면 되지만

불가변 자료는 메모리 값을 저장해서 변경할 수 없음

| 변경 | (재)할당 |
| --- | --- |
| 메모리 주소 유지 | 메모리 주소 변경 |
| num = 15 (X) | num = 15 (O) |


# 형 변환

한 데이터 타입을 다른 데이터 타입으로 변환하는 과정

### 1. 암시적 형 변환

파이썬 이 연산 중에 자동으로 데이터 타입을 변환하는 것.

```python
print(3 + 5.0) # 8.0
print(True + 3) # 4
print(True + False) # 1
```

### 2. 명시적 형 변환

암시적 형 변환을 제외한 모든 형 변환. 사용자가 직접 형 변환을 해야함

```
>>> str(100)
'100'
>>> a = str(100)
>>> print(a)
100
```
# 연산자

### 1. 산술 연산자
### 2. 복합 연산자
### 3. 비교 연산자

```
print (2 == 2.0) #True
print (2 is 2.0 ) #False
print (1 is True) #False
```


`==` 연산자는 값(데이터) 같은지 비교

`is` 연산자는 객체 상태 자체가 같은지 비교

```
x = None

# 권장
if x is None:
  print('x는 None입니다.')

# 비권장
if x == None:
  print('x는 None입니다.')

```
`is` 연산자는 싱글턴 객체 비교할 때 사용함

```
a = [1, 2, 3]
b = [1, 2, 3]

print(a==b) #True
print(a is b) #False

b = a
print(a is b) #True
```

`b = a` : 변수 b에 a의 메모리 주소를 할당

## 4. 논리 연산자

거짓으로 취급되는 값들
```
False, 숫자 0, 빈 민자열 "", 빈 리스트 [], None
```
 등 <U>비어있거나 없다</U>는 느낌의 값들


## 5. 멤버십 연산자
특정 값이 시퀀스나 다른 컬렉션안에 포함되어 있는지 확인하는 연산자

  `in`, `not in`

  ## 6. 시퀀스형 연산자
  시퀀스 자료형 (문자열, 리스트, 튜플)에 특별한 의미로 사용되는 연산자


```
print([1,2] * 2) # [1, 2, 1, 2]
```

## 참고
### Trailing Comma
리스트에서는 자주 사용하지 않지만
dict 에서는 많이씀.

```
# 좋은 예시

item = [
    'item1',
    'item2',
]

my_func(
    'value1',
    'value2,
)


# 나쁜 예시

item = ['item1','item2',]

# 한 줄 작성 시에는 불필요

item = ['item1', 'item2']
```



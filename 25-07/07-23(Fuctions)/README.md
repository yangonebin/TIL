# 목차

1. 함수
2. 매개변수와 인자
3. 재귀 함수
4. 내장 함수
5. 함수와 Scope
6. 함수 스타일 가이드
7. Packing& UnPacking
8. 참고

# 1. 함수

재사용 가능한 코드 묶음 for 특정 작업 수행

→ 재사용함으로써, 가독성과 유지보수성 향상

함수를 사용한다 (X)

함수를 호출(call)한다 (O)

### 함수의 구조


input : parameter (매개변수)

output : return value

중간 : docstring (설명서)

전체 : function body  

```python
def make_sum(pram1, pram2) :
	```이것은 두 수를 받아
	두 수의 합을 반환하는 함수입니다.
	```
	return pram1 + pram2
```

1. 함수 정의
    1. 함수 정의는 def 키워드로 시작
    2. def 키워드 이후 함수 이름 작성
    3. 괄호 안에 매개변수를 정의할 수 있음
    4. 매개변수 (parameter)는 함수에 정의된 값
2. 함수 body
    1. 콜론(:) 다음에 들여쓰기 된 코드 블록
    2. 함수가 실행 될 때 수행되는 코드를 정의
3. docstring
4. 함수 반환 값
    1. 필요한 경우 결과 반환 가능 → 반환 값이 없으면 None 반환
    2. return 키워드 이후에 반환할 값 명시
    3. return 문은 함수의 실행을 종료하고, 결과를 호출 부분으로 반환
5. 함수 호출
    1. 함수를 사용하기 위해서는 호출이 필요
    2. 함수의 이름과 소괄호를 활용해 호출
    3. 필요한 경우 인자(argument)를 전달해야함
    

```python
def make_sum(pram1, pram2):
    """이것은 두 수를 받아
    두 수의 합을 반환하는 함수입니다.
    >>> make_sum(1, 2)
    3
    """
    # return pram1 + pram2 해도 됨
    result = pram1 + pram2
    return result

sum_result = make_sum(100,300)
print(sum_result) # 400
```

```

make_sum(100, 30)
print(make_sum)

# make_sum 의 주소 반환
```
함수를 값으로 사용할 수 없음.



`print()` 함수는 `retrun` 값이 없음!

```python
return_value = print(1)
print(return_value) # None
```


💡출력과 반환은 다름! 

</aside>

```python
return_value = print(1)  
print(return_value) 

# 결과 화면
1
None
```

할당문은 오른쪽 문장을 먼저 실행! 따라서 `1` 이 출력된 후, 할당됨

# 2. 매개변수와 인자

함수를 정의할 때, 함수가 받을 값을 나타내는 변수

```python
def add_number(x, y) # x와 y는 매개변수(parameter)

sum result = add_number(a, b) # a와 b는 인자(argument)
```

## 인자의 종류

### 1. 위치 인자

함수 호출 시 반드시 인자의 위치에 따라 전달

```python
def greet(name, age):
	print(f'안녕하세요, {name}님! {age}살이시군요.'
	
greet(25, 'Alice') # 안녕하세요, 25님! Alice살이시군요.
greet('Alice') # error
```

### 2. 기본 인자 값

함수 정의에서 매개변수에 기본 값을 할당 하는 것

```python
def greet(name, age=30):
	print(f'안녕하세요, {name}님! {age}살이시군요.'
	
greet('Alice') # 안녕하세요, Alice님! 30살이시군요.
greet('Alice', 40) # 안녕하세요, Alice님! 40살이시군요.
```

### 3. 키워드 인자

함수 호출 시 인자의 이름과 함께 값을 전달. 즉 위치 인자와 다르게, 순서가 중요하지 않음!

```python
def greet(name, age):
	print(f'안녕하세요, {name}님! {age}살이시군요.'
	
greet(age = 30, name = 'Alice') # 안녕하세요, Alice님! 30살이시군요.
greet(age = 35, 'Alice') # error 
```

<aside>
⚠️호출 시, 키워드 인자는 위치 인자 뒤에 위치해야 함

</aside>

### 4. 임의의 인자 목록 (Arbitary Argument Lists)

정해지지 않은 개수의 인자를 처리하는 인자

함수 정의시 매개변수 앞에 `*` 를 붙여 사용

여러 개의 인자를 tuple로 처리

```python
def calculate_sum(*args) :
	print(args) # (1, 100, 5000, 30)
	print(type(args)) # <class 'tuple'>
	

calculate_sum(1, 100, 5000, 30)
```

### 5. 임의의 키워드 인자 목록

정해지지 않은 개수의 키워드를 인자를 처리하는 인자

함수 정의시 매개변수 앞에 `**` 를 붙여 사용

여러 개의 인자를 dictionary로 묶어 처리

```python
def print_info(**kwargs) :
		print(kwargs)
		
print_info(name = 'Eve' , age = 30) # {'name' : 'Eve' , 'age' : 30} 
```

### 함수 인자 권장 순서

위치 → 기본 → 가변 → 가변 키워드

```python
def func(pos1, pos2, default_arg = 'default', *args, **kwargs, pos3, pos4) :

func(1, 2, 3, 4, 5, 6, key1 = 'value1', key2 = 'value2', 7, 8)
```

`default` 에 문자열을 넣는다는 의미가 아니라, 값이 없으면 `defalut`를 반환하라는 것임.

<aside>
⚠️ 위치 인자는 뒤로 갈 수 없음!

why? 임의의 인자 목록이 전부 할당 받기 때문. 

</aside>

```python
def func(pos1, pos2, default_arg = 'default', *args, **kwargs) :
    
    print('default_arg:', default_arg)
    print('args:', args)
    print('kwargs:', kwars)
    
func(1, 2, 3, 4, 5, 6, key1 = 'value1', key2 = 'value2') 

# 
default_arg: 3
args: (4, 5, 6)
kwargs: {'key1' : 'value1', 'key2' : 'value2'}
```

# 3. 재귀 함수

함수 내부에서 자기 자신을 호출하는 함수

특정 알고리즘 식을 표현할 때, 변수의 사용이 줄어들어 코드 가독성이 높아짐

반드시 1개의 이상의 base case(종료되는 상황)가 존재하고, 수렴하도록 작성


⚠️종료 조건을 명확히 하고, 반복되는 호출이 종료 조건을 향하도록 할 것.

</aside>

# 4. 내장 함수

별도의 import 없이 바로 사용 가능한 파이썬이 기본적으로 제공하는 함수

built-in function 이라고 함.



# 5. 함수와 Scope

함수는 코드 내부에 `local scope` 를 생성하며,  그 외의 공간인 `global scope` 로 구분

```python
def func():
	num = 20
	print('local' , num) # local 20
	
func()

print('global', num) # error
```

### 변수 수명주기(lifecycle)

1. built - in scope : 파이썬이 실행된 이후부터 영원히 유지
2. global scope : 모듈이 호출된 시점 이후 혹은 인터프리터가 끝날 때까지 유지
3. local scope : 함수가 호출될 때 생성되고, 함수가 종료될 때까지 유지


```python
print(sum) # <built-in function sum>
print(sum(range(3))) # 3

sum = 5
print(sum) # 5
print(sum(range(3))) # error
```

정의와 호출 중요함.

호출할 때 무엇을 가져오는가.

밖에서는 가져올 수 있지만, 안에서는 가져올 수 없음

<aside>
⚠️ global 은 도시거리, local은 집안. 집안에서는 도시거리 볼 수 있지만, 도시거리에서는 집 안 못 봄!

</aside>

### global 키워드

함수 내에서 전역 변수를 수정할려는 경우 사용

```python
num = 0 # 전역 변수

def increment():
		global num # num을 전역 변수로 선언
		num += 1
		
print(num) # 0 
increment() 
print(num) # 1
```

### global 키워드 주의 사항

```python
num = 0 

def increment()
	print(num)
	global num
	num += 1
	
#error  
```

`global` 키워드 선언 전에는 참조 불가

```python
num = 0 
 
def increment(num)
	global num
	num += 1
	
#error  
```

매개변수에는 `global` 키워드 사용 불가

# 6. 함수 스타일 가이드

### 단일 책임 원칙 (Single Responsibility Principle)

모든 객체는 하나의 명확한 목적과 책임만을 가져야 함.

1. 명확한 목적 : 함수는 한가지 작업만 수행
2. 책임 분리 : 검증, 처리, 저장 등을 별도 함수로 분리 
3. 유지보수성 : 작은 단위의 함수로 나누어 관리

# 7. Packing & Unpacking

### 패킹

여러 개의 데이터를 하나의 컬렉션으로 모아 담는 과정

```python
packed_values = 1, 2, 3, 4, 5
print(packed_values) # (1, 2, 3, 4, 5)
```

`*` 활용한 패킹 (함수 매개변수 작성 시)

```python
def my_func(*args)
	print(args) # (1, 2, 3, 4, 5)
	print(type(args)) # <class 'tuple'>
	
my_func(1, 2, 3, 4, 5)
	
```

`**` 활용한 패킹 (함수 매개변수 작성 시)

```python
def my_func(**kwargs)
	print(kwargs) # {'a' : 1,'b' : 2,'c' : 3}
	print(type(kwargs)) # <class 'dict'>
	
my_func(a=1, b=2, c=3)
	
```

### 언팩킹

컬렉션에 담겨있는 데이터들을 개별 요소로 펼쳐 놓는 과정

```python
def my_dict(x, y, z):
	print(x, y, z) 
	
my_dict = { 'x' : 1, 'y' : 2, 'z' : 3}
my_function(**my_dict) # 1 2 3
```

# 8. 참고

### 함수의 반환

파이썬 함수는 언제나 단 하나의 값(객체)만 반환할 수 있음

```python
def get_user_info():
	name = 'Alice'
	age = 30
	return name, age # 콤마(,)로 여러 값을 반환하는 것처럼 보임
	
user_data = get_user_info()

print(user_data) # ('Alice',30) 단 하나의 튜플로 반환함.
```

### 람다 표현식

```python
number = [1, 2, 3, 4, 5]

def square(x):
	return x**2
	
#lambda 미사용
squared1 = list(map(square, number))
print(squared1) # [1, 4, 9, 16, 25]

#lambda 사용
squared2 = list(map(lambda x: x**2,number))
print(squared1) # [1, 4, 9, 16, 25]
```



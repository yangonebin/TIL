# 목차

1. 모듈 
2. 파이썬 표준 라이브러리
3. 제어문
4. 조건문
5. 반복문
6. 참고

# 1. 모듈

힘수와 변수의 묶음

즉, 파이썬 파일(.py) 하나 

### Import 문 사용

같은 이름의 함수가 여러 모듈에 있을 때 충돌을 방지할 수 있음

```python
#import 문 사용
import math

print(math.pi)        # 모듈명.변수명
print(math.sqrt(4))   # 모듈명.변수명
```

```python
# from 절 사용
from math import pi, sqrt

print(pi)
print(sqrt(4))
```

### from 절 사용시 주의사항

1. 사용자가 선언한 변수 또는 함수와 겹치게 되면, 동작이 이루어 지지 않음.

```python
from math import sqrt
math_result = sqrt(16) # 실수형 4.0

def sqrt(x):
		return str(x ** 0.5) 

my_reult = sqrt(16) # 문자형 4.0
```

1. 서로 다른 모듈에서 improt된 변수나 함수의 이름이 같은 경우 이름 충돌 발생

```python
from math import sqrt     #math.sqrt가 먼저 import됨
from my_math import sqrt  #my_math.sqrt가 math.sqrt를 덮어씀

result = sqrt(9) # math.sqrt가 아닌 my_math.sqrt가 사용됨
```

1. `import *`  지양
2. `as` 키워드로 별칭 가능

### 사용자 정의 모델

```python
# my_math.py
def add(x ,y):
		return x + y
		
# sample.py
import my_math

print(my_math.add(10,20)) # 30
```

[sample.py](http://sample.py) 에서  print(add(10,20)) 는 실행이 안됨. 꼭 변수명 앞에 모둘명 기입하기

# 2. 파이썬 표준 라이브러리

PSL : 파이썬 언어와 함께 제공되는 다양한 모듈과 패키지의 모음

### 패키지

연관된 모듈들을 

하나의 디렉토리로 모아 놓은 것

즉, 폴더

```python
# sample.py

from my_package.math import my_math
from my_package.statistics import tools

print(my_math.add(1,2)) # 출력: 3
print(tools.mod(1,2))   # 출력: 1
```

>>>>>>>>>>> python_codes

>>>>>>>> my_package 

>>> math

> my_math.py

>>>statistics 

> tools

>>>>>>>> [sample.py](http://sample.py) (my_package 밖에 있어야 함!)



From 패키지 에서 import 모듈

# 3. 제어문

조건에 따라 반복적으로 코드를 실행

# 4. 조건문

주어진 조건이 참인 경우에만 코드를 수행

- if 문
- elif 문
- else 문
- 복수 조건문 : 조건이 동시에 검사하는 것이 아니라 “순차적으로” 비교

```python
dust = 155

if dust > 30 :
	print("보통")
	
elif dust > 50 :
	print("나쁨")
	
else:
	print("좋음")   # 결과 : "보통"
```

- 중첩 조건문 : if문 안에 if문 가능

# 5. 반복문

주어진 코드를 여러 번 반복해서 실행

## 1. for 문

반복 가능(iterable)한 객체의 요소들을 반복하는데 주로 사용

반복 횟수가 정해져 있음

시퀀스 자료형 (list, tuple, str) 뿐만 아니라 비 시퀀스 자료형 (dict, set) 등도 반복 가능한 객체임.

```python
students = ['alice', 'harry', 'bob']

for student in students:
    print(f'{student} hi !' )
   
# student는 변수임. 
```

⚠️for 변수 in 반복 가능한 객체:

</aside>

문자열도 시퀀스 자료임

```python
# 문자열 순회
country = 'Korea'

for char in country:
    print(char)
```

range 순회

```python
# range 순회
for i in range(5):
    print(i)
```

딕셔너리 순회

```python
# dictionary 순회
my_dict = {
    'x': 10,
    'y': 20,
    'z': 30,
}

for key in my_dict:
    print(key)
    print(my_dict[key])
```

인덱스로 리스트 순회

```python
# 인덱스 순회
numbers = [4, 6, 10, -8, 5]

for i in range(len(numbers)):
    numbers[i] = numbers[i] * 2

print(numbers)
```

중첩된 반복문

```python
outers = ['A', 'B']
inners = ['c', 'd']

for outer in outers:
	for inner in inners:
		print(outer. inner)
		
# 'A', 'c'
  'A', 'd'
  'B', 'c'
  'B', 'd'
```

중첩 리스트 순회

```python
elements = [['A', 'B'], ['c', 'd']]

# 1
for elem in elements:
    print(elem)
    
#
['A', 'B']
['c', 'd']

# 2
for elem in elements:
    for item in elem:
        print(item)
        
#
A
B
c
d
```

## 2. while 문

조건이 참인 동안 반복

반복 횟수가 정해져 있지 않음 → 무한 반복 조심해야함

```python
a = 0

while a < 3 :
    print(a)
    a += 1

print("끝")
```

while 문은 몇 번 반복되는지 명시적이지 않음.

그보다는 로직을 만족하는지 여부가 더욱 중요함

반드시 종료 조건이 필요하다.

### 사용자 입력에 따른 반복

```python
number = int(input('양의 정수를 입력해주세요.: '))

while number <= 0:
    if number < 0:
        print('음수를 입력했습니다.')
    else:
        print('0은 양의 정수가 아닙니다.')

    number = int(input('양의 정수를 입력해주세요.: '))

print('잘했습니다!')

```

`while` 문과 `if` 혼용 가능

### for 문과 while  문 비교

| for 반복문 | while 반복문 |
| --- | --- |
| iterable 요소를 하나씩 순회하며 반복 | 주어진 조건식이 참인 동안 반복 |
| 반복 횟수가 명확하게 정해져 있는 경우 유용  | 반복 횟수가 불명확하거나 조건에 따라 반복을 종료해야 할 때 유용 |
| 리스트, 튜플, 문자열, range() | 사용자의 입력을 받아 특정 조건 충족될 때까지 |
| 반복 횟수가 정해져 있음 | 반복 횟수가 미리 정해져 있지 않음 |

## 3. 반복 제어

### break 키워드

해당 키워드를 만나게 되면 남은 코드를 무시하고 반복 즉시 종료

반복을 끝내야 할 명확한 조건이 있을 때 사용

```python
for i in range(10):
    if i == 5:
        break
    print(i)  # 0 1 2 3 4
```

### continue 키워드

해당 키워드를 만나게 되면 다음 코드는 무시하고 다음 반복을 수행

```python
# continue 키워드 기본
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)  # 1 3 5 7 9
```

### pass 키워드

‘아무 동작도 하지 않음’을 명시적으로 나타내는 키워드 

`None` 이랑 비슷함. 

```python
def my_function():
	pass # 없으면 error
```

# 6.참고

## 1. map 함수

map(function, iterabe)



iterable 의 모든 요소에 function 을 적용하고 

그 결과를 map object로 묶어서 반환시킴

```markdown
[toc] 

# `map`은 게으른 요리사 레시피

> "map은 당장 요리하지 않고, '요리법(레시피)'만 가지고 있는 게으른 요리사와 같기 때문"

## 1\. `map`은 '요리법'이다

코드를 보면서 이해해 봅시다. 숫자 리스트의 각 요소를 2배로 만드는 작업을 하고 싶다고 가정해 봅시다.

```python
numbers = [10, 20, 30]

# "각 숫자를 2배로 만들어라" 라는 '요리법'을 만듭니다.
recipe = map(lambda x: x * 2, numbers)

# 요리법(recipe)을 출력해 봅시다.
print(recipe)
```

**실행 결과:**

```
<map object at 0x10e7b9c10>
```

결과가 `[20, 40, 60]`이 아니라 `map object at ...`라고 나옵니다.

이건 파이썬이 `"알겠습니다! 'numbers'에 있는 각 재료를 2배로 만들라는 '요리법'은 제가 잘 가지고 있어요. 메모리(0x10e7b9c10)에 보관 중입니다."`라고 대답하는 것과 같습니다.

`map`은 함수와 리스트를 받아서 '어떻게 처리할지'에 대한 계획, 즉 '요리법'만 만들 뿐 실제로 그 작업을 바로 실행하지는 않습니다.

-----

## 2\. 결과를 보려면 '요리'를 시켜야 한다

이 게으른 요리사에게 실제로 요리를 시켜서 결과물을 눈으로 보려면 어떻게 해야 할까요?
`"이제 그 요리법대로 요리해서 상에 차려줘!"`라고 명확하게 지시해야 합니다.

### 방법 1: `list()`로 상 차리기 (가장 흔한 방법)

`list()`로 `map`을 감싸는 것은 "요리법에 있는 모든 재료를 한 번에 다 요리해서, '리스트'라는 접시에 순서대로 담아줘\!"라고 지시하는 것과 같아요.

```python
# '요리법(recipe)'대로 요리해서 list 접시에 담아달라고 요청합니다.
dishes = list(recipe)

# 결과가 담긴 접시를 출력합니다.
print(dishes)
```

**실행 결과:**

```
[20, 40, 60]
```

이제야 우리가 원했던 결과가 보입니다. `list()`가 `map`에게 일을 시켜서 실제 결과물을 만들어 낸 것입니다.

### 방법 2: `for`문으로 하나씩 요리하기

`for` 반복문은 "요리사님, 요리 하나씩 완성될 때마다 바로바로 가져다주세요\!"라고 요청하는 것과 같습니다.

```python
# '요리법(recipe)'을 for문으로 순회합니다.
# for문은 recipe에게 "다음 요리 주세요"를 계속 요청합니다.
for dish in recipe:
    print(dish)
```

**실행 결과:**

```
20
40
60
```

`for`문이 `map` 객체를 순회하면서 요소를 하나씩 요청할 때마다 `map`이 그제야 하나씩 계산해서 결과를 내어주는 방식입니다.

-----

## 3\. 왜 이렇게 '게으르게' 만들었을까?

바로 **효율성** 때문입니다.

만약 처리해야 할 데이터가 10억 개라고 상상해 보세요. `map`이 요리법만 만들지 않고 처음부터 10억 개를 전부 계산해서 리스트로 만든다면 엄청난 시간과 메모리가 낭비될 거예요.

하지만 `map`은 '게으르게' 계획만 세워두고, 우리가 **결과를 달라고 요청하는 시점에 필요한 만큼만** 계산합니다. 이런 방식을 통해 파이썬은 매우 효율적으로 대용량 데이터를 처리할 수 있습니다.

-----

## 4\. 또 다른 게으른 친구들: `range`와 `zip`

파이썬에는 `map`처럼 게으르게 동작해서 효율적인 친구들이 더 있습니다.

### `range` - 숫자 생성 계획서

`range(100)`은 0부터 99까지의 숫자가 담긴 리스트가 아닙니다. "요청하면 0부터 99까지 숫자를 차례대로 줄 수 있다"는 **약속 또는 계획서**와 같습니다.

```python
# 0부터 99까지 숫자를 만들 '계획'
num_plan = range(100)

# 계획서 자체를 출력
print(num_plan)
# >> range(0, 100)

# list()로 모든 숫자를 만들어달라고 요청
print(list(num_plan))
# >> [0, 1, 2, ..., 99]
```

`range` 덕분에 숫자 100개를 미리 메모리에 저장하지 않아도 됩니다.

### `zip` - 짝매칭 계획서

`zip`은 여러 리스트의 요소들을 어떻게 짝지을지에 대한 계획을 세웁니다. 마치 옷의 지퍼처럼, 우리가 채울 때만 한 칸씩 짝이 맞춰집니다.

```python
names = ['철수', '영희']
scores = [90, 85]

# 두 리스트를 짝지을 '계획'
pair_plan = zip(names, scores)

# 계획 자체를 출력
print(pair_plan)
# >> <zip object at ...>

# list()로 모든 짝을 만들어달라고 요청
print(list(pair_plan))
# >> [('철수', 90), ('영희', 85)]
```

이처럼 `map`, `range`, `zip`은 모두 **'일단 계획만 세워두고, 필요할 때 요청하면 그때 처리해주는'** 게으르고 효율적인 방식으로 동작합니다.

## 핵심 요약

  * **`map()`, `range()`, `zip()`**: "이렇게 처리하라"는 **계획 또는 레시피**일 뿐, 아직 실행되지 않은 상태입니다.
  * **`list(...)`**: "계획을 **전부 실행**해서 그 결과를 리스트에 담아줘\!"라는 명령입니다.
  * **`for item in ...`**: "계획을 **하나씩 실행**해서 보여줘\!"라는 명령입니다.

따라서 `map object`나 `zip object`, `range(0, 100)` 같은 메시지를 본다면, "아, 파이썬이 내 지시를 이해하고 실행할 계획을 세웠구나. 이제 `list()`나 `for`문으로 실행만 시키면 되겠다\!"라고 생각하시면 됩니다.



⚠️map은 게으른 요리사다!

</aside>

```python
# map 함수 사용 기본
numbers = [1, 2, 3]
result = map(str, numbers)

print(result)  # <map object at 0x00000239C915D760>
print(list(result))  # ['1', '2', '3']
```

## 2. zip

```python
girls = ['jane', 'ashley']
boys = ['peter', 'jay']
pair = zip(girls, boys)

print(pair)  # <zip object at 0x000001C76DE58700>
print(list(pair))  # [('jane', 'peter'), ('ashley', 'jay')]
```

## 3. for - else

`for` 루프가 `break` 를 만나 중단되지 않고, 끝까지 정상적으로 완료되었을 때만 else 블록이 실행

```python
# for-else 구문 기본
for i in range(5):
    print(i)
    if i == 3:
        # break 문이 실행되면 else 블록은 실행되지 않음
        print('반복이 중단되었습니다.')
        break
else:
    print('이 메시지는 출력되지 않습니다.')
    
# 결과
0
1
2
3
반복문이 중단 되었습니다.
```

## 4. enumerate

```python
# enumerate 함수 기본
fruits = ['apple', 'banana', 'cherry']

for index, fruit in enumerate(fruits):
    print(index, fruit)
    
# 결과
0 apple
1 banana
2 cherry
```

```python
enumerate 함수 활용 2
# 인덱스 정보를 활용하여 특정 조건에 맞는 요소 찾기
respondents = ['은지', '정우', '소민', '태호']
answers = ['', '좋아요', '', '괜찮아요']

for i, response in enumerate(answers):
    if response == '':
        print(f"{respondents[i]} 미제출")

fruits = ['apple', 'banana', 'cherry']

for a, b in enumerate(fruits):
        print(a, b)

# 결과
은지 미제출
소민 미제출
```
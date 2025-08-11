# 목차

1. 문자열
    1. 코드체계
    2. 문자열
    3. 연습문제
    4. 연산
2. 패턴매칭
    1. 고지식한 패턴 검색
    2. KMP 알고리즘
    3. 보이어-무어 알고리즘
    4. 문자열 암호화

# 1. 코드체계

문자에 대응되는 숫자를 정한 것.

영어가 대소문자 합쳐서 52자이므로 (26*2)

6비트면 (64)면 저장할 수 있음.

### 코드체계의 문제

근데 여기서 문제가 발생함.

네트워크가 발전되기 전 미국의 각 지역 별로 코드체계를 정해 놓다보니

```python
000000 → a 000001 → b : # A회사
000000 -> a 100000 -> b : # B회사
```

이렇게 제각각이었던 거임.

그래서 통일할 필요성이 있었음. 

그렇게 탄생한 게 바로

### ASCII 코드

1967년, 미국에서 ASCII(American Standard Code for Information Interchange)라는 문자 인코딩 표준이 제정됨.

ASCII는 7-bit 인코딩으로 128문자를 표현하며 33개의 추력 불가능한 제어 문자들과 공백을 비롯한 95개의 출력 가능한 문자들로 이루어짐.

### 확장 아스키

여기서 1-bit를 더 추가해서 128개를 더 쓸 수 있게함.

근데 이건 자율성을 보장한 거임. 

그래서 지역마다 다 다름.

### 유니코드

컴퓨터가 발전하면서 미국 뿐 아니라 각 나라에서 컴퓨터가 발전함.

따라서 다국어 처리를 위한 표준이 필요해졌음.

그게 바로 유니코드임.

유니코드는 비영리 단체인 유니코드 컨소시엄에서 관리함.

이모지도 유니코드 문자임

```python
'A' 의 유니코드는 16진수로 0041 (10진수로 65)
'덤'의 유니코드는 16진수로 B364
따라서 print('|B364')로 '덤' 출력 가능

print('\uB364') # 덤

```

### 바이트 단위 순서

바이트 단위 저장 순서가 정해지지 않은 경우 잘못된 해석 가능성

0041 이라고 했을 때

1 byte (4 bit)를 저장할 수 있기 때문에

00

41

(Big - endian)

혹은

41

00

(Little - endian)

으로 저장할 수 있음

### 유니코드 인코딩(UTF : Unicode Transformation Format)

`UTF - 8 (in web)`

Min : 8 - bit

Max : 32 - bit ( 1 Byte * 4)

필요한 크기에 따라 가변적으로 저장한다.

0xxxxxxx → 7 bit 사용가능 

110xxxxx 10xxxxxx → 5+6 = 11 bit 사용가능

1110xxx .. 10xx .. 10xxx

`UTF - 16 (in windows, java)`

Min : 16 - bit

Max : 32 - bit (2 Byte * 2)

`UTF - 32 (in unix)` 

Min : 32 - bit

Max : 32 - bit (4 Byte * 1)

# 2. 문자열

### 문자열의 분류

- Length-Controlled 문자열

문자열의 길이 정보를 함께 저장해서, 그 길이 만큼 문자 데이터를 읽는 방식

- Delimited 문자열

문자열을 끝을 나타내는 특정한 구분자(Delimiter) 가 있어서, 구분자가 나올 때까지 문자열로 인식. (예: `\0`)

### C언어에서 문자열

문자열은 문자들의 배열 형태로 구현된 응용 자료형

문자배열에 문자 저장할 때는 항상 마지막에 끝을 표시하는 널문자`\0` 필요.

### Python3에서의 문자열

- 연산

ab + c = abc

ab * 3 = ababab

- squence & imuutable

```python
s = ‘abc’
print(s[1]) # b

s = 'abc'
s[1] = 'a] # error

str =[]
for i in s:
    str.append(i)

str[1] = 'B'
str = ''.join(str)
print(str) # aBc
```

### 연습 문제

s1의 각 글자가 s2에 모두 존재하는가?

```python
XYPV
EOGGXYPVSY

s1 = input()
s2 = input() # 좋지 않음

s1 = list(input())
s2 = list(input()) # 옳은 방향
```

# 3. 연산

### 문자열 뒤집기

```python
s = 'ABCD'
s = list(s)
s.reverse()
s = ''.join(s)
```

### 문자열 비교

```python
s1 = 'abc'
s2 = 'abc'
s3 = 'def'
s4 = s1
s5 = s1[:2] + 'c'

print(s1 == s2) # True
print(s1 is s2) # True
print(s4 == s5) # True
print(s4 is s5) # False

a = [1,2,3]
b = [1,2,3]

print(a == b) # True
print(a is b) # False (다른 객체임)
```

### C 와 Java에서의 문자열 비교

- C
    - strcmp() 함수를 사용해 문자열의 내용 비교
- Java
    - == 연산자는 객체의 주소 비교 (Python의 is 연산자 역할)
    - equals() 메서드는 객체의 내용 비교 (Python의== 역할)

### 사전 순서 비교

비교 연산자 < 사용 

유니코드를 비교함

```python
'Apple' < 'apple' # True
'Zebra' < 'apple' # Ture
```

### 문자열 숫자를 숫자로 변환

```python
a = int('123')
b = float('3.14')
c = int('A0', 16) # 문자열 'AO'를 16진법으로 해석해서 변환

d = int('10',16) # 16
e = int(10,16) # error 
```

# 4. 고지식한 패턴 검색

```python
def brute_force(p, t) : # p 찾을 패턴, t 본문 문자열, 패턴이 있으면 인덱스, 없으면 -1 리턴
	i = 0 # t의 인덱스
	j = 0 # p의 인덱스
	M = len(p)
	N = len(t)
	while j < M and i < N :
		if t[i] != p[j] : # 다른 글자인 경우
			i = i - j
			j = -1
		i = i + 1
		j = j + 1
	if j == M : return i - M # 검색 성공
	else : return -1 # 검색 실패
```

최악 시간 복잡도 O(MN)

길이가 10,000인 문자열 길이 80인 패턴을 찾는 경우

10,000 * 80 = 800,000

# 5. KMP 알고리즘

### LPS(Longest Prefix and which is also Suffix)배열

- 접두사이자 접미사인 문자열의 최대 길이
- 일치하지 않을 때 비교할 인덱스
- 구현에 따라 next, pi 배열로도 불림

# 6. 보이어-무어 알고리즘

패턴 오른쪽 끝에 있는 문자가 불일치 하고 이 문자가 패턴 내에 존재하지 않는 경우, 이동 거리는 패턴의 길이만큼 됨.
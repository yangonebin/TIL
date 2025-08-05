# 목차

1. 알고리즘
2. 배열
3. 연습 문제
4. 버블 정렬
5. 카운팅 정렬
6. 완전 검색
7. 탐욕 알고리즘

# 알고리즘

문제를 해결하기 위한 절차나 방법 

### APS

Algorithm Problem Solving

### 의사코드(슈도코드,Pseudocode)와 순서도

컴퓨터 분야에서 알고리즘을 표현하는 방법

![내 이미지](image\image.png)

### 알고리즘의 성능

좋은 알고리즘이란?

1. 정확성 : 얼마나 정확하게 동작하는가
2. 작업량 : 얼마나 적은 연산으로 원하는 결과를 얻어내는가
3. 메모리 사용량 : 얼마나 적은 메모리를 사용하는가
4. 단순성: 얼마나 단순한가
5. 최적성 : 더 이상 개선할 여지없이 최적화되었는가

### 알고리즘의 시간 복잡도

- 실제 걸리는 시간을 측정
- 실행되는 명령문의 개수를 계산

### 알고리즘 성능 비교 예시

```python
def CalcSum( n ) :
	sum <- 0; # 1번
	for i in range (1, n+1) : # n번
		sum <- sum + i; # n번
	return sum;
	
	# 1 + n * 2 = 2n + 1
```

```python
def CalcSum ( n ) :
	return n * (n + 1) // 2 # 3번
	
	# 3번의 연산
```

### 시간 복잡도 표시

빅-오 표기법(Big-O Notation)을 언급하는 경우가 많음

시간 복잡도 함수 중에서 가장 큰 영향력을 주는 n에 대한 항만을 표시

계수(Coefficient)는 생략하여 표시

# 2. 배열(Array)

일정한 자료형의 변수들을 하나의 이름으로 열거하여 사용하는 자료구조

배열을 사용하면 하나의 선언을 통해서 둘 이상의 변수를 선언

### 1차원 배열

```python
arr =list()
arr = []
arr = [0] * 10
arr = [1,2,3]

arr[0] = 10 # 배열 arr의 0번 원소에 10을 저장하라
arr[idx] = 20 # 배열 arr의 idx번 원소에 20을 저장하라
```

### 입력 받은 정수를 1차원 배열에 저장하는 방법

```python
N = int(input())
arr = list(map(int, input().split()))
```

### 배열 원소의 합 s 계산하기

```python
s = 0
for i in range(N): # for x in arr:
	s += arr[i] # s += x
```

### 배열 원소 중 최댓값 max_v 찾기

```python
max_v = arr[0] # 첫 원소를 최대로 가정
for i in range(1, N):
	if max_v < arr[i]
		max_v = arr[i] 
```

### 배열 원소 중 최댓값의 인덱스 max_idx 찾기

```python
max_idx = 0 # 첫 원소를 최대로 가정
for i in range(1, N):
	if arr[max_dix] < arr[i]:
		max_idx = i
```

### 최댓값이 여러 개인 경우 마지막 인덱스 max_idx 찾기

```python
max_idx = 0 # 첫 원소를 최대로 가정
for i in range(1, N):
	if arr[max_idx] <= arr[i]
		max_idx = i 
```

### 찾는 값이 배열이 있으면 해당 원소의 인덱스, 없으면 -1을 idx에 넣기

```python
# input
6 5
2 7 5 3 1 7

N, V = map(int, input().split()) # N, 찾는값 V
arr = list(map(int, input().split()))

idx = -1 # 찾는 값이 없다고 가정
for i in range(N):
	if arr[i] == V:
		idx = i
		break # for i를 break
```

# 3. 연습문제

```python
T = int(input())
for test_case in range(1, T+1)
	N = int(input())
	ai = list(map(int, input().split()))

	diff = max(ai) - min(ai)
	print(f'#{test_case} {diff})
```

```python

```

# 4. 버블 정렬

### 정렬이란?

2개 이상의 자료를 키(특정 기준)에 의해 재배열하는 알고리즘

### 정렬의 종류

1. 버블 정렬
2. 카운팅 정렬
3. 선택 정렬
4. 퀵 정렬
5. 삽입 정렬
6. 병합 정렬

### 버블 정렬

인접한 두 개의 원소를 비교하며 자리를 계속 교환하는 방식

시간 복잡도 `O(n^2)`

교환하며 자리를 이동하는 모습이 물 위에 올라오는 거품 모양과 같음

한 단계가 끝나면 가장 큰 원소가 마지막 자리에 정렬된다.

```python
# 의사코드(pseudocode)
BubbleSort(a, N)
	for i : N-1 -> 1
		for j 0 -> i-1
			if a[j] > a[j+1]
				a[j] <-> a[j+1]
```

```python
# 코드 구현
def bubble_sor(a, N) : # 정렬할 List, N 원소 수
	for i in range(N-1, 0 , -1) : # 범위의 끝 위치 
		for j in range(i) :
			for j in range(i) :
				if a[j] > a[j+1] :
					a[j], a[j+1] = a[j+1], a[j]
```

# 5. 카운팅 정렬

항목들의 순서를 결정하기 위해 집합에 각 항목이 몇 개씩 있는지 세는 작업을 하여,

선형 시간에 정렬하는 효율적인 방식

### 카운팅 정렬 제한 사항

1. 정수나 정수로 표현할 수 있는 자료에 대해서만 적용 가능
2. 카운트들을 위한 충분한 공간을 할당하려면 집합 내의 가장 큰 정수를 알아야 함.

### 시간 복잡도

O(n+k) : n 은 리스트 길이. k는 정수의 최댓값

[1단계] DATA에서 각 항목들의 발생 횟수를 세고, 카운트 배열에 저장한다.

`COUNTS[i] = i의 발생 횟수`

[2단계] 정렬된 집합에서 각 항목의 앞에 위치할 항목의 개수를 반영하기 위해 원소를 조정한다.

`COUNTS[i] = COUNTS[i-1] + COUNTS[i]`

즉, 결국 원소의 개수 총합이 됨

[3단계] DATA의 마지막 원소의 발생횟수를 감소키시키고 TEMP에 삽입

```python
DATA = [0, 4, 1, 3, 1, 2, 4, 1]

def counting_sort(DATA, TEMP, K):

	COUNTS = [0] * (k+1)

	for i in range (len(DATA)) # DATA[i] 발생횟수 기록
		COUNTS[DATA[i]] += 1
		
	for i in range (1, k+1) : # COUNTS 값 조정 (누적)
		COUNTS[i] += COUNTS[i-1]
			
	for i in range (len(DATA)-1, -1, -1) : # 3단계
		COUNTS[DATA[i]] -= 1
		TEMP[COUNTS[DATA[i]]] = DATA[i]	 
```

# 6. 완전 검색(Exaustive Search)

모든 경우의 수를 나열해보고 확인하는 기법

Brute-force 혹은 generate-and-test 기법이라고도 불림.

### 순열 (Permutation)

단순하게 순열을 생성하는 방법

```python
for i1 in range(1, 4):
	for i2 in range(1, 4):
		if i2 != i1 :
			for i3 in range(1, 4):
				if i3 != i1 and i3 != i2 :
					print(i1, i2, i3)
```

# 7. 탐욕 알고리즘

여러 경우 중 하나를 결정해야 할 때마다 그 순간에 최적이라고 생각되는 것을 선택해 나가는 방식으로 진행

### 탐욕 알고리즘 과정

1. 해 선택 : 현재 상태에서 부분 문제의 최적 해를 구한 뒤, 부분 해 집합에 추가
2. 실행 가능성 검사
3. 해 검사

### Baby - gin 접근

```python
num = 456789 # Baby gin 확인할 6자리 수
c = [0] * 12 # 6자리 수로부터 각 자리 수를 추출하여 개수를 누적할 리스트

for i in range(6) :
	c[num % 10] += 1
	num //= 10
```

왜 12자리를 만드는가?

더미공간을 위해…? 이해 못해도 그냥 넘어가자… 그럼갑다 해야함..

for문은 count 방을 만드는 작업임!!

0 1  2 3 4 5 6 7 8 9

0 0 0 0 1  1  1  1  1  1

```python
i = 0
tri = run = 0
while i < 10 :
	if c[i] >= 3 : #triplete 조사 후 데이터 삭제
		c[i] -= 3
		tri += 1
		continue;
		
	if c[i] >= 1 and c[i+1] >= 1 and c[i+2] >= 1 : # run 조사 후 데이터 삭제
		c[i] -= 1
		c[i+1] -= 1
		c[i+2] -= 1
		run += 1
		continue
	i += 1
	
if run + tri == 2 : print("Baby Gin")
else : print("Lose")
	
```

아하!

0~9까지 10칸을 만들고 더미공간

자리수를 더 써서 메모리를 더 쓰는 대신 연산을 줄이는 방법임.

i 가 9일 때 11까지 비교하기 위함.
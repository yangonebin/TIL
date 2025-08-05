T = int(input())
for test_case in range(1, T+1):
	N = int(input())
	ai = list(map(int, input().split()))
    
	diff = max(ai) - min(ai)
	print(f'#{test_case} {diff}')
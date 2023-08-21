import sys
input = sys.stdin.readline

while True:
    n = int(input())
    if n == 0:
        break
    t = 0
    i = 0
    arr = input().rstrip().replace(' ','').upper() # 공백 제거하고 대문자로 바꿈
    result = [''] * len(arr)
    for a in arr:
        try : # 인덱스 넘어가는 경우
            result[t+i*n] = a # 결과물 넘어갈때 n씩 넘어감
            i += 1
        except:
            t += 1 # t는 0 ~ n-1 번째 위치를 뜻함
            result[t] = a
            i = 1
    print(*result, sep='')
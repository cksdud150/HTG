def recursion(i,ll,m,j,result): # i는 알파벳 위치, ll은 암호가 몇자리인지, m은 모음 개수, j는 자음 개수, result는 출력용
    # if i >= c:
    #     return
    if ll == l:
        if m >= 1 and j >= 2:
            print(result)
    else:
        for ii in range(i+1,c):
            if alpha[ii] in ('a','e','i','o','u'):
                recursion(ii,ll+1,m+1,j,result+alpha[ii])
            else:
                recursion(ii,ll+1,m,j+1,result+alpha[ii])

l, c = map(int,input().split())
alpha = input().split()
alpha.sort()
for i in range(c):
    if alpha[i] in ('a','e','i','o','u'):
        recursion(i,1,1,0,alpha[i])
    else:
        recursion(i,1,0,1,alpha[i])
    
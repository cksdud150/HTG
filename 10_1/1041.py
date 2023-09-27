n = int(input())
dice = list(map(int,input().split()))
small1 = min(dice)
small2 = min([dice[i]+dice[j] for i,j in [[0,1],[0,2],[0,3],[0,4],[1,2],[1,3],[1,5],[2,4],[2,5],[3,4],[3,5],[4,5]]])
small3 = min([dice[i]+dice[j]+dice[k] for i,j,k in [[0,1,2],[0,1,3],[0,2,4],[0,3,4],[1,2,5],[1,3,5],[2,4,5],[3,4,5]]])
if n == 1:
    result = sum(dice) - max(dice)
else:
    result = ((n-2)*(n-2) + (n-2)*(n-1)*4)*small1 + ((n-1)*4 + (n-2)*4)*small2 + 4*small3
print(result)
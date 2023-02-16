qpos = str(input("Enter the position sequence of queens : "))


arr=[]
rows, cols=8,8
for i in range(rows):
    col = []
    for j in range(cols):
        col.append(0)
    arr.append(col)

# 61475381
i =0
for pos in qpos:
    #arr[5][0]='Q'
    # print(int(pos))
    arr[int(pos)-1][i]='Q'
    i=i+1;

arr.reverse()
for darr in arr :
    print(darr)


for index,row in arr:
    print(index)
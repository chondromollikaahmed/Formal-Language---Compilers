qpos = str(input("Enter the position sequence of queens : "))

posl=[]

for pos in qpos:
    posl.append(int(pos))

print(posl)


def countHorizontal(point, pos):
 global h3
 for i in range(point + 1, len(pos)):
  #  print(pos[i],pos[point])
   if pos[i] == pos[point]:
     h3 += 1
     print(h3)
def countDiagonalUp(point, pos):
 global h3
 for i in range(point + 1, len(pos)):
#    print(pos[i],pos[point] , i , point)
   if pos[i] == pos[point] + i - point:
     h3 += 1
     print(h3)
def countDiagonalDown(point, pos):
 global h3
 for i in range(point + 1, len(pos)):
   if pos[i] == pos[point] - i + point:
     h3 += 1
     print(h3)


h3=0

for i in range(len(posl)):
   print(i,posl)
   countHorizontal(i, posl)


for i in range(len(posl)):
   countDiagonalUp(i, posl)


for i in range(len(posl)):
   countDiagonalDown(i, posl)




print('Heuristic value for 8-Queen: ', h3)


# 61574381
A = 1
B= 7
for i in range(5):
  for j in range(3):
    print('I=%d J=%d' %(A, B))
    B -= 1
  A += 2
  B += 5

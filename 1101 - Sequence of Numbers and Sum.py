while(True):
  Lista = []
  a, b = map(int, input().split())
  if(a <= 0) or (b <= 0):
    break
  else:
    if(a > b):
      a, b = b, a
    for i in range(a, b + 1):
      Lista.append(i)
    Soma = 'Sum=%d' %sum(Lista)
    Lista.append(Soma)
    print(' '.join(map(str, Lista)))

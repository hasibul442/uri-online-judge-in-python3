N = int(input())
for c in range(0, N):
  num = int(input())
  if num % 2 == 0 and num > 0:
    print('EVEN POSITIVE')
  elif num % 2 == 0 and num < 0:
    print('EVEN NEGATIVE')
  elif num % 2 == 1 and num > 0:
    print('ODD POSITIVE')
  elif num % 2 == 1 and num < 0:
    print('ODD NEGATIVE')
  else:
    print('NULL')

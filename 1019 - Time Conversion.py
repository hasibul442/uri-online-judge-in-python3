second = int(input())

min = int(second/60)
second -=min*60
hour = int(min/60)
min -=hour*60

print(repr(hour)+":"+repr(min)+":"+repr(second))

a, b = input().split()
ar = input().split()
x = set(input().split())
y = set(input().split())
print(sum([(i in x) - (i in y) for i in ar]))

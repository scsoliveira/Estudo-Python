y = int(input(""))
result = [y]
for b in range(y):
  x = int(input(""))
  f1 = int(input(""))
  f2 = int(input(""))
  fr = abs(f1 - f2)
  a = fr/x
  result.append(a)
  
for c in range(len(result)):
  print(result[c])

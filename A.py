soma = ""
produto = "."
x = int(input(""))
numero = []
for i in range(x):
  p = int(input(""))
  k = int(input(""))
  for two in range(10):
    if(soma == produto):
      numero.append(soma)
    for one in range(10):
      if(one*two==k):
        produto = str(one) + str(two)
      if(one+two==p):
        soma = str(one) + str(two)
for a in range(len(numero)):
  print(numero[a])
      
        
        
    
      



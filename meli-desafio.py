# Meli Desafio
# função recebe um numero de entrada, e deve formar um numero de 4 algarimos
# cada algarismo é limitado pelo valor de entrada e deve printar o numero de 4 algarimos
# que a soma seja igual a 21, se não existir nenhum numero cujo de esse valor printar nulo 

n = input()
max = int(n+n+n+n)
count = 1111
l = int(n)

if(max < 3666):
  print("null")

while count < max:
  number = list(str(count))
  if(int(number[3])+int(number[2])+int(number[1])+int(number[0]) == 21):
    print(count)
  if(int(number[3]) < int(l)):
    count += 1
  elif(int(number[3]) == l and int(number[2]) < l):
    count += (10-l)
  elif(int(number[2]) == l and int(number[1]) < l ):
    count += 100-(10*l)
  elif(int(number[1]) == l and int(number[0]) < l ):
    count += 1000-(100*l)
  
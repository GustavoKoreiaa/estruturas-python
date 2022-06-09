print("Testando o comando IF (Digite um número menor de 18:)")
valor = int(input("Qual sua idade? "))
if valor < 18: 
  print("Você ainda não dirigir! :")

#----------#----------#
print("\n")
print("Testando o comando IF.. ELSE (Se..senão)")
valor = int(input("Qual sua idade? "))
if valor < 18: 
  print("Você ainda não pode dirigir!")
else:
  print("Você pode dirigir!")
  #----------#----------#
print("\n")
print("Testanto o comando IF..ELIF..ELSE (Se..Senão..Senão se)")
valor = int(input("Que coisa fofa!"))
if valor < 6:
  print("Você ainda não pode dirigir!")
elif valor < 18:
  print("Você ainda não pode dirigir!")
elif valor > 60:
  print("Você está na melhor idade!")
else: 
  print("Você pode dirigir")
  

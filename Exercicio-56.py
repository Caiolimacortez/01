from time import sleep
import os

Mulheres: int = 0
IdadeTotalMedia = 0
Homem = 0
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
print('-='* 20)
Nome1 = str(input('Digite o Seu Nome: '))

def AntiErro1():
  Idade1 = input('Digite a Sua Idade: ')

  try:
    return int(Idade1)
  except Exception as err:
    print('Digite Somente Numeros Inteiros! Ex = [1] [2]... ')
  return AntiErro1()

Idade1 = (AntiErro1())

#print("Idade1 [{}]".format(Idade1))

while True:
  Sexo1 = str(input('Digite o Seu Sexo [M/F]: '))

  Sexo1 = Sexo1.upper()
  Sexo1 = Sexo1.strip()

  if Sexo1 != ('M') and  Sexo1 != ('F'):
    print('\nOpção Inválida Voçê Digitou = {}'.format(Sexo1))
    print('Digite - M - Para Masculino é - F - Para Feminino')
    sleep(0.3)
    #os.system('cls' if os.name == 'nt' else 'clear')
  else:
    break

if Sexo1 == ('M'):
  Maisvelho = Idade1
  Homem = Nome1

elif Idade1 <= 20:
  Mulheres += 1

print('-='* 20)
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
Nome2 = str(input('Digite o Seu Nome: '))

def AntiErro2():
  Idade2 = input('Digite a Sua Idade: ')

  try:
    return int(Idade2)
  except Exception as err:
    print('Digite Somente Numeros Inteiros! Ex = [1] [2]... ')
  return AntiErro2()

Idade2 = (AntiErro2())

while True:
  Sexo2 = str(input('Digite o Seu Sexo [M/F]: '))

  Sexo2 = Sexo2.upper()
  Sexo2 = Sexo2.strip()

  if Sexo2 != ('M') and  Sexo2 != ('F'):
    print('\nOpção Inválida Voçê Digitou = {}'.format(Sexo2))
    print('Digite - M - Para Masculino é - F - Para Feminino')
    sleep(0.3)
    #os.system('cls' if os.name == 'nt' else 'clear')

  else:
    break

if Sexo2 == ('M'):
  if Idade2 >= Idade1:
    Maisvelho = Idade1
    Homem = Nome2

elif Idade2 <= 20:
  Mulheres += 1

print('-='* 20)
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
Nome3 = str(input('Digite o Seu Nome: '))

def AntiErro3():
  Idade3 = input('Digite a Sua Idade: ')

  try:
    return int(Idade3)
  except Exception as err:
    print('Digite Somente Numeros Inteiros! Ex = [1] [2]... ')
  return AntiErro3()

Idade3 = (AntiErro3())

while True:
  Sexo3 = str(input('Digite o Seu Sexo [M/F]: '))

  Sexo3 = Sexo1.upper()
  Sexo3 = Sexo1.strip()

  if Sexo3 != ('M') and  Sexo3 != ('F'):
      print('\nOpção Inválida Voçê Digitou = {}'.format(Sexo3))
      print('Digite - M - Para Masculino é - F - Para Feminino')
      sleep(0.3)
      #os.system('cls' if os.name == 'nt' else 'clear')

  else:
    break

if Sexo3 == ('M'):
  Maisvelho = Idade3
  Homem = Nome3

elif Idade3 <= 20:
  Mulheres += 1

print('-='* 20)
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
Nome4 = str(input('Digite o Seu Nome: '))

def AntiErro4():
  Idade4 = input('Digite a Sua Idade: ')

  try:
    return int(Idade4)
  except Exception as err:
    print('Digite Somente Numeros Inteiros! Ex = [1] [2]... ')
  return AntiErro4()

Idade4 = (AntiErro4())

while True:
  Sexo4 = str(input('Digite o Seu Sexo [M/F]: '))

  Sexo4 = Sexo1.upper()
  Sexo4 = Sexo1.strip()

  if Sexo4 != ('M') and  Sexo4 != ('F'):
      print('\nOpção Inválida Voçê Digitou = {}'.format(Sexo4))
      print('Digite - M - Para Masculino é - F - Para Feminino')
      sleep(0.3)
      #os.system('cls' if os.name == 'nt' else 'clear')

  else:
    break

if Sexo4 == ('M') and Maisvelho <= Idade4:
  Maisvelho = Idade4
  Homem = Nome4

elif Idade4 <= 20:
  Mulheres += 1

#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
IdadeTotalMedia = (Idade1 + Idade2 + Idade3 + Idade4) /4

if Mulheres != 0:
  print('\nHá {} Mulheres Com 20 Anos De Idade.'.format(Mulheres))
print('\nA Idade Media do Grupo é de {:.0f} Anos.'.format(IdadeTotalMedia))
if Homem != 0:
  print('\nO Homem Mais Velho é {} Com {} Anos De Idade.'.format(Homem,Maisvelho))
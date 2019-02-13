from time import sleep
import os

Mulheres = 0
Idade_1 = 0
Idade_2 = 0
Idade_3 = 0
Idade_4 = 0


print('-='* 20)
Nome1 = str(input('Digite o Seu Nome: '))


Idade1 = int(input('Digite a Sua Idade: '))

while True:
  Sexo1 = str(input('Digite o Seu Sexo [M/F]: '))

  Sexo1 = Sexo1.upper()
  Sexo1 = Sexo1.strip()

  if Sexo1 != ('M') and  Sexo1 != ('F'):
    print('\nOpção Inválida Voçê Digitou = {}'.format(Sexo1))
    print('Digite - M - Para Masculino é - F - Para Feminino')
    sleep(0.3)
    os.system('cls' if os.name == 'nt' else 'clear')
  else:
    break

print('-='* 20)

Nome2 = str(input('Digite o Seu Nome: '))
Idade2 = int(input('Digite a Sua Idade: '))
while True:
  Sexo2 = str(input('Digite o Seu Sexo [M/F]: '))

  Sexo2 = Sexo2.upper()
  Sexo2 = Sexo2.strip()

  if Sexo2 != ('M') and  Sexo2 != ('F'):
    print('\nOpção Inválida Voçê Digitou = {}'.format(Sexo1))
    print('Digite - M - Para Masculino é - F - Para Feminino')
    sleep(0.3)
    os.system('cls' if os.name == 'nt' else 'clear')

  else:
    break

print('-='* 20)
Nome3 = str(input('Digite o Seu Nome: '))
Idade3 = int(input('Digite a Sua Idade: '))
while True:
  Sexo3 = str(input('Digite o Seu Sexo [M/F]: '))

  Sexo3 = Sexo1.upper()
  Sexo3 = Sexo1.strip()

  if Sexo3 != ('M') and  Sexo3 != ('F'):
      print('\nOpção Inválida Voçê Digitou = {}'.format(Sexo1))
      print('Digite - M - Para Masculino é - F - Para Feminino')
      sleep(0.3)
      os.system('cls' if os.name == 'nt' else 'clear')

  else:
    break

print('-='* 20)
Nome4 = str(input('Digite o Seu Nome: '))
Idade4 = int(input('Digite a Sua Idade: '))
while True:
  Sexo4 = str(input('Digite o Seu Sexo [M/F]: '))

  Sexo4 = Sexo1.upper()
  Sexo4 = Sexo1.strip()

  if Sexo4 != ('M') and  Sexo4 != ('F'):
      print('\nOpção Inválida Voçê Digitou = {}'.format(Sexo1))
      print('Digite - M - Para Masculino é - F - Para Feminino')
      sleep(0.3)
      os.system('cls' if os.name == 'nt' else 'clear')

  else:
    break

#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
if  Sexo1 == ('F'):
  Idade_1 = 1
  if Idade1 <= 20:
    Mulheres = +1

if Sexo2 == ('F'):
  Idade_2 = 1
  if Idade2 <= 20:
    Mulheres = +1

if Sexo3 == ('F'):
  Idade_3 = 1
  if Idade3 <= 20:
    Mulheres +1

if Sexo4 == ('F'):
  Idade_4 = 1
  if Idade4 <= 20:
    Mulheres +1

#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

Idade = (Idade1 + Idade2 + Idade3 + Idade4) /4

if  Idade_1 == 1:
  if Idade2 > Idade3 and Idade4:
    Homem = Nome2
    IdadeH = Idade2

if  Idade_2 == 1:
  if Idade1 > Idade3 and Idade4:
    Homem = Nome1
    IdadeH = Idade1

if  Idade_3 == 1:
  if Idade4 > Idade2 and Idade1:
    Homem = Nome4
    IdadeH = Idade4

if  Idade_4 == 1:
  if Idade3 > Idade1 and Idade2:
    Homem = Nome3
    IdadeH = Idade3

else:
  if Sexo1 == ('M'):
    if Idade1 > Idade2 and Idade3 and Idade4:
      Homem = Nome1
      IdadeH = Idade1

  if Sexo2 == ('M'):
    if Idade2 > Idade2 and Idade3 and Idade4:
      Homem = Nome2
      IdadeH = Idade2

  if Sexo3 == ('M'):
    if Idade3 > Idade1 and Idade2 and Idade4:
      Homem = Nome3
      IdadeH = Idade3

  if Sexo4 == ('M'):
    if Idade4 > Idade1 and Idade2 and Idade3:
      Homem = Nome4
      IdadeH = Idade4

#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

print('\nHá {} Com 20 Anos De Idade'.format(Mulheres))
print('\nA Idade Media do Grupo é de {:.0f} Anos'.format(Idade))
print('\nO nome do Homen Mais velho do grupo é {} com {] Anos'.format(Homem, IdadeH))
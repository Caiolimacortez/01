from time import sleep
import sys
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

  if Sexo1 != ('M') and Sexo1 != ('F'):
    print('\nOpção Inválida Você Digitou = {}'.format(Sexo1))
    print('Digite [M] Para Masculino ou [F] Para Feminino')

  else:
    break


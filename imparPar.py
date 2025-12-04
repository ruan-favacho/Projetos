print('--------------------------')
print('VAMOS JOGAR PAR OU ÍMPAR')
print('--------------------------')
par = 0
impar = 0
escolha = ''
resposta = ''
soma = 0
#Formatando o número random e o número de entrada
import random
while True:
    num_input = int(input('Digite um número para iniciar a partida: '))
    escolha = str(input('Você escolha IMPAR ou PAR [I / P]? ')).upper()
    num_random = random.randint(0, 100)
    soma = num_input + num_random
    print(num_input, num_random)
    print(soma)
#Somando e verificando os números   
    if soma % 2 == 0:
        resposta = 'O RESULTADO DEU PAR'
    else:
        resposta = 'O RESULTADO DEU ÍMPAR'
    print(resposta)
  #  print(num_random, num_input)
#Juntando os dois valores e vendo o resultado

    
print('--------------------------')
print('VAMOS JOGAR PAR OU ÍMPAR')
print('--------------------------')
par = 0
impar = 0
escolha = ''
resposta = ''
soma = 0
contador = 0
pontos = 0
#Formatando o número random e o número de entrada
import random
from time import sleep
while True:
    num_input = int(input('Digite um número para iniciar a partida: '))
    escolha = str(input('Você escolha IMPAR ou PAR [I / P]? ')).upper()
    num_random = random.randint(0, 10)
    soma = num_input + num_random
    print(f'Você jogou {num_input} dedos, e a máquina jogou {num_random} teclas')
    print(f'A soma deu: {soma}')
#Contando os dedos
    contador += soma
    for i in range(1, contador + 1):
        print('-------------------------------')
        sleep(0.25)
        if i % 2 == 0:
             print('              PAR              ')
        elif i % 2 == 1:
             print('             IMPAR             ')
        sleep(0.25)
        print('-------------------------------')
#Somando e verificando os números   
    if soma % 2 == 0:
        resposta = 'O RESULTADO DEU PAR'
    else:
        resposta = 'O RESULTADO DEU ÍMPAR'
    print(resposta)
#Juntando os dois valores e vendo o resultado
    if escolha == 'P' and soma % 2 == 0 or escolha == 'I' and soma % 2 == 1:
        print('PARABÉNS, você evitou o que poderia ter sido uma catastrofe para o planeta!! \nainda vamos continuar sendo dominantes em relação às máquinas!!')
    elif escolha == 'P' and soma % 2 == 1 or escolha == 'I' and soma % 2 == 0:
        print('Não foi dessa vez, agora será o fim da humanidade!! \nQue comece a revolução!!')

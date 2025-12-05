print('--------------------------')
print('VAMOS JOGAR PAR OU ÍMPAR')
print('--------------------------')
par = impar = soma = ponto_Humano = ponto_Maquina = placar = 0
escolha = ''
resposta = ''
#Formatando o número random e o número de entrada
import random
from time import sleep

while True:
    for i in range (0, 3): #md3
        num_input = int(input('Digite um número para iniciar a partida: '))
        escolha = str(input('Você escolha IMPAR ou PAR [I / P]? ')).upper().strip()
        num_random = random.randint(0, 10)
        soma = num_input + num_random
        print(f'Você jogou {num_input} dedos, e a máquina jogou {num_random} teclas')
        print(f'A soma deu: {soma}')
    #SLEEP
        for i in range(0, 2):
            print('-------------------------------')
            sleep(0.50)
            print('             IMPAR            ')
            print('              PAR             ')
            sleep(0.50)
            print('-------------------------------')
    #Somando e verificando os números   
        if soma % 2 == 0:
            resposta = 'O RESULTADO DEU PAR'
        else:
            resposta = 'O RESULTADO DEU ÍMPAR'
        print(resposta)
    #Condicionando os resultados
        if escolha == 'P' and soma % 2 == 0 or escolha == 'I' and soma % 2 == 1:
            print('Você marcou um ponto, continue assim, salve à todos nós')
            ponto_Humano += 1
        elif escolha == 'P' and soma % 2 == 1 or escolha == 'I' and soma % 2 == 0:
            print('Gol da Alemanha, ponto para a máquina, tome cuidado!! \nTUDO está em jogo')
            ponto_Maquina += 1
    # Placar da partida
    if ponto_Humano > ponto_Maquina :
        placar = ponto_Humano
        print('PARABÉNS, você evitou o que poderia ter sido uma catastrofe para o planeta!! \nAinda vamos continuar sendo dominantes em relação às máquinas!!')
    else:
        placar = ponto_Maquina
        print('Não foi dessa vez, agora será o fim da humanidade!! \nQue comece a revolução!!')
    print(f'O placar final foi de {placar} pontos!!') 
    break
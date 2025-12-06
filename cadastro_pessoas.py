print('-----------------------')
print('  CADASTRO DE PESSOAS  ')
print('-----------------------')
maioridade = 0
homens = 0
mulheres_menores20 = 0
while True:
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: [M/F] ')).strip().upper()
    continuar = str(input('Quer continuar? [S/N] ')).strip().upper()
    while continuar not in 'N':
        if idade > 18:
            maioridade += 1
        if sexo == 'M':
            homens += 1
        if sexo == 'F' and idade < 20:
            mulheres_menores20 += 1
        idade = int(input('Idade: '))
        sexo = str(input('Sexo: [M/F] '))
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()
        
        print(f'Cadastros de maiores de idade: {maioridade}')
        print(f'Cadastro de homens: {homens}')
        print(f'Cadastro de mulheres com menos de 20 anos: {mulheres_menores20}')
    break     


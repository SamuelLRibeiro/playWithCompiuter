from time import sleep
from random import randint

print('COMPIUTER diz: "Olá, me chamo COMPIUTER e fui criado pelo Semlua"')
sleep(1)
nome = str(input('COMPIUTER diz: "Como você se chama?" '))
print(f'COMPIUTER diz: "Muito prazer, {nome}! Você gostaria de jogar um jogo? "')
decisao = str(input('Digite a sua resposta: ')).capitalize()
if decisao[0] == 'S':
    sleep(0.8)
    print('COMPIUTER diz: "LEGAL! Diga um número de 0 a 10 e eu direi outro. Se você digitar o mesmo que eu, você ganha!"')
    compiuterNumber = randint(0,10)
    userNumber = int(input("Digite seu número contra o COMPIUTER: "))
    print(f'COMPIUTER diz: "Eu pensei no número {compiuterNumber}"')
    print(f'COMPIUTER diz: "Você digitou o número {userNumber}"')
    if userNumber == compiuterNumber:
        print('COMPIUTER diz: "Você ganhou!"')
    else:
        print('COMPIUTER diz: "Você perdeu!"')
else:
    print('COMPIUTER diz: "Tudo bem, eu não posso obrigar ninguém a jogar... :(" ')

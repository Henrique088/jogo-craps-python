from random import randint


def regras():
    print("---------Bem vindo ao Craps------\n")
    print("Craps é um jogo de dois dados com o objetivo de tirar um somátorio especifico"
          "na jogada inicial ou em caso de outros valores você pode continuar e ter a chance de vencer\n")
    print("Regras:", end ="")
    print("1 - Seu objetivo inicial é tirar um 7 ou 11")
    print("2 - Em caso de um 2, 3 ou 12 você autômaticamente perde")
    print("3 - Em caso de um 4, 5, 6, 8, 9 ou 10, você continua jogando até tirar o mesmo número novamente")
    print("4 - Se tirar um 7 antes de tirar o mesmo número você perde")


class jogo:
    def __init__(self, nome):
        self._nome = nome.title()
        self.vitoria = 0
        self.derrota = 0


    def craps(self, rolagem_1, rolagem_2):

        if(rolagem_1 + rolagem_2 in (7,11)):
            print("soma {}".format(rolagem_1+rolagem_2))
            print("Parabéns você venceu!!!!")

            return 1

        elif (rolagem_1 + rolagem_2 in(2,3,12)):
            print("Que pena você perdeu na primeira rodada :(")

            return 0

        else :
            print("Continue Jogando até tirar o mesmo número para vencer")

            return 2

    def dados(self):
        return randint(1,6)

    @property
    def nome_jogador(self):
        return self._nome

    @property
    def soma_vitoria(self):
        self.vitoria += 1

    @property
    def soma_derrota(self):
        self.derrota += 1

    def placar(self):
        return print("Vitória: {} \nDerrota: {}".format(self.vitoria, self.derrota))



if(__name__ == "__main__"):
    regras()
    primeira_jogada = 0
    print("Escreva seu nome: ")
    nome = input()

    comeca = jogo(nome)


    while(True):

        resultado_1 = comeca.dados()
        print("Dado 1: {}".format(resultado_1))

        resultado_2 = comeca.dados()
        print("Dado 2: {}".format(resultado_2))

        soma = resultado_1+resultado_2

        print("Soma: {}".format(soma))
        if(primeira_jogada==0):

            p = comeca.craps(resultado_1, resultado_2)

            primeira_jogada = 1

        if (p == 1 or p == 0):

            if(p ==1):
                comeca.soma_vitoria
            else:
                comeca.soma_derrota

            print(comeca.placar())
            print("Deseja continuar jogando? (y) yes, (n) no: ")
            desejo = input().lower()

        else:
            while(True):

                resultado_1 = comeca.dados()
                print("Dado 1: {}".format(resultado_1))

                resultado_2 = comeca.dados()
                print("Dado 2: {}".format(resultado_2))

                print("Soma: {}".format(resultado_1 + resultado_2))

                if(resultado_1 + resultado_2 == soma ):
                    print("Parabéns você venceu!!!")
                    print(soma)
                    print(resultado_1+resultado_2)
                    comeca.soma_vitoria
                    comeca.placar()

                    # print("Deseja continuar jogando? (y) yes, (n) no: ")
                    # desejo = input().lower()
                    break

                elif(resultado_1+resultado_2==7):
                    print("Que pena você perdeu! ")
                    comeca.soma_derrota
                    comeca.placar()

                    # print("Deseja continuar jogando? (y) yes, (n) no: ")
                    # desejo = input().lower()
                    break

                else:
                    pass

            print("Deseja continuar jogando? (y) yes, (n) no: ")
            desejo = input().lower()

        if (desejo == 'y'):
            primeira_jogada =0

        else:
            print("Fim do jogo! Até a próxima,{}...".format(comeca.nome_jogador))
            break




























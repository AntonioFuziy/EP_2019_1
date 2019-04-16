# EP 2019-1: Escape Insper
#
# Alunos: 
# - aluno A: Fulano da Silva, fulanos@insper.edu.br
# - aluno B: Sicrano de Almeida, sicranoa1@insper.edu.br

def carregar_cenarios():
    cenarios = {
        "saguao": {
            "titulo": "Saguao do perigo",
            "descricao": "Voce esta no saguao de entrada do insper",
            "opcoes": {
                "sala do professor": "Tomar o elevador para a sala do professor",
                "biblioteca": "Ir para a biblioteca",
                "fab lab" : "Ir para o fab lab de escada"
            }
        },
        "biblioteca": {
            "titulo": "Andar Sagrado",
            "descricao": "Voce chegou na biblioteca. Shhhhhh!!!",
            "opcoes": {
                "saguao": "Tomar o elevador para o saguao de entrada",
                "armario": "Você tem a chance de ganhar o jogo"
            }
        },
        "fab lab": {
            "titulo": "O monstro te aguarda",
            "descricao": "Você chegou ao fab lab"
                         "O professor revelou que é um monstro disfarçado "
                         "e devorou sua alma.",
            "opcoes": {
                    "saguao": "Tomar o elevador para o saguao de entrada",
            }
        },
        "armario": {
            "titulo": " Voce chegou ao corredor dos armários",
            "descricao": "",
            "opcoes": {
                "biblioteca": "Voltar para a biblioteca",
                "win":"você ganhou o jogo"
            }
        },
        "sala do professor": {
            "titulo": "Você chegou na sala do Rei Toshi. Ajoelhe-se",
            "descricao": "Você precisa provar seu valor e falar a senha passada durante o jogo"
                         "Só assim você mudará a data de entrega do EP",
            "opcoes": {
                "saguao": "Ir para o saguao de entrada",
                "biblioteca": "Ir para a biblioteca",
                "fab lab": "Falar com o professor"
            }
        }
    }
    nome_cenario_atual = "saguao"
    return cenarios, nome_cenario_atual


def main():
    print("Na hora do sufoco!")
    print("------------------")
    print()
    print("Parecia uma boa idéia: vou só jogar um pouquinho/assistir Netflix/"
        "embaçar em geral. Amanhã eu começo o EP. Mas isso não deu certo...")
    print()
    print("É o dia de entregar o EP e você está muuuuito atrasado! Você está "
        "na entrada do Insper, e quer procurar o professor para pedir um "
        "adiamento do EP (boa sorte...)")
    print()

    cenarios, nome_cenario_atual = carregar_cenarios()

    game_over = False
    while not game_over:
        
        cenario_atual = cenarios[nome_cenario_atual]
        print (cenario_atual['titulo'])
        print('-'*len(cenario_atual['titulo']))
        print (cenario_atual['descricao'])
        print ()

        opcoes = cenario_atual['opcoes']
        if len(opcoes) == 0:
            print("Acabaram-se suas opções! Mwo mwo mwooooo...")
            game_over = True
        else:
            print ('As opções disponiveis são: ')
            print ()
            for k,v in opcoes.items():
                print ('-{0}: {1}'.format(k,v))
            print ()
            escolha =input("Digite a sua opção: ")

            if escolha in opcoes:
                nome_cenario_atual = escolha
            else:
                print("Sua indecisão foi sua ruína!")
                game_over = True

    print("Você morreu!")


# Programa principal.
if __name__ == "__main__":
    main()

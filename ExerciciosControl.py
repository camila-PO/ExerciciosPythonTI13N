import this
import ExerciciosModel
this.opcao = -1



def Menu():
    print('Menu\n\n'          +
          '\n1. Exercício 01' +
          '\n2. Exercício 02' +
          '\n3. Exercício 03' +
          '\n4. Exercício 04' +
          '\n5. Exercício 05' +
          '\n6. Exercício 06' +
          '\n7. Exercício 07' +
          '\n8. Exercício 08' +
          '\n9. Exercício 09' +
          '\n6. Exercício 10' +
          '\n7. Exercício 11' +
          '\n6. Exercício 12' +
          '\n7. Exercício 13' +
          '\n6. Exercício 14' +
          '\n7. Exercício 15' +
          '\n6. Exercício 16' +
          '\n7. Exercício 17' +
          '\n6. Exercício 18' +
          '\n7. Exercício 19' +
          '\n6. Exercício 20' +
          '\n0. Sair'         +
          '\nEscolha uma das opções acima: ')
    this.opcao = int(input())

def Executar():
    while(this.opcao != 0):
        Menu()
        if this.opcao == 0:
            print('Obrigado!')
        elif this.opcao == 1:
            print(ExerciciosModel.exercicio01())
        elif this.opcao == 2:
            print('Informe um número')
            num1 = int(input())
            print(ExerciciosModel.exercicio02(num1))
        elif this.opcao == 3:
            while this.bas <= 0:
                print('Informe a base do retângulo: ')
                this.bas = float(input())
                if this.bas <= 0:
                    print('Informe uma base com valor positivo')

            while this.altura <= 0:
                print('Informe a altura do retângulo: ')
                this.altura = float(input())
                if this.altura <= 0:
                    print('Informe uma base com valor positivo')

            print(ExerciciosModel.exercicio03(this.bas,this.altura))
        elif this.opcao == 4:
            print(ExerciciosModel.exercicio04())
        elif this.opcao == 5:
            print(ExerciciosModel.exercicio05())
        elif this.opcao == 6:
            print(ExerciciosModel.exercicio06())
        elif this.opcao == 7:
            print(ExerciciosModel.exercicio07())
        elif this.opcao == 8:
            print(ExerciciosModel.exercicio08())
        elif this.opcao == 9:
            print('Por favor, informe a quantidade de maçãs compradas:')
            maca = int(input())
            if maca <= 11:
                valor = 1.30
            else:
                valor = 1
            print('valor total: R$ {}'.format(maca * valor))
            msgs = 'obrigado'
            return msgs

        #elif this.opcao == 10:

        #elif this.opcao == 11:


        #elif this.opcao == 12:

        elif this.opcao == 13:
            print(ExerciciosModel.exercicio13())
        elif this.opcao == 14:
            print(ExerciciosModel.exercicio14())
        elif this.opcao == 15:
            print(ExerciciosModel.exercicio15())
        elif this.opcao == 16:
            print(ExerciciosModel.exercicio16())
        elif this.opcao == 17:
            print(ExerciciosModel.exercicio17())
        elif this.opcao == 18:
            print(ExerciciosModel.exercicio18())
        elif this.opcao == 19:
            print(ExerciciosModel.exercicio19())
        elif this.opcao == 20:
            print(ExerciciosModel.exercicio20())
        else:
            print('Código digitado não é válido!')
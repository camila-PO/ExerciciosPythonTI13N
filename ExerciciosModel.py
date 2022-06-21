import ExerciciosControl
import this
this.quant = 0

def Exercicio01():
    A = 10
    B = 20
    msg = 'antes da troca A = {}, B = {}'.format(A,B)
    aux = A
    A = B
    B = aux
    msg = msg +'\nDepois da troca: A= {}, B = {}'.format(A,B)
    return msg

def exercicio02(num1):
    return 'O antecessor é {}'.format(num1-1)

def exercicio03(bas, altura):
    return bas * altura

def exercicio04():
       ano = int(input('informe os anos'))
       mes = int(input('informe os mêses'))
       dia = int(input('informce os dias'))
       idade: int = ano * 365 + mes * 30 + dia
       return idade

def exercicio05():
       et = int(input('informe o número total de eleitores'))
       vb = int(input('informe o número de votos brancos'))
       vn = int(input('informe o número de votos nulos'))
       vl = int(input('informe o número de votos válidos'))

       pvb = float(vb * 100) / et
       pvn = float(vn * 100) / et
       pvl = float(vl * 100) / et

       result = "A porcentagem de votos brancos é: {}".format(pvb), "A porcentagem de votos nulos é: {}".format(
           pvn), "A porcentagem de votos válidos é: {}".format(pvl)
       return result

def exercicio06():
       SalarioMensal = float(input('informe o seu salário mensal:'))
       reajuste = float(input('informe o Percentual de reajuste:'))
       newSalario = (SalarioMensal * reajuste / 100) + SalarioMensal
       return newSalario

def exercicio07():
       custoFabrica = float(input('informe o custo de fábrica:'))
       percentualD = custoFabrica * 28 / 100 + custoFabrica
       impostos = custoFabrica * 45 / 100 + custoFabrica
       CustoFinal = "O custo final do seu carro é de: {} R$".format(percentualD + impostos)

       return CustoFinal

def exercicio08():
       nota1 = float(input('informe a 1ª nota do aluno:'))
       nota2 = float(input('informe a 2ª nota do aluno:'))
       nota3 = float(input('informe a 3ª nota do aluno'))
       media = "Sua média Final é: {}".format(nota1 + nota2 + nota3 / 3)

       return media
#def exercio09():

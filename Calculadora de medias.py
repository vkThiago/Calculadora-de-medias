a = int(input("Digite a nota da sua primeira prova: "))
b = int(input("Digite a nota da sua segunda prova: "))
c = int(input("Digite a nota da sua terceira prova: "))
nota =(a+b+c)/3
if nota > 7:
   print (f'Sua media foi {nota}, parabens você foi aprovado!')
else:
   print (f'Sua media foi {nota}, infelizmente você foi reprovado')
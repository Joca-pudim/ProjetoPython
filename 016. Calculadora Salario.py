# 16. Receba a quantidade de horas trabalhadas, o valor por hora, o percentual de desconto e o
# número de descendentes. Calcule o salário que serão as horas trabalhadas x o valor por hora.
# Calcule o salário líquido (= Salário Bruto – desconto). A cada dependente será acrescido R$ 100
# no Salário Líquido. Exiba o salário a receber.
# Maior que os outros esse

horas_trabalhadas = float(input("Digite a quantidade de horas trabalhadas: "))
valor_por_hora = float(input("Digite o valor por hora: "))
percentual_desconto = float(input("Digite o percentual de desconto (%): "))
numero_dependentes = int(input("Digite o número de dependentes: "))

salario_bruto = horas_trabalhadas * valor_por_hora

desconto = salario_bruto * (percentual_desconto / 100)

salario_liquido = salario_bruto - desconto

salario_a_receber = salario_liquido + (numero_dependentes * 100)

print("Salário a receber: R$", salario_a_receber)
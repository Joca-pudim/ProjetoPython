# 8. Receba o valor de um depósito em poupança. Calcule e mostre o valor após 1 mês de aplicação sabendo que rende 1,3% a. m.

deposito = float(input("Digite o valor do depósito: "))

valor_final =  (deposito * 1.013)

print("Valor após 1 mês: R$, {:.2f}".format(valor_final))
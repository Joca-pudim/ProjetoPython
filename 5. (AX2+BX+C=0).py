# 5. Receba os coeficientes A, B e C de uma equação do 2o grau (AX2+BX+C=0). Calcule e mostre as raízes reais (considerar que a equação possui 2 raízes reais).

A = float(input("Digite o valor de A: "))
B = float(input("Digite o valor de B: "))
C = float(input("Digite o valor de C: "))

delta = (B**2) - (4*A*C)

x1 = (-B + (delta ** 0.5)) / (2*A)
x2 = (-B - (delta ** 0.5)) / (2*A)

print("Raiz 1:", x1)
print("Raiz 2:", x2)

# esse aqui confundio um pouco a minha cabeça, comparado com os outros
# eu podia usar {:.2f}".format(X1) para diminuir o numero, mas... eu não sei o proposito dele então vo deixar inteiro
# suponho que adimitir meus erros aqui é melhor do que quando eu tiver trabalhando
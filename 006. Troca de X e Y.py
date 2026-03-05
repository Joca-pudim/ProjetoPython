# 6. Receba os valores em x e y. Efetua a troca de seus valores e mostre seus conteúdos.

x = float(input("Digite o valor de x: "))
y = float(input("Digite o valor de y: "))

temp = x
x = y
y = temp

print("Novo valor de x:", x)
print("Novo valor de y:", y)
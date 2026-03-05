#14. Receba 2 ângulos de um triângulo. Calcule e mostre o valor do 3o ângulo.

angulo1 = float(input("Digite o primeiro ângulo (em graus): "))
angulo2 = float(input("Digite o segundo ângulo (em graus): "))

angulo3 = 180 - (angulo1 + angulo2)

if angulo3 <= 0:
    print("Erro: a soma dos dois ângulos não pode ser maior ou igual a 180°")
else:
    print("O terceiro ângulo é:", angulo3, "graus")
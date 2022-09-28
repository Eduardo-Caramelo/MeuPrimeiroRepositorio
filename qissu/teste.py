# num1 = int(input("Digite o primeiro número: "))
# num2 = int(input("Digite o segundo número: "))
# num3 = int(input("Digite o terceiro número: "))
#
# soma = num1 + num2 + num3
#
# if soma >= 30 and soma <= 50:
#     print(f"Você ficou no orçamento\nVocê gastou: {soma}R$10")
# elif soma <=30:
#     print(f"Parabens você economizou\nVocê gastou: {soma}R$")
# else:
#     print(f"Você passou do seu orçamento\nVocê gastou: {soma}R$")
# num1 = float(input("Digite um número: "))
#
# if num1 >= 0.01:
#     print(f"{num1} é positivo")
# elif num1 < 0:
#     print(f"{num1} é negativo")
# else:
#     print(f"{num1} é neutro")
n1 = float(input("Digite sua primeira nota: "))
n2 = float(input("Digite sua segunda nota: "))

media = (n1 + n2) /2

if media >= 7 and media <= 10:
    print(f"Aprovado\nSua média foi: {media}")
elif media >= 5 and media <= 6:
    print(f"Exame\nSua média foi: {media}")
elif media < 5 and media > 0:
    print(f"Reprovado\nSua média foi: {media}")
elif media > 10:
    print("Nota muito alta")
elif media < 0:
    print("Nota abaixo do normal")
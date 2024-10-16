# Vamos solicitar como entrada dois números e depois vamos realizar uma operação simples entre eles.

numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))

operacao = input("Escolha a operação (+, -, *, /): ")

if operacao == "+":
    resultado = numero1 + numero2
    print("O resultado da soma é: ",resultado)
elif operacao == "-":
    resultado = (abs(numero1 - numero2))
    print("O resultado da subtração é: ", resultado)
elif operacao == "*":
    resultado = numero1 * numero2
    print("O resultado da multiplicação é: ",resultado)
elif operacao == "/":
    if numero2 != 0:
        resultado = numero1 / numero2
        print(f"O resultado da divisão é: ",resultado)
    else:
        print("Erro: Divisão por zero não é permitida.")
else:
    print("Operação inválida.")


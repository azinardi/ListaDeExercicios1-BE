def calculadora(operacao, num1, num2):
    if operacao == '+':
        return num1 + num2
    elif operacao == '-':
        return num1 - num2
    elif operacao == '*':
        return num1 * num2
    elif operacao == '/':
        if num2 == 0:
            return "Erro: divisão por zero!"
        else:
            return num1 / num2
    else:
        return "Operação inválida!"

operacao = input("Escolha a operação (+, -, *, /): ")
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

print("Resultado:", calculadora(operacao, num1, num2))
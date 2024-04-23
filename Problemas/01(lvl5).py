import math

print("Seja bem vindo a calculadora avançada alem as operaçoes basicas como +,-,* e / temos '**' para potencia e 'r' para raiz quadrada")

try:
    #digitando a operacao
    operacao = input("Digite a operação (+, -, *, /, ** ou r): ")
    #condicoes das operacoes
    
    if operacao == "+":
        num = float(input("Digite o numero base: "))
        num2 = float(input(f"{num} Somado por?: "))
        calculo = num + num2
        print(f"O resultado de {num} + {num2} é: {calculo}")
        
    elif operacao == "-":
        num = float(input("Digite o numero base: "))
        num2 = float(input(f"{num} Subtraido por?: "))
        calculo = num - num2
        print(f"O resultado de {num} - {num2} é: {calculo}")
        
    elif operacao == "*":
        num = float(input("Digite o numero base: "))
        num2 = float(input(f"{num} Multiplicado por?: "))
        calculo = num * num2
        print(f"O resultado de {num} * {num2} é: {calculo}")
        
    elif operacao == "/":
        num = float(input("Digite o numero base: "))
        num2 = float(input(f"{num} Divido por?: "))
        if num2 == 0:
            print("Não é possível dividir por zero!")
        else:
            calculo = num / num2
            print(f"O resultado de {num} / {num2} é: {calculo:.0f}")
            
    elif operacao == "**":
        num = float(input("Digite o numero base: "))
        num2 = float(input(f"{num} Elevado a?: "))
        calculo = math.pow(num, num2)
        print(f"O resultado de {num} ** {num2} é: {calculo:.0f}")
        
    elif operacao == "r":
        num = float(input("Digite o número qual queria descobrir a raiz: "))
        calculo = math.sqrt(num)
        print(f"A raiz de {num} é {calculo:.0f}")
    else:
        print("Operação inválida. Por favor, escolha entre '+', '-', '*', '/', '**' ou 'r'")
        #tratamento de error
except ValueError:
    print("Por favor, digite números válidos.")


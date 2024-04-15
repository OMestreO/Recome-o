num = int(input("Digite o primeiro numero:"))
num2 = int(input("Digite o segundo numero:"))
operacao = input("Digite a operacao: ")

if operacao == "+" :
    calculo = num + num2
    print("O resuldado de ", num, "+", num2, "é:", calculo)
elif operacao == "-" :
    calculo = num - num2
    print("O resuldado de ", num, "-", num2, "é:", calculo)
elif operacao == "*" :
    calculo = num * num2
    print("O resuldado de ", num, "*", num2, "é:", calculo)
elif operacao == "/" :
    calculo = num / num2
    calculo = round(calculo)
    print("O resuldado de ", num, "/", num2, "é:", calculo)
else :
    print("Operacao nao encontrada")

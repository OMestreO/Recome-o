"""Manipulação de erros: Se o usuário digitar algo que não é um número para os valores de entrada, seu programa irá gerar uma exceção. 
Você pode querer adicionar manipulação de erro para lidar com esse tipo de situação.

Melhoria da saída: A saída poderia ser melhorada para ser mais informativa e amigável ao usuário. Por exemplo, em vez de "Operacao nao encontrada", 
você poderia fornecer uma mensagem mais descritiva, como "Operação inválida. Por favor, escolha entre '+', '-', '*' ou '/'".

Aprimoramento da apresentação: Você poderia considerar formatar a saída para torná-la mais legível e esteticamente agradável. Por exemplo, você pode 
usar f-strings (disponíveis no Python 3.6 e posterior) para formatar a saída de uma maneira mais clara.
"""

#Aqui está uma versão do seu código com essas melhorias:

try:
    num = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o segundo número: "))
    operacao = input("Digite a operação (+, -, * ou /): ")

    if operacao == "+":
        calculo = num + num2
        print(f"O resultado de {num} + {num2} é: {calculo}")
    elif operacao == "-":
        calculo = num - num2
        print(f"O resultado de {num} - {num2} é: {calculo}")
    elif operacao == "*":
        calculo = num * num2
        print(f"O resultado de {num} * {num2} é: {calculo}")
    elif operacao == "/":
        if num2 == 0:
            print("Não é possível dividir por zero!")
        else:
            calculo = num / num2
            print(f"O resultado de {num} / {num2} é: {calculo:.2f}")
    else:
        print("Operação inválida. Por favor, escolha entre '+', '-', '*' ou '/'")
except ValueError:
    print("Por favor, digite números válidos.")
    
#Essas são apenas algumas sugestões para aprimorar seu código. Se tiver alguma dúvida ou quiser mais esclarecimentos, estou à disposição!
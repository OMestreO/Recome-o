def primo(numero):
    # Verifica se o número é menor ou igual a 1
    if numero <= 1:
        return f"O numero {numero} não é primo"
    
    # Itera de 2 até a raiz quadrada do número
    for i in range(2, int(numero ** 0.5) + 1):
        # Verifica se o número é divisível por i
        if numero % i == 0:
            # Se for divisível, não é primo
            return f"O numero {numero} não é primo"
    
    # Se não for divisível por nenhum número entre 2 e a raiz quadrada do número, é primo
    return f"O numero {numero} é primo"

#inserir o numero
num = int(input("digite um numero: "))
# Testando a função
print(primo(num))

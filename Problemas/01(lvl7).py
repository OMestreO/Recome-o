print("\nOlá usuario Um palíndromo é uma frase que é lida da mesma forma de trás para frente\nEscreva a frase que deseja testar se é um palíndromo\n ")

def palindromo(frase):
    # Remover espaços e pontuações e tornar todas as letras minúsculas
    formatandoFrase = ''.join(caractere for caractere in frase if caractere.isalnum()).lower()
    
    # Verificar se a frase é igual à sua versão invertida
    return formatandoFrase == formatandoFrase[::-1]

# Solicitar ao usuário para inserir uma frase
frase_user = input("Digite uma frase para verificar se é um palíndromo: ")

# Verificar se a frase fornecida pelo usuário é um palíndromo
if palindromo(frase_user) == True:
    print("\nA frase é um palíndromo")
else:
    print("\nA frase não é um palíndromo")
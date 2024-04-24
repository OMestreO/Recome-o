print("Este  programa em Python que verifique se duas palavras \nfornecidas pelo usuário são anagramas uma da outra\n")

def anagramas(palavras1, palavras2):
    # Remover os espaços em branco
    palavras1 = palavras1.replace(" ", "").lower()
    palavras2 = palavras2.replace(" ", "").lower()
    
    # Verificar se as duas palavras tem o mesmos numero de letras
    if len(palavras1) != len(palavras2) :
        return "\nAnagramas são palavras que tem mesmo numeros de letras\ne letras iguais. Exemplo 'amor' e 'roma'\n"
    
    # Contar ocorrencias de letras nas duas palavras
    contagem1 = {}
    contagem2 = {}
    
    for letra in palavras1 :
        contagem1[letra] = contagem1.get(letra, 0) + 1
        
    for letra in palavras2 :
        contagem2[letra] = contagem2.get(letra, 0) + 1
        
    if contagem1 == contagem2 :
        return f"\nA palavra '{palavras1}' é anagrama de '{palavras2}'"
    else :
        return f"\nA palavra '{palavras1}' não é anagrama de '{palavras2}'"
    
palavra1 = input("Digite sua primeira palavra: ")    
palavra2 = input("Digite a palavra para confimarmos se é anagrama:")    

print(anagramas(palavra1,palavra2))

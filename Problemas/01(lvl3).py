vogais = ['a', 'á', 'à', 'â', 'ã', 'e', 'é', 'è', 'ê', 'i', 'í', 'ì', 'î', 'o', 'ó', 'ò', 'ô', 'õ', 'u', 'ú', 'ù', 'û']

# Definindo uma string
texto = input("Digite uma palavra:")
texto = texto.lower()

# V para vogais
v = 0
# C para consoantes
c = 0

# Iterando sobre cada caractere na string usando um loop while
for letra in texto:
    if letra in vogais:
        v += 1
    else:
        c += 1
        
print(f"A palavra '{texto}' tem {v} vogais e {c} consoantes")
import random 
import string

def gerador(tamanho):
    # Definir os caracteres possíveis para inclusão na senha
    caracteres = string.ascii_letters + string.digits + string.punctuation

    # Gerar a senha aleatória combinando os caracteres escolhidos
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))

    return senha
    
# Solicitar ao usuário o comprimento da senha desejada
tamanho_senha = int(input("\nDigite o comprimento da senha desejada: "))

# Gerar a senha aleatória
gerando = gerador(tamanho_senha)

# Exibir a senha gerada para o usuário
print(f"\nA senha gerada é: {gerando}\n")
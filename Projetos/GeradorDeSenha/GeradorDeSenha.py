import random
import string

def password_generator():
    print("Bem-vindo ao Gerador de Senhas!")
    
    # Escolha do nível de complexidade
    print("Escolha o nível de complexidade da senha:")
    print("1. Apenas números")
    print("2. Letras e números")
    print("3. Letras, números e símbolos")
    try:
        complexity = int(input("Digite o número correspondente ao nível de complexidade desejado: "))
        length = int(input("Digite o comprimento da senha (mínimo 4): "))

        if length < 4:
            print("O comprimento mínimo é 4. Tente novamente.")
            return

        # Definição do conjunto de caracteres com base na complexidade
        if complexity == 1:
            characters = string.digits
        elif complexity == 2:
            characters = string.ascii_letters + string.digits
        elif complexity == 3:
            characters = string.ascii_letters + string.digits + string.punctuation
        else:
            print("Complexidade inválida. Tente novamente.")
            return

        # Geração da senha
        password = ''.join(random.choice(characters) for _ in range(length))
        print(f"Sua senha gerada é: {password}")
    except ValueError:
        print("Erro: Por favor, insira valores numéricos válidos.")

# Executa o gerador de senhas
if __name__ == "__main__":
    password_generator()

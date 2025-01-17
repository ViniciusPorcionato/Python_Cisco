def calculator():
    print("Bem-vindo à Calculadora Simples!")
    
    # Entrada de dados
    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        print("Escolha a operação:")
        print("1. Adição (+)")
        print("2. Subtração (-)")
        print("3. Multiplicação (*)")
        print("4. Divisão (/)")
        operation = input("Digite o número ou símbolo da operação desejada: ")

        # Processamento e saída
        if operation in ['1', '+']:
            print(f"Resultado: {num1} + {num2} = {num1 + num2}")
        elif operation in ['2', '-']:
            print(f"Resultado: {num1} - {num2} = {num1 - num2}")
        elif operation in ['3', '*']:
            print(f"Resultado: {num1} * {num2} = {num1 * num2}")
        elif operation in ['4', '/']:
            if num2 != 0:
                print(f"Resultado: {num1} / {num2} = {num1 / num2}")
            else:
                print("Erro: Divisão por zero não é permitida.")
        else:
            print("Operação inválida. Tente novamente.")
    except ValueError:
        print("Erro: Por favor, insira valores numéricos válidos.")

# Executa a calculadora
if __name__ == "__main__":
    calculator()

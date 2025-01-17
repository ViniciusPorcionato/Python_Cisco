def temperature_converter():
    print("Bem-vindo ao Conversor de Temperaturas!")
    
    # Entrada de dados
    try:
        print("Escolha a unidade de entrada:")
        print("1. Celsius (C)")
        print("2. Fahrenheit (F)")
        print("3. Kelvin (K)")
        input_unit = input("Digite o número correspondente à unidade de entrada: ")
        temperature = float(input("Digite a temperatura: "))

        print("Escolha a unidade de saída:")
        print("1. Celsius (C)")
        print("2. Fahrenheit (F)")
        print("3. Kelvin (K)")
        output_unit = input("Digite o número correspondente à unidade de saída: ")

        # Processamento e conversões
        result = None

        if input_unit == '1':  # Celsius
            if output_unit == '1':
                result = temperature  # Celsius para Celsius
            elif output_unit == '2':
                result = (temperature * 9/5) + 32  # Celsius para Fahrenheit
            elif output_unit == '3':
                result = temperature + 273.15  # Celsius para Kelvin
        elif input_unit == '2':  # Fahrenheit
            if output_unit == '1':
                result = (temperature - 32) * 5/9  # Fahrenheit para Celsius
            elif output_unit == '2':
                result = temperature  # Fahrenheit para Fahrenheit
            elif output_unit == '3':
                result = (temperature - 32) * 5/9 + 273.15  # Fahrenheit para Kelvin
        elif input_unit == '3':  # Kelvin
            if output_unit == '1':
                result = temperature - 273.15  # Kelvin para Celsius
            elif output_unit == '2':
                result = (temperature - 273.15) * 9/5 + 32  # Kelvin para Fahrenheit
            elif output_unit == '3':
                result = temperature  # Kelvin para Kelvin
        
        # Saída
        if result is not None:
            print(f"A temperatura convertida é: {result:.2f}")
        else:
            print("Conversão inválida. Verifique as unidades escolhidas.")
    except ValueError:
        print("Erro: Por favor, insira valores numéricos válidos.")

# Executa o conversor
if __name__ == "__main__":
    temperature_converter()

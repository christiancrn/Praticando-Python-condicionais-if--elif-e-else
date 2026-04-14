def somar(a, b):
    return a + b
try:
    numero1 = float(input("Informe o primeiro número: "))
    numero2 = float(input("Informe o segundo número: "))

    resultado = somar(numero1, numero2)
    print(f"A soma dos números é: {resultado}")
except ValueError:
    print("Por favor, informe números válidos.")
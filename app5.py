gasto_A = float(input("Informe o gasto do cliente A (R$): "))
gasto_B = float(input("Informe o gasto do cliente B (R$): "))
gasto_C = float(input("Informe o gasto do cliente C (R$): "))
salario_mensal = float(input("Informe o salário mensal do cliente (R$): "))

if (gasto_A + gasto_B + gasto_C) > salario_mensal:
    print("O cliente está gastando mais do que ganha.")
else:
    print("O cliente está gastando dentro do seu orçamento.")

if __name__ == '__main__':
    pass        
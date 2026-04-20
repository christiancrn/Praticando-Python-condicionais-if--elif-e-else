while True:
    cpf = input("Qual seu CPF: ")
    if cpf.isdigit() and len(cpf) == 11:
        print("CPF valido!!")
        break
    else:
        print("CPF incorreto, Digite novamente..")
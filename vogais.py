def contar_vogais(texto):
    vogais = 'aeiouAEIOU'
    contador = 0
    for char in texto:
        if char in vogais:
            contador += 1
    return contador

texto = input("Digite um texto: ")
total_vogais = contar_vogais(texto)
print(f"O texto contém {total_vogais} vogais.")
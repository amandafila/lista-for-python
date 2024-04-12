quantidade = int(input("Quantas idades serão informadas? "))
soma = 0
for c in range(0, quantidade): 
    valor = int(input("Digite uma idade: "))
    soma += valor
media = soma/quantidade
print(f"A média é {media}")
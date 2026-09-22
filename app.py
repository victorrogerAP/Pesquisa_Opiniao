bom = 0
ruim = 0
excelente = 0
for i in range(50):
    nome = input("Digite seu nome: ")
    idade =  int(input("Qual sua idade: "))
    opiniao = int(input("Qual sua Opinião?\n " \
    "1 - Bom\n " \
    "2 - Ruim\n " \
    "3 - Excelente "))
    match opiniao:
        case 1:
            bom += 1
            print("Seu nome é ",nome,"e tem ",idade,"anos e sua opinião foi boa.")
        case 2:
            ruim += 1
            print("Seu nome é ",nome,"e tem ",idade,"anos e sua opinião foi ruim.")
        case 3:
            excelente += 1
            print("Seu nome é ",nome,"e tem ",idade,"anos e sua opinião foi excelente.")

print("Quantidade de respostas boas foram",bom)
print("Quantidade de respostas ruins foram",ruim)
print("Quantidade de respostas excelentes foram",excelente)
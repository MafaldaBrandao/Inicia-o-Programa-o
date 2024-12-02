#Mafalda Brandão
#Pedro Fevereiro

def calcular(c):
    if c< 1250:
        parcelas: 2417.56
        taxas:3.74
    else: 
        parcelas: 8813.22
        taxas: 8.86

    IA=taxas*c-parcelas
    return IA


def main():
    nome = (input( "Qual é o nome do comprador?"))
    marca = (input( "Qual é a marca do veículo?"))
    modelo = (input( "Qual é o modelo do veículo?"))
    c = float(input( "Qual é cilindrada do motor?"))
    IA= calcular(c)
    print("IA=", IA)

if __name__=='__main__':
    main()
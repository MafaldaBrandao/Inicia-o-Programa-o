#ler 3 numeros reais e verificar se podem ser as medidas 
#dos lados de um triangulo

a = float(input( "Insira um numero:"))
b = float(input( "Insira um numero:"))
c = float(input( "Insira um numero:"))

if a + b > c and a + c > b and b + c > a:
    print("Os números podem formar um triângulo.")
else:
    print("Os números não podem formar um triângulo.")
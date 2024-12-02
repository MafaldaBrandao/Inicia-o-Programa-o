#ler 3 numeros reais e verificar se podem ser as medidas dos lados de um triangulo
#caso seja um triangulo, classificar o triangulo (isosceles, escaleno ou equilatero)

a = float(input( "Insira um numero:"))
b = float(input( "Insira um numero:"))
c = float(input( "Insira um numero:"))

if a + b > c and a + c > b and b + c > a:
    print("Os números podem formar um triângulo.")

    if a == b == c:
        print("O triângulo é Equilátero (todos os lados iguais).")
    elif a == b or a == c or b == c:
        print("O triângulo é Isósceles (dois lados iguais).")
    else:
        print("O triângulo é Escaleno (todos os lados diferentes).")
    
else:
    print("Os números não podem formar um triângulo.")
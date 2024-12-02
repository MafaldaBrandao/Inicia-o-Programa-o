
peso = float(input( "Insira o seu peso:"))
altura = float(input( "Insira a sua altura:"))
imc = peso / (altura**2)
print(" O teu imc é " : imc )

if imc < 18.5:
    print("Classificação:Abaixo do peso.")
elif 18.5 <= imc <= 24.9:
    print("Classificação: Peso normal.")
elif 25.0 <= imc <= 29.9:
    print("Classificação: Sobrepeso.")
elif 30.0 <= imc <= 34.9:
    print("Classificação: Obesidade grau 1.")
elif 35.0 <= imc <= 39.9:
    print("Classificação: Obesidade grau 2.")
else:
    print("Classificação: Obesidade grau 3 (mórbida).")
def classifica_imc(imc): 
    if imc < 18.5:
        return "abaixo do peso"
    elif 18.5 <= imc < 24.9:
        return "peso normal"
    elif 24.9 <= imc < 29.9:
        return "sobre peso"
    else:
        return "obesidade"
    
peso = input("Digite seu peso em Kg: ")
altura = input("Digite sua altura em mt: ")
imc = peso / (altura ** 2)
print(classifica_imc(imc))

cedula = ""
coeficientes = [2,1,2,1,2,1,2,1,2]
suma_total = 0
for i in range(9):
    digito = int(cedula[i])
    producto = digito * coeficientes[i]
    if producto >= 10:
        producto -= 9 
    suma_total += producto
    residuo = suma_total % 10
    if residuo == 0:
        digito_verificador = 0
    else: digito_verificador = 10 - residuo
    print(digito_verificador)

    print("lo he logrado")
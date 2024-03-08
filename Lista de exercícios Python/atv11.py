lado1 = float(input("Digite o primeiro lado: "))
lado2 = float(input("Digite o segundo lado: "))
lado3 = float(input("Digite o terceiro lado: "))

def tipotriangulo(lado1, lado2, lado3):
    if lado1 == lado2 and lado2 == lado3:
        return "Equilátero"
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        return "Isósceles"
    else:
        return "Escaleno"
        
def verificatriangulo(lado1, lado2, lado3):
    return lado1 + lado2 > lado3 and lado1 + lado3 > lado2 and lado2 + lado3 > lado1
    
if verificatriangulo(lado1, lado2, lado3):
    tipo = tipotriangulo(lado1, lado2, lado3)
    print(f"Os lados {lado1}, {lado2} e {lado3} formam um triângulo tipo {tipo}.")
else:
        print("Os valores informados não formam um triângulo.")
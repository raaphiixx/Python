reta1 = int(input("Digite o primeiro lado: "))
reta2 = int(input("Digite o segundo lado: "))
reta3 = int(input("Digite o terceiro lado: "))
print()
if(reta1 + reta2 > reta3) and (reta3 + reta1 > reta2) and (reta2 + reta3 > reta1):
    print("É um triângulo!")
    if reta1 == reta2 == reta3:
        print("Triângulo EQUILÁTERO")
    elif (reta1 == reta2 != reta3) or (reta1 == reta3 != reta2) or (reta2 == reta3 != reta1):
        print("Triângulo ISÓSCELES")
    else:
        print("Triângulo ESCALENO")
else:
    print("Não é um triângulo!")
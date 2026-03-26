nota1=float(input("ingrese la nota del parcial 1: "))
nota2=float(input("ingrese la nota del parcial 2: "))
nota3=float(input("ingrese la nota del parcial 3: "))
notas=[nota1, nota2, nota3]
promedio = sum(notas) / len(notas)
print(promedio)
# Programa para verificar si un numero es par o impar
# input

X=int(input("Digite el valor de x: "))
      
# Processing
      
R = (X % 2)

if R==0:
   rta= "PAR"

else:
   rta= "IMPAR"
print("Hola")

#Output
print("El numero " + str(X) + " es: " +  rta )
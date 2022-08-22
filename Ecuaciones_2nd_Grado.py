print ("ECUACIONES SEGUNDO GRADO")
print
print ("Ve introduciendo valores:")
A = int(input("A="))
B = int(input("B="))
C = int(input("C="))
Estructura_1 = B*B-4*A*C
Ráiz_Cuadrada1= float(Estructura_1**(1/2))
Cálculos1 = ((-B + Ráiz_Cuadrada1)/(2*A))
Cálculos2 = ((-B - Ráiz_Cuadrada1)/(2*A))
print ("1er resultado:" + str(Cálculos1))
print ("2nd resultado:" + str(Cálculos1))



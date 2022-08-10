print ("CALCULADORA")
print ("1-sumar")
print ("2-restar")
print ("3-multiplicar")
print ("4-Dividir")
elección = int(input("Escoge una opción"))
print ("Introduce dos números que quieras calcular")
if elección is 1:
    primero = int(input("Primera Cifra"))
    segundo = int(input("Segunda Cifra"))
    resultado = primero + segundo
    print (str(primero)+"+"+str(segundo)+"="+str(resultado))
if elección is 2:
    primero = int(input("Primera Cifra"))
    segundo = int(input("Segunda Cifra"))
    resultado = primero - segundo
    print (str(primero)+"-"+str(segundo)+"="+str(resultado))
if elección is 3:
    primero = int(input("Primera Cifra"))
    segundo = int(input("Segunda Cifra"))
    resultado = primero * segundo
    print (str(primero)+"*"+str(segundo)+"="+str(resultado))
if elección is 4:
    primero = int(input("Primera Cifra"))
    segundo = int(input("Segunda Cifra"))
    resultado = primero / segundo
    print (str(primero)+"/"+str(segundo)+"="+str(resultado))
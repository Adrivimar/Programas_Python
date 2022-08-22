print ("DIME CUÁNTOS AÑOS TIENES Y TE DIRÉ SI ERES MAYOR DE EDAD Y DE QUÉ SIGLO ERES")
edad = input ()
edad = int(edad)
if edad < 18:
    print ("No eres mayor de edad")
else:
    print ("Eres mayor de edad")
print
if edad < 22:
    print ("Eres del siglo XXI")
else:
    print ("Eres del siglo XX")
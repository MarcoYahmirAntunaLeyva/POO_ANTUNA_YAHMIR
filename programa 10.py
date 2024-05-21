while True:
    
   n1 = float(input("Ingrese un numero: "))
   n2 = float(input("Ingrese un segundo numero: ")) 
   
   suma = n1 + n2
   print("La suma de",n1,"y",n2,"es",suma,)
   
   continuar = input("¿Quieres hacer otrs suma? (ingresa 'n' para detenerse, cualquier otra tecla para continuar): ")
   
   if continuar.lower() == 'n':
       print("¡Programa terminado!")
       break
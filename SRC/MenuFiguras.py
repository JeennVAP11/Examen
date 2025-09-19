from blessed import Terminal
term = Terminal()

def MenudeFiguras(MenudeFiguras):
     print (f"-------------- {MenudeFiguras} -------------- ")


def menu(): 
  opcion = -1
  
  while not opcion==0:
     print(f"{term.orange} =======================")
     print(f" {term.green}   Menu de Figuras")
     print(f" {term.orange} =======================")
     print(f"{term.pink} 1.{term.normal} Rectangulo")
     print(f"{term.pink} 2.{term.normal} Cuadrado")
     print(f"{term.pink} 3.{term.normal} Circulo")
     print(f"{term.pink} 4.{term.normal} Triangulo")
     print(f"{term.red} 0. Salir{term.normal}")

     print(f"{term.blue}Elige una opcion:")

     opcion = int(input())

     print(f"{term.purple}Opcion elegida: {opcion}")

     evaluar_opcion_2(opcion)
def evaluar_opcion_2(opcion):
   
   match opcion:
      case 1:
        
         print("-------------------------------")
         print(f" {term.green} Area y Perimetro del Rectangulo {term.normal} ")
         print("------------------------------- ")

         numero1=input ("Ingresa la Altura de la figura:")
         numero2=input ("Ingresa el Ancho de la figura:" )
         Altura=float(numero1)
         Ancho=float(numero2)

         print(f"El {term.red}area {term.normal} de la figura es: ", (Altura * Ancho))
         print(f"El {term.red}perimetro {term.normal} de la figura es: ", ((2*Altura) + (2*Ancho)))

      case 2:

         print(f"{term.green}-------------------------------{term.normal}")
         print("Area y Perimetro del Cuadrado")
         print(f"{term.yellow}-------------------------------{term.normal}")

         numero1=input ("Ingresa un Lado de la figura:")
         Lado=float(numero1)

         print(f"El {term.red}area {term.normal} de la figura es: ", (Lado * Lado))
         print(f"El {term.red}perimetro {term.normal} de la figura es: ", (Lado +Lado +Lado + Lado))

      case 3:

         print(f"{term.Yellow}-------------------------------{term.normal}")
         print("Area y Perimetro del Circulo")
         print(f"{term.Yellow}-------------------------------{term.normal}")

         numero1=input ("Ingresa el radio de la figura:")
         radio=float(numero1)
         pi=3.1416

         print(f"El {term.red}area {term.normal} de la figura es: ", (pi * (radio**2)))
         print(f"El {term.red}perimetro {term.normal} de la figura es: ", (2 * pi * radio))

      case 4:
         
         print(f"{term.Yellow}-------------------------------{term.normal}")
         print("Area y Perimetro del Triangulo")
         print(f"{term.Yellow}-------------------------------{term.normal}")

         numero1=input ("Ingresa la Altura de la figura:")
         numero2=input ("Ingresa la base de la figura:" )
         numero3=input ("Ingresa un lado de la figura:" )
         Altura=float(numero1)
         Base=float(numero2)
         Lado=float(numero3)

         print(f"El {term.red}area {term.normal} de la figura es: ", ((Base * Altura)/2))
         print(f"El {term.red}perimetro {term.normal} de la figura es: ", (Lado + Lado + Lado))

      case _:
         pass
   a=input ()  


def factorial(numero):
    resultado = 1 
    if numero <= 0:
        return "No se puede calcular el factorial"
    
    for i in range (1, numero + 1):
        resultado = resultado * i
    return resultado   

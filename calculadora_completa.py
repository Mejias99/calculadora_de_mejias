print ("Hola, Mundo! Bienvenido a tu calculadora interactiva. \n")

def suma (x, y):
  
    return x + y


def resta (x, y):
  
    return x - y


def multiplica (x, y):
  
    return x * y


def divide(x, y):
    return x / y


print("¿Qué quieres que haga?\n1.Suma \n2.Resta \n3.Multiplicación \n4.División")


while True:
  
    decision = input("Escribe el número de la operación que deseas que realice: ")

    if decision in ('1', '2', '3', '4'):
      
        num1 = float(input("Escribe el primer operador: "))
      
        num2 = float(input("Escribe el segundo operador: "))

      
        if decision == '1':
          
            print(num1, "+", num2, "=", suma (num1, num2))

      
        elif decision == '2':
          
            print(num1, "-", num2, "=", resta(num1, num2))
          

        elif decision == '3':
          
            print(num1, "*", num2, "=", multiplica(num1, num2))
          

        elif decision == '4':
          
            print(num1, "/", num2, "=", divide(num1, num2))

      
        next_calculation = input("¿Deseas que realice otra operación? (sí/no): ")
      
        if next_calculation == "no":
          
          break

        if next_calculation != "sí":

          print ("Mmm no sé que has puesto pero, bueno, supongo que quieres que realice otra operación")

  
    else:
        print("Mmmm... no sé que has introducido pero creo que no coincide con ninguna de las opciones que te he dado")

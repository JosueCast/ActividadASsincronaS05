import random

nombre1 = "Josué Aarón"
apellido1 = "Castillo Valdiviezo"
sexo1 = "Masculino"
edad1 = 21

nombre2 = "Gerardo Antonio"
apellido2 = "Rosa Menjivar"
sexo2 = "Masculino"
edad2 = 17

nombre3 = "José Nicolás"
apellido3 = "Abrego Salguero"
sexo3 = "Masculino"
edad3 = 18

nombre4 = "Rolando Alexander"
apellido4 = "Perez Lopez"
sexo4 = "No binario"
edad4 = 17

nombre5 = "Bryan Edenilson"
apellido5 = "Quintanilla Alberto"
sexo5 = "Masculino"
edad5 = 22

saludo = "Programando con python por primer vez"
# mostrando integrantes del grupo
nombre_completo1 = nombre1 + " " + apellido1
nombre_completo2 = nombre2 + " " + apellido2
nombre_completo3 = nombre3 + " " + apellido3
nombre_completo4 = nombre4 + " " + apellido4
nombre_completo5 = nombre5 + " " + apellido5

print("--------------------------------------------------------\nEscoja que quiere hacer\n----------------------------------------------")
print("Mostrar Listado de integrantes: 1")
print("Sacar Promedio de edad de los integrantes: 2")
print("Buscar la posicion de una palabra: 3")
print("Listados con la edad de los integrantes al finalizar la carrera: 4")
option = input("\nIngresar Opcion:  ")

match option:
    case "1":
        # Mostrando lista de usuarios 
        print("Los nombres completos de los integrantes son:\n------------------------------------------------------------\n" )
        print(nombre_completo1)
        print(nombre_completo2)
        print(nombre_completo3)
        print(nombre_completo4)
        print(nombre_completo5)
    case "2":
        # Buscar promedio de edades de integrantes
        promedio_Edades = (edad1 + edad2 + edad3 + edad4 + edad5) / 5
        print("Promedio de Integrantes:  ",promedio_Edades)
    case "3":
        # Buscar Frase en una cadena 
        frase_1 = "Programado con Gerardo pyton " 
        frase_2 = "Programado con Bryan pyton " 
        frase_3 = "Programado con Rolando pyton " 
        frase_4 = "Programado con Nico pyton " 
        # Random numero esto esta de mas
        numb_random = random.randint(1,4)
        print(numb_random)
        #sacando frase aleatorio para dinamismo
        
        match numb_random:
                case 1: 
                     print(frase_1)
                     word = input("Palabra a buscar: ")
                     word_search= frase_1.find(word)
                     print(word_search)
                case 2:   
                     print(frase_2)
                     word = input("Palabra a buscar: ")
                     word_search= frase_2.find(word)
                     print(word_search)
                case 3: 
                     print(frase_3)
                     word = input("Palabra a buscar: ")
                     word_search= frase_3.find(word)
                     print(word_search)
                case 4: 
                     print(frase_4)
                     word = input("Palabra a buscar: ")
                     word_search= frase_4.find(word)
                     print(word_search)
                case _: 
                     print("No lo he definidio]]")
    case "4":

        print("Los integrantes con la edad al finalizar la carrera:\n---------------------------------------------------------------------" )
        print(nombre_completo1,"Edad al finalizar la carrera sera de: ",edad1 + 5,"Años")
        print(nombre_completo2,"Edad al finalizar la carrera sera de: ",edad2 + 5,"Años")
        print(nombre_completo3,"Edad al finalizar la carrera sera de: ",edad3 + 5,"Años")
        print(nombre_completo4,"Edad al finalizar la carrera sera de: ",edad4 + 5,"Años")
        print(nombre_completo5,"Edad al finalizar la carrera sera de: ",edad5 + 5,"Años")
        print("----------------------------------------------------------------------------------------" )

    case _:
        print("--------------------------------------------\n*** Esa Opcion no esta disponible ***\n--------------------------------------------")


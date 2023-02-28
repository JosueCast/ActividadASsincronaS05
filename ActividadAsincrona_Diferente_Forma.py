#actividad asincrona
mydict = [{'nombres': "Josue Aaron",  "apellidos": "Castillo Valdiviezo","edad": "21","sexo": "Masculino","id": 1 },
         {'nombres': "Jose Nicolas",  "apellidos": "Abrego fuentes","edad": "19","sexo": "Masculino","id": 2  },
         {'nombres': "Bryan alexis",  "apellidos": "Fuente abrego","edad": "23","sexo": "Masculino", "id": 3 },
         {'nombres': "Jose Nicolas",  "apellidos": "Abrego fuentes","edad": "18","sexo": "Masculino","id": 4 },
         {'nombres': "Rocio Maria",  "apellidos": "Marbelly Paz","edad": "18","sexo": "Femenino","id": 5  },]
## variables ##
len = len(mydict) 
i=0
promedio = 0
#Mostrar cada Integrante del grupowhile 
#sacar promedio de los integrantes
while i < len:
    list = mydict[i]
    print("Integrante ",int(i) + int(1)," ",list["nombres"],list["apellidos"],list["edad"],list["sexo"])
    edades = mydict[i]
    promedio = int(promedio) + int(edades["edad"])
    i = i + 1
    #finaliza el bucle
print(" ------------------------------------------------------------------------","\n La edad promedio de los integrantes es: ",promedio / len) 
buscar = input("Buscar integrante...> ")
for alumnos in mydict:
    # print(alumnos)
    
    if buscar == alumnos["nombres"]:
        print("-----------------------------------------------------------")
        print("Nombre: ",alumnos["nombres"] +"",alumnos["apellidos"],"\nLa edad al finalizar la carrera sera de: ",int(alumnos["edad"]) + 5," Años")
        break
        



































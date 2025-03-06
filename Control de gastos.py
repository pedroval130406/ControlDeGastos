# variables y listas utilizadas
extraL = []
extra = 0
presupuestoFinal = 0
gastoL = []
conceptoGastoL = []
conceptoExtraL = []
fechaGastoL = []
fechaExtraL = []
ahorro = int
ahorroFinal = 0
ahorroL = []
fechaAhorroL = []
fechaRetiroL = []
retiroL = []

#Importar la libreria datetime para el formato del tiempo
from datetime import datetime

# Función para agregar concepto y fecha
def extrasInfo (tipoDato):
    while True:
        if tipoDato == "extra":
            conceptoExtra = input("Ingresa el concepto del extra: ")
            if conceptoExtra.isalnum():
                conceptoExtraL.append(conceptoExtra)
                print(f"Concepto '{conceptoExtra}' guardado correctamente")
                break
            else:
                print("Ingresa un valor válido (solo letras y números).")

        elif tipoDato == "gasto":
            conceptoGasto = input("Ingresa el concepto del gasto: ")
            if conceptoGasto.isalnum():
                conceptoGastoL.append(conceptoGasto)
                print(f"Concepto '{conceptoGasto}' guardado correctamente")
                break
            else:
                print("Ingresa un valor válido (solo letras y números).")
        
        elif tipoDato == "fechaExtraL":
            fecha_str = input("Ingresa la fecha en formato DD/MM/YYYY: ")
            try:
                fechaExtra = datetime.strptime(fecha_str, "%d/%m/%Y")  # Validar formato
                print(f"Fecha válida: {fechaExtra.strftime('%d/%m/%Y')}")
                fechaExtraL.append(fechaExtra)
                break
            except ValueError:
                print("Formato incorrecto. Usa DD/MM/YYYY.")

        elif tipoDato == "fechaGastoL":
            fecha_str = input("Ingresa la fecha en formato DD/MM/YYYY: ")
            try:
                fechaGasto = datetime.strptime(fecha_str, "%d/%m/%Y")  # Validar formato
                print(f"Fecha válida: {fechaGasto.strftime('%d/%m/%Y')}")
                fechaGastoL.append(fechaGasto)
                break
            except ValueError:
                print("Formato incorrecto. Usa DD/MM/YYYY.")

        elif tipoDato == "fechaAhorroL":
            fecha_str = input("Ingresa la fecha en formato DD/MM/YYYY: ")
            try:
                fechaAhorro = datetime.strptime(fecha_str, "%d/%m/%Y")  # Validar formato
                print(f"Fecha válida: {fechaAhorro.strftime('%d/%m/%Y')}")
                fechaAhorroL.append(fechaAhorro)
                break
            except ValueError:
                print("Formato incorrecto. Usa DD/MM/YYYY.")
        
        elif tipoDato == "fechaRetiroL":
            fecha_str = input("Ingresa la fecha en formato DD/MM/YYYY: ")
            try:
                fechaRetiro = datetime.strptime(fecha_str, "%d/%m/%Y")  # Validar formato
                print(f"Fecha válida: {fechaRetiro.strftime('%d/%m/%Y')}")
                fechaRetiroL.append(fechaRetiro)
                break
            except ValueError:
                print("Formato incorrecto. Usa DD/MM/YYYY.")

    return conceptoExtraL, conceptoGastoL, fechaGastoL, fechaExtraL

#Ciclo while con el menú principal de opciones
while True:
    try:
        print ("1.- Guardar el presupuesto.")
        print ("2.- Agregar presupuesto extra.")
        print ("3.- Registrar gastos.")
        print ("4.- Reporte de gastos completos.")
        print ("5.- Mostrar presupuesto.")
        print ("6.- Estado de salud finaciera.")
        print ("7.- Ahorros.")
        print ("8.- Salir.")
        opcion = int(input("¿Qué desea hacer?: "))
        print ("---------------------------------------------------------------------")

        # Opcion uno para ingresar el presupuesto    
        if opcion == 1:
            while True:
                try:
                    presupuesto = int(input("Ingresa tu presupuesto: "))
                    print ("Presupuesto guardado exitosamente")
                    print (f"Tienes {presupuesto}$ de presupuesto")              
                    print ("---------------------------------------------------------------------")
                    presupuestoFinal = presupuesto #Asignamos que prresupuesto final tenga el mismo valor que presupuesto
                    break
                except ValueError:
                    print("Elija un valor valido") #Asignamos un valor válido.

# Agregar el presupuesto extra
        elif opcion == 2: 
            extra = int(input("Ingresa presupuesto extra: "))
            extraL.append(extra) # Se agrega a una lista para el reporte de todos
            extrasInfo(tipoDato="extra")
            extrasInfo(tipoDato="fechaExtraL")
            presupuestoFinal += extra  # Se suma el presupuesto final más el extra que se tenga
            print("Presupuesto extra agregado correctamente.")
            print(f"Se agregó {extra}$ a tu presupuesto, ahora tienes {presupuestoFinal}$.")
            print("---------------------------------------------------------------------")

        #Opción 3 de registro de datos    
        elif opcion == 3:
            try:
                gasto = int(input("Ingresa tu gasto: "))  
                gastoL.append(gasto)
                extrasInfo(tipoDato="gasto")
                extrasInfo(tipoDato="fechaGastoL")
                presupuestoFinal -= gasto  # Restamos solo el gasto actual, no la suma total
                print("Gasto realizado correctamente.") 
                print(f"Se ha gastado {gasto}$ en tu presupuesto, ahora tienes {presupuestoFinal}$.")
                print("---------------------------------------------------------------------")
            except ValueError:
                print("Ingresa un valor válido.")

        # Generar el reporte de gasto
        elif opcion == 4:
            print("Aquí tienes tu reporte completo: ") 
            print (f"Tú presupuesto inicial es {presupuesto}")
            print (f"Tu preupuesto final es {presupuestoFinal}$.") #Muestra un reporte general
            print ("")
            print ("Registro de presupuesto extra")
            for extra, conceptoExtra, fechaExtra in zip(extraL, conceptoExtraL, fechaExtraL): #Mostrar la lista de presupuesto extra
                print (f"+ {extra}$ / Concepto: {conceptoExtra} / Fecha: {fechaExtra}")
            print ("")
            print ("Registro de Gastos")
            for gasto, conceptogasto, fechaGasto in zip (gastoL, conceptoGastoL, fechaGastoL): #Mostrar la lista de gastps
                print (f"- {gasto}$ / Concepto: {conceptogasto} / Fecha: {fechaGasto}")
            print ("")
            print ("Retiros de ahorrros")
            for retiro, fechaRetiro in zip (retiroL, fechaRetiroL): # Mostrar lista de retiros de ahorros
                print (f"- {retiro} / Fecha: {fechaRetiro}")
            print("---------------------------------------------------------------------")
        
        #Imprime el presupuesto final
        elif opcion == 5:
            print (f"Tu presupuesto actualmente es de {presupuestoFinal}$.")
            print ("---------------------------------------------------------------------")

        # Muestra el estado de salud financiera
        elif opcion == 6:
            print("Tu estado de salud financiera es:")
            if 0 <= presupuestoFinal <= 200: #Si esta entre 0 y 200 se considera buena
                print("BUENA")
                print("Pero te recomendamos dejar más dinero o hacer ahorros para cualquier emergencia")
            elif 200 < presupuestoFinal >= 500: #Más de 500 es muy buena
                print("MUY BUENA")
                print("Buen control en tus gastos, deberías considerar ahorrar")
            elif presupuestoFinal > 500 and ahorroFinal > 0: #Si tienes más de 500 y cuentas con ahorros es excelente
                print("EXCELENTE")
                print("Sigue manteniendo tu salud financiera en este estado")
            else: #Si estas en negativo es mala
                print("MALA")
                print("Cuida tus gastos, ten un control")
            print("---------------------------------------------------------------------")

        #Opción de ahorros
        elif opcion == 7: 
            opcionAhorros = 0 #Abrir variable para opción de ahorros
            while opcionAhorros != 4:
                try:
                    print ("1.- Ver ahorros.")
                    print ("2.- Guardar ahorros.")
                    print ("3.- Retirar ahorros.")
                    print ("4.- Volver a menú principal.")
                    opcionAhorros = int(input("Ingresa una opción: ")) #Menú de opciones

                    if opcionAhorros == 1: #Muestra los ahorros y su lista. Tanto ahorros como retiros.
                        print (f"Tus ahorros son {ahorroFinal}$.")
                        print ("")
                        print ("Lista de ahorros.")
                        for ahorro, fechaAhorro in zip (ahorroL,fechaAhorroL):
                            print (f"+ {ahorro} / Fecha: {fechaAhorro}")
                        print ("")
                        print ("Lista de retiros.")
                        for retiro, fechaRetiro in zip (retiroL, fechaRetiroL):
                            print (f"- {retiro} / Fecha: {fechaRetiro}")
                        print ("---------------------------------------------------------------------")

                    elif opcionAhorros == 2: # Para agregar
                        print(f"Lo recomendado es el 33%, tienes {presupuestoFinal}$, su 33% es {presupuestoFinal/3}$.") #Te sugiere el ahorro
                        while True:
                            try:
                                ahorro = int(input("Ingresa la cantidad de tu ahorro: "))
                                if ahorro <= presupuestoFinal:  # Se permite ahorrar si es menor o igual al presupuesto disponible
                                    ahorroL.append(ahorro)
                                    extrasInfo(tipoDato="fechaAhorroL")
                                    ahorroFinal += ahorro  # Se suma solo el ahorro actual
                                    presupuestoFinal -= ahorro  # Se descuenta solo el ahorro actual
                                    print(f"Ahorro guardado exitosamente. Se ahorraron {ahorro}$, ahora tienes {ahorroFinal}$ en ahorros.")
                                    print("---------------------------------------------------------------------")
                                    break
                                else:
                                    print("No puedes ahorrar más de lo que tienes disponible.")
                            except ValueError:
                                print("Ingresa un valor válido.")

                    elif opcionAhorros == 3: #Retirar de ahorros
                        retiro = int(input(f"Tienes {ahorroFinal}$, ingresa la cantidad a retirar: "))
                        if retiro <= ahorroFinal:
                            retiroL.append(retiro)
                            extrasInfo(tipoDato="fechaRetiroL")
                            ahorroFinal -= retiro  # Restar el retiro del ahorro total
                            print(f"Retiro exitoso. Has retirado {retiro}$, ahora tienes {ahorroFinal}$ en ahorros.")
                            print("---------------------------------------------------------------------")
                        else:
                            print("No puedes retirar más de lo que tienes en ahorros.")
                    
                    elif opcionAhorros == 4: #Volver al menú principal
                        print ("Regresando al menú principal")
                        print ("---------------------------------------------------------------------")

                except ValueError:
                    print("Elija un valor valido")
        # Termina el progra,a
        elif opcion == 8:
            print ("Gracias por usar nuestro servicio.")
            print ("---------------------------------------------------------------------")
            print ("FIN")
            break
        

    except ValueError:
        print("Elija un valor valido")
        print("---------------------------------------------------------------------")
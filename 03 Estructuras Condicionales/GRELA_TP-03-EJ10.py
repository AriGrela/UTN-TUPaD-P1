hemisferio = (input("En que hemisferio se encuentra? Ingrese n para Norte/ s para Sur: ")).lower()
dia_ano = int(input("Que dia es?: "))
mes_ano = int(input("Ingresa el mes (numero): "))

if hemisferio == "n":
    if (dia_ano >= 21 and mes_ano == 12) or mes_ano == 1 or mes_ano == 2 or (dia_ano <= 20 and mes_ano == 3):
        print ("Usted esta en Invierno")
    elif (dia_ano >= 21 and mes_ano == 3) or mes_ano == 4 or mes_ano == 5 or (dia_ano <= 20 and mes_ano == 6 ):
        print ("Usted esta en Primavera")
    elif (dia_ano >= 21 and mes_ano == 6) or mes_ano == 7 or mes_ano == 8 or (dia_ano <= 20 and mes_ano == 9 ):
        print ("Usted esta en Verano")
    elif (dia_ano >= 21 and mes_ano == 9) or mes_ano == 10 or mes_ano == 11 or (dia_ano <= 20 and mes_ano == 12 ):
        print ("Usted esta en Otoño")
elif hemisferio == "s":
   
    if (dia_ano >= 21 and mes_ano == 12) or mes_ano == 1 or mes_ano == 2 or (dia_ano <= 20 and mes_ano == 3):
        print("Usted esta en Verano")
    elif (dia_ano >= 21 and mes_ano == 3) or mes_ano == 4 or mes_ano == 5 or (dia_ano <= 20 and mes_ano == 6):
        print("Usted esta en Otoño")
    elif (dia_ano >= 21 and mes_ano == 6) or mes_ano == 7 or mes_ano == 8 or (dia_ano <= 20 and mes_ano == 9):
        print("Usted esta en Invierno")
    elif (dia_ano >= 21 and mes_ano == 9) or mes_ano == 10 or mes_ano == 11 or (dia_ano <= 20 and mes_ano == 12):
        print("Usted esta en Primavera")
else:
    print("Hemisferio no reconocido. Por favor, ingrese 'n' o 's'.")






    


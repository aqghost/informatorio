# Ejercicio: tenemos que ingresar por pantalla un string con la fecha en formato ISO, por ejemplo
# '20250505', identificar el mes en el que se encuentra (en este caso, mayo)

meses = {
    "01": "Enero",
    "02": "Febrero",
    "03": "Marzo",
    "04": "Abril",
    "05": "Mayo",
    "06": "Junio",
    "07": "Julio",
    "08": "Agosto",
    "09": "Septiembre",
    "10": "Octubre",
    "11": "Noviembre",
    "12": "Diciembre"
}
fecha = input('Ingresar la fecha en formato AAAAMMDD: ')
mes_ingresado=fecha[4:6]
if len(fecha) == 8:
    if mes_ingresado in meses:
        print(f"{meses[mes_ingresado]}")
    else:
        print("Fecha fuera de rango válido")
else:
    print("Formato de fecha invalido")
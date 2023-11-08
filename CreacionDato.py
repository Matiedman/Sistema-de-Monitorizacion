from easysnmp import snmp_get, snmp_walk

# Variables
tempIntValue = 0
humIntValue = 0

def getTemperature(sxFxRxpdu):

    #print("\nDatos de temperatura: ")

    # Se almacena el objeto, su tipo, que es OBJECT-TYPE -> Integer. Su acceso es de solo lectura.
    getInterfaceTempStauts = sxFxRxpdu.get('1.3.6.1.4.1.534.6.6.7.7.1.1.4.0.1')

    temperatureOID = getInterfaceTempStauts.oid                         # Se almacena el OID de la temperatura.
    dataTypeTempOID = getInterfaceTempStauts.snmp_type                  # Se almacena el tipo de dato que devuelve el OID.         
    tempValue = getInterfaceTempStauts.value                            # Se almacena el dato de la temperatura obtenido del OID
    objectType = type(getInterfaceTempStauts)                           # Guarda el tipo de dato que almacena la variable
    tempIntValue = (int(getInterfaceTempStauts.value))/10               # Se conviernte el dato a entero y luego lo divide por 10. 
    #print("Se registraron", tempIntValue,"ºC")

    return tempIntValue

def getHumedity(sxFxRxpdu):

    #print("\nDatos de humedad: ")

    # Se almacena el objeto, su tipo, que es OBJECT-TYPE -> Integer. Su acceso es de solo lectura.
    getInterfaceHumStauts = sxFxRxpdu.get('1.3.6.1.4.1.534.6.6.7.7.2.1.4.0.1')     
    humedityOID = getInterfaceHumStauts.oid                             # Se almacena el OID de la humedad.
    dataTypeHumOID = getInterfaceHumStauts.snmp_type                    # Se almacena el tipo de dato que devuelve el OID.         
    humValue = getInterfaceHumStauts.value                              # Se almacena el dato de la humedad obtenido del OID
    objectType = type(getInterfaceHumStauts)                            # Guarda el tipo de dato que almacena la variable
    humIntValue = (int(getInterfaceHumStauts.value))/10                 # Se conviernte el dato a entero y luego lo divide por 10. 
    #print("Se registró", humIntValue,"% de humedad")

    return humIntValue
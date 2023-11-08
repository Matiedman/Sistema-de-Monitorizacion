from easysnmp import Session, snmp_get, snmp_walk

import time, Configuraciones





 
def main():

    Configuraciones.pduDefinitions()
    Configuraciones.deviceConfigName()
    Configuraciones.tempHumeDataCreate()
    Configuraciones.sxFxRxKey_value()

    while 1:
        # Se muestran datos actualizados cada 10 seg.    
        Configuraciones.tempHumeDataCreate()
        Configuraciones.sxFxRxKey_value()         
        print(Configuraciones.SbF1KeyValueHume)
        print(Configuraciones.SbF1KeyValueTemp)
        time.sleep(10)
        print("------------------------------------\t")

if __name__ == '__main__':
    main()
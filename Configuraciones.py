from easysnmp import Session, snmp_get, snmp_walk

import CreacionDato


SApduRxSession = [] # Array de elementos de las diferentes sesiones de los PDU en los Rx del sector A. 
SBpduF1Session = [] # Array de elementos de las diferentes sesiones de los PDU de la fila 1 del sector B. 
SBpduF2Session = [] # Array de elementos de las diferentes sesiones de los PDU de la fila 2 del sector B. 

SaKeyValueTemp = {}     # Contiene los elementos que almacenan datos "llave-valor" respecto a la temperatura de los diferentes dispositivos según área.
SbF1KeyValueTemp = {}
SbF2KeyValueTemp = {}
SaKeyValueHume = {}     # Contiene los elementos que almacenan datos "llave-valor" respecto a la humedad de los diferentes dispositivos segun área.
SbF1KeyValueHume = {}
SbF2KeyValueHume = {}

saRxNameTemp = []        # Los siguientes elementos contienen los nombres de cada dispositivo según área para su temperatura y humedad.
sbF1RxpduNameTemp = []  
sbF2RxpduNameTemp = []

saRxNameHume = []
sbF1RxpduNameHume = []
sbF2RxpduNameHume = []

saRxPduDatoTemp = []    # Los siguientes elementos contienen los datos de temperatura y humedad correspondiente a cada dispositivo según área. 
sbF1RxPduDatoTemp = []
sbF2RxPduDatoTemp = []

saRxPduDatoHume = []
sbF1RXPduDatoHume = []
sbF2RXPduDatoHume = []

# Funcion que carga las sesiones de cada pdu segun rack, fila y sector del DC en distintas variables con nombre asociado  
# y luego en un array que los une por area y fila.  
def pduDefinitions():
    
    global SApduRxSession, SBpduF1Session, SBpduF2Session   # Esto indica que se hace referencia a la misma variable global antes declarada. 

    #-----------------------------------------------SECTOR A-------------------------------------------------------------#

    # En el sector A luego de debuggear han salido para todas sesiones el siguiente error:
        # easysnmp.exceptions.EasySNMPTimeoutError: timed out while connecting to remote host
    # excepto en las sesiones de los racks R2 y R3. Ver su tipo de error. 

    # saR1pduSession = Session(hostname='sar1pdu.psi.unc.edu.ar', community='publiceaton', version=1) 
    # -> Ver porque no funciona: saR2pduSession = Session(hostname='sar2pdu.psi.unc.edu.ar', community='publiceaton', version=1) 
    # -> Ver porque no funciona: saR3pduSession = Session(hostname='sar3pdu.psi.unc.edu.ar', community='publiceaton', version=1)
    # saR4pduSession = Session(hostname='sar4pdu.psi.unc.edu.ar', community='publiceaton', version=1) 
    # saR5pduSession = Session(hostname='sar5pdu.psi.unc.edu.ar', community='publiceaton', version=1) 
    # saR6pduSession = Session(hostname='sar6pdu.psi.unc.edu.ar', community='publiceaton', version=1)
  
    # SApduRxSession = [saR1pduSession, saR2pduSession, saR3pduSession, saR4pduSession, saR5pduSession, saR6pduSession]
    # Uuna vez reparado todos los erroes, descomentar las lineas y hacer el mismo procedimiento para probarlos. Debuggear. 
          

    #-----------------------------------------------SECTOR B-------------------------------------------------------------#
    sbF1R1pduSession = Session(hostname='sbf1r1pdu.psi.unc.edu.ar', community='publiceaton', version=1)
    # sbF1R2pduSession = Session(hostname='sbf1r2pdu.psi.unc.edu.ar', community='publiceaton', version=1)-> Arroja  easysnmp.exceptions.EasySNMPTimeoutError: timed out while connecting to remote host
    # sbF1R3pduSession = Session(hostname='sbf1r3pdu.psi.unc.edu.ar', community='publiceaton', version=1)-> Arroja  easysnmp.exceptions.EasySNMPTimeoutError: timed out while connecting to remote host
    sbF1R4pduSession = Session(hostname='sbf1r4pdu.psi.unc.edu.ar', community='publiceaton', version=1)
    sbF1R5pduSession = Session(hostname='sbf1r5pdu.psi.unc.edu.ar', community='publiceaton', version=1)

    # sbF2R1pduSession = Session(hostname='sbf2r1pdu.psi.unc.edu.ar', community='publiceaton', version=1)-> Arroja easysnmp.exceptions.EasySNMPTimeoutError: timed out while connecting to remote host
    # sbF2R2pduSession = Session(hostname='sbf2r2pdu.psi.unc.edu.ar', community='publiceaton', version=1)-> Arroja easysnmp.exceptions.EasySNMPTimeoutError: timed out while connecting to remote host
    # sbF2R3pduSession = Session(hostname='sbf2r3pdu.psi.unc.edu.ar', community='publiceaton', version=1)-> Arroja easysnmp.exceptions.EasySNMPTimeoutError: timed out while connecting to remote host
    # sbF2R4pduSession = Session(hostname='sbf2r4pdu.psi.unc.edu.ar', community='publiceaton', version=1)-> Arroja easysnmp.exceptions.EasySNMPTimeoutError: timed out while connecting to remote host
    # sbF2R5pduSession = Session(hostname='sbf2r5pdu.psi.unc.edu.ar', community='publiceaton', version=1)-> Arroja easysnmp.exceptions.EasySNMPTimeoutError: timed out while connecting to remote host

    SBpduF1Session = [sbF1R1pduSession, sbF1R4pduSession, sbF1R5pduSession]
    # SBpduF1Session = [sbF1R1pduSession, sbF1R2pduSession, sbF1R3pduSession, sbF1R4pduSession, sbF1R5pduSession]
    
    # SBpduF2Session = [sbF2R1pduSession, sbF2R2pduSession, sbF2R3pduSession, sbF2R4pduSession, sbF2R5pduSession]

    
    #-----------------------------------------------SECTOR C (en construccion)--------------------------------------------#
    #######################################################################################################################

# Creacion de diccionarios para almacenar los valores de temperatura y humedad como "Clave: Valor". 
def deviceConfigName():

    global saRxNameTemp, sbF1RxpduNameTemp, sbF2RxpduNameTemp, saRxNameHume, sbF1RxpduNameHume, sbF2RxpduNameHume

    # Lista de temperatura por area:
    # saRxNameTemp = ["saR1pdu", "saR2pdu", "saR3pdu", "saR4pdu", "saR5pdu", "saR6pdu"]   
    sbF1RxpduNameTemp = ["sbF1R1pduTemp", "sbF1R4pduTemp", "sbF1R5pduTemp"]  
    #sbF1RxpduNameTemp = ["sbF1R1pduTemp", "sbF1R2pduTemp", "sbF1R3pduTemp", "sbF1R4pduTemp", "sbF1R5pduTemp"]  
    # sbF2RxpduNameTemp = ["sbF2R1pduTemp", "sbF2R2pduTemp", "sbF2R3pduTemp", "sbF2R4pduTemp", "sbF2R5pduTemp"]

    # Lista de humedad por area:
    # saRxNameHume = ["saR1pduHume", "saR2pduHume", "saR3pduHume", "saR4pduHume", "saR5pduHume", "saR6pduHume"]
    sbF1RxpduNameHume = ["sbF1R1pduHum", "sbF1R4pduHum", "sbF1R5pduHum"]
    #sbF1RxpduNameHume = ["sbF1R1pduHum", "sbF1R2pduHum", "sbF1R3pduHum", "sbF1R4pduHum", "sbF1R5pduHum"]
    # sbF2RxpduNameHume = ["sbF2R1pduHum", "sbF2R2pduHum", "sbF2R3pduHum", "sbF2R4pduHum", "sbF2R5pduHum"]


# Creacion de los datos de temperatura y humedad:
def tempHumeDataCreate():

    # Creacion de los datos de temperatura:
    # for SaRx in SApduRxSession:
    #     saRxPduDatoTemp.append(CreacionDato.getTemperature(SaRx))          # Con el metodo append() se van agregando elementos al final de la lista. 
    
    for SbF1Rx in SBpduF1Session:
        sbF1RxPduDatoTemp.append(CreacionDato.getTemperature(SbF1Rx))      
    
    # for SbF2Rx in SBpduF2Session:
    #     sbF2RxPduDatoTemp.append(CreacionDato.getTemperature(SbF2Rx))     

    # Creacion de los datos de humedad:
    # for SaRx in SApduRxSession:
    #     saRxPduDatoHume.append(CreacionDato.getHumedity(SaRx))         
    
    for SbF1Rx in SBpduF1Session:
        sbF1RXPduDatoHume.append(CreacionDato.getHumedity(SbF1Rx))      
    
    # for SbF2Rx in SBpduF2Session:
    #     sbF2RXPduDatoHume.append(CreacionDato.getHumedity(SbF2Rx))   


# A partir de las listas anteriores creadas, seguidamente se harán diccionarios para manejar los valores segun el dispositivo (clave-valor). 
def sxFxRxKey_value():

    global SaKeyValueTemp, SbF1KeyValueTemp, SbF2KeyValueTemp, SaKeyValueHume, SbF1KeyValueHume, SbF2KeyValueHume

    # Contiene los elementos que almacenan datos "llave-valor" respecto a la temperatura de los diferentes dispositivos según área.
    # SaKeyValueTemp = {saRxNameTemp:saRxPduDatoTemp for (saRxNameTemp, saRxPduDatoTemp) in zip(saRxNameTemp, saRxPduDatoTemp)} 
    SbF1KeyValueTemp = {sbF1RxpduNameTemp:sbF1RxPduDatoTemp for (sbF1RxpduNameTemp, sbF1RxPduDatoTemp) in zip(sbF1RxpduNameTemp, sbF1RxPduDatoTemp)}
    # SbF2KeyValueTemp = {sbF2RxpduNameTemp:sbF2RxPduDatoTemp for (sbF2RxpduNameTemp, sbF2RxPduDatoTemp) in zip(sbF2RxpduNameTemp, sbF2RxPduDatoTemp)}
    
    # Contiene los elementos que almacenan datos "llave-valor" respecto a la humedad de los diferentes dispositivos segun área.
    # SaKeyValueHume = {saRxNameHume:saRxPduDatoHume for (saRxNameHume,saRxPduDatoHume) in zip(saRxNameHume, saRxPduDatoHume)}    
    SbF1KeyValueHume = {sbF1RxpduNameHume:sbF1RXPduDatoHume for (sbF1RxpduNameHume, sbF1RXPduDatoHume) in zip(sbF1RxpduNameHume, sbF1RXPduDatoHume)}
    # SbF2KeyValueHume = {sbF2RxpduNameHume:sbF2RXPduDatoHume for (sbF2RxpduNameHume, sbF2RXPduDatoHume) in zip(sbF2RxpduNameHume, sbF2RXPduDatoHume)}


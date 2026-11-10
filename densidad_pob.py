#Calculo de la densidad poblacional.
densidad_pob = 0

poblacion_total = 0

list_denpob = []

ageb_poblacion = QgsProject.instance().mapLayersByName("Ageb_SLP_Poblacion")[0]

print("Densidad poblacional....")

print("Densidad poblacional a nivel de Ageb.")

print(f"Nombre de la capa vectorial: {ageb_poblacion.name()}")

print("Datos de densidad poblacional calculados:")

def Densidad_poblacional():
    
    list_denpob.clear()
    
    for pobtotal in ageb_poblacion.getFeatures():
        
        pob_valor = pobtotal["POBTOT_INT"]
        
        area_valor = pobtotal["Area(km^2)"]
        
        if pob_valor is None or area_valor is None:
            
            densidad_pob = 0.0
            
            list_denpob.append(densidad_pob)
            
            print(densidad_pob)
            
        else:
            try:
                poblacion = int(pob_valor)
                area = float(area_valor)
                
                if area <= 0:
                    
                    densidad_pob = 0.0
                    
                    list_denpob.append(densidad_pob)
                    
                    print(densidad_pob)
                    
                else:
                    
                    densidad_pob = float(poblacion / area)
            
                    list_denpob.append(densidad_pob)
            
                    print(densidad_pob)
                    
            except (ValueError, TypeError):
                
                densidad_pob = 0.0
                
                list_denpob.append(densidad_pob)
                
                print("Ocurrio un error de conversión.")
        
    #Vaciar la lista en el campo de densidad poblacional. 
    
    ageb_poblacion.startEditing()
    print("Transferencia de datos al campo de densidad poblacional.")
    indice = ageb_poblacion.fields().indexFromName("DenPob")
    
    for ageb, denpob in zip(ageb_poblacion.getFeatures(), list_denpob):
        
        ageb_poblacion.changeAttributeValue(ageb.id(),indice,denpob)
    
    ageb_poblacion.commitChanges()
    
    print("Los datos fueron guardados con exito. ")
    
Densidad_poblacional()
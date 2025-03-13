from django.db import models
import oracledb

# Create your models here.
class Departamento: 
    numero = 0
    nombre = ""
    localidad = ""
    
class ServiceDepartamento:
    def __init__(self):
        self.connection = oracledb.connect(user='SYSTEM',password='oracle',dsn='localhost/xe')
    
    def insertDepartamento(self,numero,nombre,localidad):
        sql= "insert into DEPT values(:p1,:p2,:p3)"
        
        cursor=self.connection.cursor()
        cursor.execute(sql,(numero ,nombre,localidad))
        registros=cursor.rowcount
        self.connection.commit()
        cursor.close()
        return registros
    ##############################
    def deleteDepartamento(self,numero):
        sql= "delete into DEPT values(:p1,:p2)"
        
        cursor=self.connection.cursor()
        cursor.execute(sql,(numero))
        registros=cursor.rowcount
        self.connection.commit()
        cursor.close()
        return registros
            
    def getDepartamentos(self):
        sql="select * from DEPT"
        cursor = self.connection.cursor()
        cursor.execute(sql)
        lista=[]
        for row in cursor:
            dept= Departamento()
            dept.numero = row[0]
            dept.nombre = row[1]
            dept.localidad = row[2]
            lista.append(dept)
        cursor.close
        return lista
class Hospitales: 
    idhospital = 0
    nombre = ""
    direccion = ""
    
class ServiceHospital:
    def __init__(self):
        self.connection = oracledb.connect(user='SYSTEM',password='oracle',dsn='localhost/xe')
        
    def getHospitales(self):
        sql="select * from HOSPITAL"
        cursor = self.connection.cursor()
        cursor.execute(sql)
        lista=[]
        for row in cursor:
            hosp= Hospitales()
            hosp.idhospital = row[0]
            hosp.nombre = row[1]
            hosp.direccion = row[2]
            lista.append(Hospitales)
        cursor.close
        return lista
        
    

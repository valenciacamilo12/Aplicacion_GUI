#!/usr/bin/python3
from conectarDB import *

class Sentencias(Conexion):

	def insertar(self,officeCode,City,Phone,AddressLine1,AddressLine2,State,Country,PostalCode,Territory):
		cnx = self.conectar()
		cursor = cnx.cursor()
		sql = "INSERT INTO offices VALUES('"+officeCode+"','"+City+"','"+Phone+"','"+AddressLine1+"','"+AddressLine2+"','"+State+"','"+Country+"','"+PostalCode+"','"+Territory+"')"
		cursor.execute(sql)
		cnx.commit()
		self.cerrarConexion(cnx)
	
	def listar(self):
		cnx = self.conectar()
		cursor = cnx.cursor()
		sql = "SELECT * FROM offices"
		lista = []
		cursor.execute(sql)
		for (usuarios) in cursor:
			lista.append(usuarios)
		self.cerrarConexion(cnx)
		return lista


	def buscar(self,cadena):
		cnx = self.conectar()
		cursor = cnx.cursor()
		sql = "SELECT * FROM offices WHERE City LIKE '%"+str(cadena)+"%'"
		lista = []
		cursor.execute(sql)
		for (usuarios) in cursor:
			lista.append(usuarios)
		self.cerrarConexion(cnx)
		return lista


	def modificar(self,officeCode,City,Phone,AddressLine1,AddressLine2,State,Country,PostalCode,Territory):
		cnx = self.conectar()
		cursor = cnx.cursor()
		sql = "UPDATE offices SET City = '"+City+"' , Phone = '"+Phone+"' , AddressLine1 = '"+AddressLine1+"' , AddressLine2 = '"+AddressLine2+"' , State = '"+State+"' , Country = '"+State+"', PostalCode = '"+PostalCode+"' , Territory = '"+Territory+"' WHERE officeCode = '"+officeCode+"' "
		if self.verificar(officeCode) != 0:
			cursor.execute(sql)
			cnx.commit()
		self.cerrarConexion(cnx)



	def verificar(self,officeCode):
		cnx = self.conectar()
		cursor = cnx.cursor()
		sql = "SELECT * FROM offices WHERE officeCode = officeCode"
		try:
			result = cursor.execute(sql)
			resultado = cursor.fetchone()
				
			return resultado

		except ValueError:
			print ("**************************************")
			print ("ERROR AL INGRESAR DATOS")
			print ("**************************************")

		self.cerrarConexion(cnx)


	
	def eliminar(self,officeCode):
		cnx = self.conectar()
		cursor = cnx.cursor()
		sql = "DELETE FROM offices WHERE officeCode ="+str(officeCode)
		try:
			if self.verificar(officeCode) != 0:
				cursor.execute(sql)
				cnx.commit()

		except ValueError:
			print ("**************************************")
			print ("ERROR AL INGRESAR DATOS")
			print ("**************************************")

		self.cerrarConexion(cnx)
			

         
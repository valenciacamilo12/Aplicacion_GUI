#-*-coding:utf-8-*-
#!/usr/bin/python3

import pymysql

class Conexion():

	def conectar(self):
		try:
			self.conexion = pymysql.connect("localhost","root","123","classicmodels")
			return self.conexion

		except pymysql.InternalError as error:
			code, message = error.args
			print("ERROR: ", code, message)

	
	def cerrarConexion(self,conexion):
		print("Cerrando Conexion")
		self.conexion.close()
		print("Conexion Cerrada")
		
		
		







		
			
			  
			
		 

	
			

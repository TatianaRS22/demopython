# language: es

@pruebaEjemplo
Característica: Prueba Ejemplo
	Esto es solo una prueba

@pruebaEjemplo1
Escenario: Llenar informacion de contacto
	Dado que estoy en la pagina de contacto
  	Cuando lleno el campo de nombre con "<nombre>"
		Y lleno el campo de correo electronico con "prueba@gmail.com"
	Entonces lleno el campo de mensaje con "Esta es solo una prueba"

@pruebaEjemplo2
Escenario: Llenar informacion de trabaja con nosotros
	Dado que estoy en la pagina de trabaja con nosotros
  	Cuando lleno el campo de nombre de trabajo con "<nombre>"
	Entonces lleno el campo de mensaje

@pruebaEjemplo3
Escenario: Informacion de servicios
	Dado que estoy en la pagina de modalidad
  	Cuando se recorra la pagina
	Entonces vuelve al inicio

@pruebaEjemplo4
Escenario: Informacion de Chat
	Dado que estoy en la pagina de softesting
  	Cuando ingreso icono de chat
	Entonces lleno el chat mensaje

@pruebaEjemplo5
Escenario: Informacion de componentes servicios
	Dado que estoy en la pagina de componentes de servicio
  	Cuando se recorre la pagina de componentes

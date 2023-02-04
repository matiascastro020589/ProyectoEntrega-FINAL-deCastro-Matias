# ProyectoEntrega2

EL PROYECTO CONTIENE 

MODELS - 3 > CLIENTES / PRODUCTOS / VENDEDORES
EXISTEN 3 FORMULARIOS PARA INSERTAR NUEVOS DATOS A CADA UNO DE ESTOS. 
EXISTEN 3 FORMULARIOS DE BUSQUEDA TODOS UBICADOS EN LA MISMA RUTA DE BUSCADORES 
BUSCAR PRODUCTO POR PRECIO
BUSCAR CLIENTE POR NOMBRE
BUSCAR VENDEDOR POR NOMBRE

LISTADO > URLS >

admin/
AppCoder/ [name='Inicio'] *** PANTALLA DE INICIO - INFORMA CORRECTO LOGEO DE USUARIO
AppCoder/ acercade [name='Acerca de'] *** PANTALLA ACERCA DE LA WEB 
AppCoder/ buscadores [name='Buscadores'] *** BUSCADORES CREADOS PARA REALIZAR BUSQUEDAS SOBRE LAS 3 INSTANCIAS (PRODUCTOS, VENDEDORES Y CLIENTES)
AppCoder/ productos [name='Productos'] 	*** FORMULARIO PARA ALTA DE PRODUCTOS
AppCoder/ clientes [name='Clientes'] *** FORMULARIO PARA ALTA DE CLIENTES
AppCoder/ vendedores [name='Vendedores'] *** FORMULARIO PARA ALTA DE VENDEDORES
AppCoder/ producto/list [name='List'] *** LISTADO DE PRODUCTOS REGISTRADOS
AppCoder/ ^(?P<pk>\d+)$ [name='Detail'] *** VER DATOS DE LOS PRODUCTOS REGISTRADOS NOMBRE, Y PRECIO
AppCoder/ ^nuevo$ [name='New'] *** CREAR NUEVO REGISTRO DE PRODUCTO
AppCoder/ ^editar/(?P<pk>\d+)$ [name='Edit'] *** EDITAR REGISTRO DE PRODUCTO NOMBRE Y PRECIO
AppCoder/ ^borrar/(?P<pk>\d+)$ [name='Delete'] *** ELIMINAR REGISTRO DE PRODUCTO
AppCoder/ cliente/list [name='Listcliente'] *** LISTADO DE CLIENTES REGISTRADOS
AppCoder/ ^(?P<pk>\dcliente+)$ [name='Detailcliente'] *** VER DATOS DEL CLIENTE NOMBRE, APELLIDO E EMAIL, Y LOCALIDAD
AppCoder/ ^nuevocliente$ [name='Newcliente'] *** CREAR NUEVO REGISTRO DE CLIENTE
AppCoder/ ^editarcliente/(?P<pk>\d+)$ [name='Editcliente'] *** EDITAR REGISTRO DE CLIENTE - CAMBIAR NOMBRE, APELLIDO, EMAIL O LOCALIDAD
AppCoder/ ^borrarcliente/(?P<pk>\d+)$ [name='Deletecliente'] *** BORRAR REGISTRO DE CLIENTE
AppCoder/ vendedor/list [name='Listvendedor'] *** LISTADO DE VENDEDORES REGISTRADOS
AppCoder/ ^(?P<pk>\dvendedor+)$ [name='Detailvendedor'] *** VER DATOS DEL VENDEDOR NOMBRE, APELLIDO E EMAIL
AppCoder/ ^nuevovendedor$ [name='Newvendedor'] *** CREAR NUEVO REGISTRO DE VENDEDOR
AppCoder/ ^editarvendedor/(?P<pk>\d+)$ [name='Editvendedor'] *** EDITAR REGISTRO DE VENDEDOR - CAMBIAR NOMBRE, APELLIDO O EMAIL
AppCoder/ ^borrarvendedor/(?P<pk>\d+)$ [name='Deletevendedor'] *** BORRAR REGISTRO DE VENDEDOR
AppCoder/ login [name='Login'] *** PARA REGISTRAR EL INGRESO Y VALIDAR EL USUARIO PREVIAMENTE REGISTRARO
AppCoder/ register [name='Register'] *** REGISTRO DE NUEVO USUARIO 
AppCoder/ logout [name='Logout'] *** SALIR DE LA APP, DESLOGEANDO AL USUARIO
AppCoder/ editarPerfil [name='EditarPerfil'] *** PERMITE EDITAR EL PERFIL CON EL QUE SE ESTÁ LOGEADO

-------------


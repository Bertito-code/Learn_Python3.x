# Nombramos la clase con el nombre de la excepcion personalizada 
# Hacer referencia al tipo de excepcion que va a recoger
# Ponemos la classe padre Exception que es de la que sale el resto de excepciones

# Asi creariamos la clase personalizada pero sin un mensaje personalizado para la excepcion 
'''
class ExcepcionPersonalizada(Exception):
    pass
'''

# Se crea la clase para que nos pueda devolver mensajes personalizados la excepcion
class ExcepcionPersonalizada(Exception):
    def __init__ (self, mensaje):
        self.mensaje = mensaje
        
    

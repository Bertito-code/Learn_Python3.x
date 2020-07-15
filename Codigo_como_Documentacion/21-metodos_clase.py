
class Miclase:
    
    variable_clase = "Variable Clase"
    
    def __init__(self):
        # Si no se crea un objeto, la variable nunca se llama con lo cual no se crea la variable
        self.variable_instancia = "Variable Instancia"
    
    @staticmethod
    # Los metodos estaticos no reciben ningun parametro
    def metodo_estatico():
        print("Metodo Estatico")
        print(Miclase.variable_clase)
        # Desde un metodo estatico no podemos acceder a una variable de instancia
        # print(Miclase.variable_instancia)
        
    @classmethod
    # Los metodos de clase reciben un parametro, en este caso ponemos cls que hace referencia a la clase
    def metodo_clase(cls):
        print("Metodo de Clase: " + str(cls))    
        print(cls.variable_clase)
        # No podemos acceder a la variable de instancia desde contexto estatico
        # print(cls.variable_instancia)

    # Los metodos de instancia no tienen ningun decorador, 
    # es decir que se va poder asociar y ejecutar desde los objetos
    # Desde un metodo de instancia si es posible acceder 
    # a los metodos estaticos de clase o variable de clase
    def metodo_instancia(self):
        self.metodo_estatico()
        self.metodo_clase()
        print(self.variable_clase)
        print(self.variable_instancia)
        
# El contexto estatico no puede acceder al contexto dinamico, 
# pero el contexto dinamico si que puede accerder al contexto estatico       
Miclase.metodo_estatico()
Miclase.metodo_clase()

print()

objeto1 = Miclase()
objeto1.metodo_instancia()



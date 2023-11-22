class Cliente():
    def __init__(self,nombre,apellido,ci,direccion,telefono):
        self.nombre = nombre
        self.apellido = apellido
        self.ci =ci
        self.direccion=direccion
        self.telefono =telefono
    
    def show(self):
        print(f"""
    nombre: {self.nombre}
    apellido: {self.apellido}
    cedula: {self.ci}
    direccion: {self.direccion}
    telefono: {self.telefono}
    """)
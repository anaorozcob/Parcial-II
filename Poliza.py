class Poliza():
    def __init__(self,tipo,monto,fecha_inicio,fecha_vencimiento):
        self.tipo =tipo 
        self.monto = monto 
        self.fecha_inicio =fecha_inicio
        self.fecha_vencimiento =fecha_vencimiento

    def show(self):
                print(f"""
    tipo: {self.tipo}
    monto: {self.monto}
    fecha de inicio: {self.fecha_inicio}
    fecha de vencimiento : {self.fecha_vencimiento}
    """)
        


class Poliza_salud(Poliza):
    def __init__(self,tipo,monto,fecha_inicio,fecha_vencimiento,asegurados,suma,total):
        super().__init__("Salud",monto,fecha_inicio,fecha_vencimiento)
        self.asegurados = asegurados 
        self.suma = suma
        self.total =total

class Poliza_Automovil(Poliza):
    def __init__(self,tipo,monto,fecha_inicio,fecha_vencimiento,vehiculotype, marca,modelo,año,placa, total):
        super().__init__("Automovil",monto,fecha_inicio,fecha_vencimiento)
        self.vehiculotype = vehiculotype
        self.marca =marca
        self.modelo=modelo
        self.año=año
        self.placa=placa
        self.total = total
        

    
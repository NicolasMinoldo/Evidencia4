class MaquinaFabricacionAditiva:
    def __init__(self, modelo, estado, material_disponible, nivel_calibracion, material_necesario,
                 material_faltante):

        self.__modelo = modelo
        self.__estado = estado  # Puede ser "en espera", "en proceso", "pausado"
        self.__material_disponible = material_disponible
        self.__nivel_calibracion = nivel_calibracion
        self.__material_necesario = material_necesario
        self.__material_faltante = material_faltante


    def get_modelo(self):
        return self.__modelo

    def set_modelo(self, modelo):
        self.__modelo = modelo

    def get_estado(self):
        return self.__estado

    def set_estado(self,estado):
        self.__estado = estado

    def get_material_disponible(self):
        return self.__material_disponible

    def set_material_disponible(self, material_disponible):
        self.__material_disponible = material_disponible

    def get_nivel_calibracion(self):
        return self.__nivel_calibracion

    def set_nivel_decalibracion(self,nivel_calibracion):
        self.__nivel_calibracion = nivel_calibracion

    def get_material_necesario(self):
        return self.__material_necesario

    def set_material_necesario(self,material_necesario):
        self.__material_necesario = material_necesario

    def get_material_faltante (self):
        return self.__material_faltante

    def set_material_faltante(self,materiaL_faltante):
        self.__material_faltante = materiaL_faltante

    def iniciar_fabricacion(self):
        if self.__material_disponible >= self.__material_necesario:
            self.__estado = "en proceso"
            return True
        else:
            self.__estado = "en espera"
            return False

    def pausar_fabricacion(self):
        if self.__estado == "en espera":
            return 0
        else:
             self.__estado == "en proceso"
             return 1
    #
    def reabastecer_material(self):
        if self.__material_faltante == "Si":
            return "material disponible"
        elif self.__material_faltante == "No":
            return "material faltante"
        else:
            raise ValueError("Seleccione Si o No")

    def __str__(self):
        return f"Modelo: {self.__modelo}, Estado: {self.__estado}, Material Disponible: {self.__material_disponible}, " \
               f"Nivel de Calibración: {self.__nivel_calibracion}, Material Necesario: {self.__material_necesario}, " \
               f"Material Faltante: {self.__material_faltante}"


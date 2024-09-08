import pytest
from MaquinaFabricacionAditiva import MaquinaFabricacionAditiva

@pytest.mark.parametrize("valor1, valor2, resultado_esperado", [
    (100, 20, True),
    (50, 60, False)
])

def test_iniciar_la_fabricacion(valor1, valor2, resultado_esperado):
    mi_fabrica = MaquinaFabricacionAditiva(modelo="Cannon", estado="en proceso", material_disponible=valor1,
                                           nivel_calibracion=10, material_necesario=valor2,
                                           material_faltante="No")
    assert mi_fabrica.iniciar_fabricacion() == resultado_esperado

@pytest.mark.parametrize("valor,resultado_esperado",[
    ("en espera", 0),
    ("en proceso", 1)
])

def test_estado_de_fabricacion(valor, resultado_esperado):
    mi_estado= MaquinaFabricacionAditiva(modelo="Cannon", estado=valor, material_disponible= 100,
                                         nivel_calibracion=10, material_necesario=20,
                                         material_faltante="No")
    assert mi_estado.pausar_fabricacion() == resultado_esperado


@pytest.mark.parametrize("valor, resultado_esperado",[
    ("Si", "material disponible"),
    ("No", "material faltante")
])

def test_reabastecer_material(valor, resultado_esperado):
    mi_material= MaquinaFabricacionAditiva(modelo="Cannon", estado="en proceso",material_disponible=100,
                                           nivel_calibracion=10, material_necesario=20,
                                           material_faltante=valor)
    assert mi_material.reabastecer_material() == resultado_esperado


@pytest.mark.parametrize("Valor", ["Si", "No", "Talvez"])
def test_excepcion_restablecer_material(Valor):
            maquina = MaquinaFabricacionAditiva(modelo="Cannon", estado="en proceso",material_disponible=100,
                                           nivel_calibracion=10, material_necesario=20,
                                           material_faltante=Valor)
            if Valor not in ["Si", "No"]:
                with pytest.raises(ValueError, match="Seleccione Si o No"):
                    maquina.reabastecer_material()
            else:
                assert maquina.reabastecer_material() in ["material disponible", "material faltante"]


@pytest.mark.parametrize(
    "modelo, estado, material_disponible, nivel_calibracion, material_necesario,"
    " material_faltante, resultado_esperado",
    [
        ("Cannon", "en proceso", 100, 10, 20, "No",
         "Modelo: Cannon, Estado: en proceso, Material Disponible: 100,"
         " Nivel de Calibración: 10, Material Necesario: 20, Material Faltante: No"),
("Cannon", "en proceso", 100, 10, 20, "Si",
         "Modelo: Cannon, Estado: en proceso, Material Disponible: 100,"
         " Nivel de Calibración: 10, Material Necesario: 20, Material Faltante: Si"),
("Cannon", "en proceso", 100, 10, 20, "Talvez",
         "Modelo: Cannon, Estado: en proceso, Material Disponible: 100,"
         " Nivel de Calibración: 10, Material Necesario: 20, Material Faltante: Talvez")
    ])
def test_str_material(modelo, estado, material_disponible, nivel_calibracion, material_necesario, material_faltante,
                      resultado_esperado):
    mi_maquina = MaquinaFabricacionAditiva(modelo, estado, material_disponible, nivel_calibracion, material_necesario,
                                           material_faltante)

    resultado = str(mi_maquina)
    assert resultado == resultado_esperado
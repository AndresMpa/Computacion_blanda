from stages.get_info import get_info
from stages.analyze_info import analyze_info

states = {
    "1": get_info,
    "2": analyze_info,
}


def select_stage(stage: str):
    """
    Dado un estado del sistema regresa una funcion para ejecutar
    """
    return states.get(stage, "Error")

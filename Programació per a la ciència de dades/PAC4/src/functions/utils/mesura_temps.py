import timeit
from typing import Callable


def mesura_temps(funcio_a_mesurar: Callable) -> None:
    """
    Mesura el temps de processament d'una funció. Es fan
    2 repeticions i 3 execucions. S'obté el temps mínim.

    :param funcio_a_mesurar: La funció a mesurar.
    """
    t = timeit.Timer(funcio_a_mesurar)

    # Nombre d'execucions i repeticions
    num_executions = 3
    repetitions = 2

    temps_repetits = t.repeat(number=num_executions, repeat=repetitions)

    # arrodonim a 2 decimals
    temps_minim = round(min(temps_repetits), 2)
    print(f"Temps mínim: {temps_minim} segons, "
          f"després de {repetitions} repeticions amb "
          f"{num_executions} execucions cada una.")

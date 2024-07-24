import pandas as pd
import numpy as np
import concurrent.futures
from typing import Callable
from typing import Optional
import re


def filtrar_idioma_resum(df: pd.DataFrame) -> Optional[pd.DataFrame]:
    """
    Filtra les sèries del DataFrame per l'idioma 'en'
    i la presència de les paraules 'mystery' o 'crime' en el resum (overview).

    :param df: DataFrame a filtrar.
    :return: DataFrame filtrat o None si no hi ha cap sèrie que compleixi els criteris.
    """
    # Filtrem les sèries que compleixen els requisits
    series_filtrades = df[(df['original_language'] == 'en') &
                          (df['overview'].str.contains('mystery|crime', case=False, na=False))]

    # Mirem si el DataFrame resultant està buit
    if series_filtrades.empty:
        return None
    else:
        return series_filtrades


def filtrat_any_cancellada(df: pd.DataFrame, any: int) -> Optional[pd.DataFrame]:
    """
    Filtra les sèries del DataFrame que han començat en l'any especificat i han estat cancel·lades.

    :param df: DataFrame que conté les dades de les sèries.
    :param any: Any en què les sèries van començar.
    :return: Un nou DataFrame amb les sèries que compleixen ambdues condicions.
             Retorna None si no es troben sèries que compleixin els criteris.
    """
    # Fem servir coerce per a que si hi ha algun error en les dades la funció
    # pugui seguir, donant el valor Not a Time l'error.
    df['first_air_date'] = pd.to_datetime(df['first_air_date'], errors='coerce')
    # Normalitzem per eliminar possibles espais en blanc
    # o majúscules que no siguin la primera
    df['status'] = df['status'].str.strip().str.capitalize()

    # Filtrem per any i status cancel·lat
    series_filtrades = df[(df['first_air_date'].dt.year == any) & (df['status'] == "Canceled")]

    if series_filtrades.empty:
        return None
    else:
        return series_filtrades


# modificació de la funció 'filtrat_any_cancellada' per a mirar si hi ha errors a les dades
# es fa servir en l'exercici 4.
def filtrat_any(df: pd.DataFrame, any: int) -> Optional[pd.DataFrame]:
    """
    Filtra les sèries del DataFrame que han començat en l'any especificat.

    :param df: DataFrame que conté les dades de les sèries.
    :param any: Any en què les sèries van començar.
    :return: Un nou DataFrame amb les sèries que compleixen la condició.
             Retorna None si no es troben sèries que ho compleixin.
    """
    df['first_air_date'] = pd.to_datetime(df['first_air_date'], errors='coerce')

    # Filtrem per any
    series_filtrades = df[(df['first_air_date'].dt.year == any)]

    if series_filtrades.empty:
        return None
    else:
        return series_filtrades


def filtrar_idioma(df: pd.DataFrame, idioma: str) -> Optional[pd.DataFrame]:
    """
    Filtra les sèries del DataFrame basant-se en l'idioma especificat.
    Retorna un DataFrame amb les sèries que inclouen l'idioma especificat
    en les columnes 'original_language' o 'languages'.

    :param df: DataFrame que conté les dades de les sèries.
    :param idioma: L'idioma a filtrar, per exemple 'ja' per japonès.
    :return: DataFrame filtrat. Retorna None si no es troben dades.
    """
    # Regex per fer la busca
    regex_idioma = rf'\b{idioma}\b|\b\s{idioma},'

    # Filtrem
    series_filtrades = df[df['original_language'].str.contains(regex_idioma, flags=re.IGNORECASE, na=False) |
                          df['languages'].str.contains(regex_idioma, flags=re.IGNORECASE, na=False)]

    if series_filtrades.empty:
        return None
    else:
        return series_filtrades


def filtra_df_en_parallel(df: pd.DataFrame, funcio_filtratge: Callable[[pd.DataFrame], pd.DataFrame],
                          nombre_threads: int = 4) -> pd.DataFrame:
    """
    Filtra el DataFrame en paral·lel mitjançant threads.

    :param df: DataFrame original.
    :param funcio_filtratge: Funció de filtratge a aplicar a cada segment del DataFrame.
    :param nombre_threads: Nombre de threads a utilitzar (per defecte 4).
    :return: DataFrame filtrat.
    """
    # Dividim el dataframe
    segments = np.array_split(df, nombre_threads)

    # Utilitza ThreadPoolExecutor per processar cada segment en paral·lel
    # max_workers és el nombre màxim de fils a utilitzar a la vegada
    with concurrent.futures.ThreadPoolExecutor(max_workers=nombre_threads) as executor:
        resultats = executor.map(funcio_filtratge, segments)

    # Combinem els resultats
    return pd.concat(resultats)


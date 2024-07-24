import pandas as pd


def afegir_variable(df_temp: pd.DataFrame) -> pd.DataFrame:
    """
    Afegeix la variable 'air_days' al DataFrame especificat. Representa
    el nombre de dies que una sèrie ha estat en emissió. La funció accepta
    el DataFrame d'entrada i retorna un nou DataFrame amb aquesta columna afegida.

    :param df_temp: DataFrame que conté les columnes 'first_air_date'
                       i 'last_air_date'.
    :return: DataFrame amb la nova columna 'air_days' afegida.
    """

    df_temp['first_air_date'] = pd.to_datetime(df_temp['first_air_date'])
    df_temp['last_air_date'] = pd.to_datetime(df_temp['last_air_date'])

    # Calculem el nombre de dies en emissió
    df_temp['air_days'] = (
        df_temp['last_air_date'] - df_temp['first_air_date']
    ).dt.days

    return df_temp

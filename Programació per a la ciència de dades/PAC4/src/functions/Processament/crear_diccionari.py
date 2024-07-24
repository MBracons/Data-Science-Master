import pandas as pd


def crear_diccionari(df: pd.DataFrame) -> dict:
    """
    Crea un diccionari on cada clau és el nom original de la sèrie i el valor és
    la web completa del pòster, formada per la concatenació de 'homepage'
    i 'poster_path'. Si alguna de les dues és NaN, buida, o no és una cadena,
    el valor serà 'NOT AVAILABLE'.

    :param df: DataFrame que conté les columnes 'original_name', 'homepage', i 'poster_path'.
    :return: Diccionari amb el nom de la sèrie com a clau i l'adreça del pòster com a valor.
    """
    diccionari_posters = {}

    for index, row in df.iterrows():
        nom_serie = row['name']
        homepage = row['homepage']
        poster_path = row['poster_path']

        # Comprovem si 'homepage' i 'poster_path' són cadenes vàlides
        if isinstance(homepage, str) and homepage.strip() and isinstance(poster_path, str) and poster_path.strip():
            diccionari_posters[nom_serie] = homepage + poster_path
        else:
            diccionari_posters[nom_serie] = "NOT AVAILABLE"

    return diccionari_posters

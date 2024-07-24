import os
import pandas as pd
import csv

def llegir_to_df(path: str) -> pd.DataFrame:
    """
    Llegeix tots els arxius CSV en el directori especificat i
    els fusiona en un únic DataFrame utilitzant la columna 'id'.

    :param path: Directori de la carpeta on es troben els arxius CSV.
    :return: DataFrame combinat amb totes les columnes dels CSV.
    """
    # Ho fem servir per mirar si és el primer que llegim
    df_final = None

    for filename in os.listdir(path):
        # mirem els arxius que acaben en '.csv'
        if filename.endswith('.csv'):
            file_path = os.path.join(path, filename)
            df_actual = pd.read_csv(file_path)

            if df_final is None:
                # És el primer
                df_final = df_actual
            else:
                # No és el primer, fem merge
                # outer perquè ho faci encara que no hi hagi coincidències
                df_final = pd.merge(df_final, df_actual, on='id', how='outer')
                df_final = df_final.drop_duplicates(subset='id')

    return df_final



def llegir_to_dict(path: str) -> dict:
    """
    Llegeix tots els arxius CSV en el directori especificat i
    els fusiona en un únic diccionari utilitzant la clau 'id'.

    :param path: Directori de la carpeta on hi ha els CSV.
    :return: Diccionari resultant.
    """
    diccionari = {}

    for filename in os.listdir(path):
        if filename.endswith('.csv'):
            file_path = os.path.join(path, filename)
            with open(file_path, mode='r') as file:
                reader = csv.DictReader(file)

                for row in reader:
                    id_clau = row['id']
                    if id_clau not in diccionari:
                        diccionari[id_clau] = row

    return diccionari

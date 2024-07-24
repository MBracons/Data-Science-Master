import pandas as pd
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from typing import Optional


def grafic_any(df: pd.DataFrame) -> Optional[plt.Figure]:
    """
    Genera un gràfic de barres que mostra el nombre de sèries per any d'inici.

    :param df: DataFrame que conté les dades de les sèries, incloent-hi la columna 'first_air_date'.
    :return: Un gràfic de barres mostrat a la pantalla.
    """
    df['first_air_date'] = pd.to_datetime(df['first_air_date'], errors='coerce')
    df['start_year'] = df['first_air_date'].dt.year

    # Comptem el nombre de sèries per any
    series_per_any = df['start_year'].value_counts().sort_index()

    # Creem un gràfic de barres
    plt.figure(figsize=(12, 6))
    series_per_any.plot(kind='bar')
    plt.title("Nombre de Sèries per Any d'Inici")
    plt.xlabel("Any d'Inici")
    plt.ylabel("Nombre de Sèries")
    plt.show()


def grafic_type(df: pd.DataFrame, any_inicial: int = 1940) -> None:
    """
    Genera un gràfic de línies mostrant el nombre de sèries de cada categoria de la variable "type"
    produïdes a cada dècada des de l'any especificat.

    :param df: DataFrame que conté les dades de les sèries.

    :param any_inicial: Any inicial des del qual es volen analitzar les dades.
                        Per defecte és 1940.
    """
    df['first_air_date'] = pd.to_datetime(df['first_air_date'])
    df['decada'] = (df['first_air_date'].dt.year // 10) * 10

    # Filtrem
    df = df[df['decada'] >= any_inicial]

    # Agrupem per type i dècada
    comptatge_series = df.groupby(['type', 'decada']).size().unstack(fill_value=0)

    # Generem el gràfic
    comptatge_series.T.plot(kind='line', marker='o')
    plt.title(f"Nombre de Sèries per Tipus i Dècada des de {any_inicial}")
    plt.xlabel("Dècada")
    plt.ylabel("Nombre de Sèries")
    plt.legend(title="Tipus de Sèrie")
    plt.show()


def grafic_genres(dades: pd.DataFrame) -> None:
    """
    Genera un gràfic circular mostrant el percentatge de sèries per gènere.
    Els gèneres que representen menys de l'1% són agrupats en una categoria "Altres".
    Només els segments amb més d'un 5% del total inclouen etiquetes dins del gràfic.
    """
    dades_genres = dades['genres'].dropna().str.split(',').explode()
    comptatge_genres = dades_genres.value_counts()
    percentatges = comptatge_genres / comptatge_genres.sum() * 100
    altres = percentatges[percentatges < 1].sum()
    percentatges = percentatges[percentatges >= 1]
    percentatges['Altres'] = altres

    # Definim quins segments s'han de separar (explode) i etiquetar
    explode = [0.1 if value < 1 else 0.0 for value in percentatges]
    labels = [label if percent > 5 else '' for label, percent in percentatges.items()]

    # Generem el gràfic
    plt.figure(figsize=(10, 8))
    wedges, texts, autotexts = plt.pie(percentatges, labels=labels, autopct='%1.1f%%',
                                       startangle=140, explode=explode, pctdistance=0.85)

    # Ajustem la font perquè es vegi bé el gràfic
    for text, autotext in zip(texts, autotexts):
        text.set_fontsize(8)
        autotext.set_fontsize(8)

    plt.legend(wedges, percentatges.index, title="Gèneres", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))
    plt.title("Percentatge de Sèries per Gènere")
    plt.axis("equal")

    plt.show()

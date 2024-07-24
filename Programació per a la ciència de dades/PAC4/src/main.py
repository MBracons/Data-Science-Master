from functions.DescompressioLectura.descomprimir import descomprimir
from functions.DescompressioLectura.llegir import llegir_to_df, llegir_to_dict
from functions.utils.mesura_temps import mesura_temps
from functions.Processament.afegir_variable import afegir_variable
from functions.Processament.crear_diccionari import crear_diccionari
from functions.Filtratge.filtrar import filtrar_idioma, filtrar_idioma_resum, \
                                        filtrat_any, filtrat_any_cancellada, \
                                        filtra_df_en_parallel
from functions.Visualitzacio.grafics import grafic_type, grafic_any, grafic_genres

import sys
import warnings
warnings.filterwarnings('ignore', category=FutureWarning)
exercicis_executats = [False, False, False, False]


def exercici_1():
    global df_1_2
    print("EXERCICI 1: DESCOMPRESSIÓ I LECTURA DE FITXERS")

    print("\nExercici 1.1:")
    # ".." per pujar un nivell en els directoris
    ruta_zip = "../TMDB.zip"
    ruta_desti = ".."
    descomprimir(ruta_zip, ruta_desti)

    print("\nExercici 1.2:")
    df_1_2 = llegir_to_df('..')

    nombre_files_df_1_2 = len(df_1_2)
    print(f"El DataFrame té {nombre_files_df_1_2} files.\n")
    print("El temps de processament ha sigut de :")
    mesura_temps(lambda: llegir_to_df('..'))

    print("\nExercici 1.3:")
    diccionari_1_3 = llegir_to_dict('..')
    nombre_claus_dict_1_3 = len(diccionari_1_3)
    print(f"El diccionari té {nombre_claus_dict_1_3} claus.\n")
    print("El temps de processament ha sigut de :")
    mesura_temps(lambda: llegir_to_dict('..'))

    print("\nExercici 1.4:")
    print(
        "La funció que utilitza dataframes és més lenta, però ens dona facilitats per\n"
        "analitzar i operar amb les dades del dataframe.\n"
        "La funció que utilitza el diccionari és més ràpida, fent que sigui millor per\n"
        "a gestionar fitxers de una gran mida (com 10GB).\n"
        "Crec que la millor opció seria combinar els documents amb diccionaris i\n"
        "posteriorment si es vol fer un anàlisi, transformar-lo en un dataframe.\n"
    )


def exercici_2():
    global df_2_1
    print("\nEXERCICI 2: PROCESSAMENT DE DADES")

    print("\nExercici 2.1:")

    df_2_1 = afegir_variable(df_1_2)

    # Ordenem df_2_1 per 'air_days' en ordre descendent
    df_2_1_sorted = df_2_1.sort_values(by='air_days', ascending=False)
    top_10_air_days = df_2_1_sorted[['id', 'name', 'air_days']].head(10)
    print("Les 10 series amb més dies en emissió són:\n")
    print(top_10_air_days)

    print("\nExercici 2.2:")
    # Apliquem la funció al dataframe
    diccionari_posters = crear_diccionari(df_2_1)
    print("Els 5 primers posters són:\n")
    for name, poster in list(diccionari_posters.items())[:5]:
        print(f"{name}: {poster}")


def exercici_3():
    print("\nEXERCICI 3: FILTRATGE DE DADES")

    print("\nExercici 3.1:")
    df_filtrat = filtra_df_en_parallel(df_1_2, filtrar_idioma_resum)
    print("Les sèries que compleixen els requisits d'idioma original i resum són:")
    if df_filtrat is not None:
        print(df_filtrat[['name']])
    else:
        print("No s'han trobat sèries que compleixin els criteris")

    print("\nExercici 3.2:")
    data_any = 2023
    df_filtrat = filtrat_any_cancellada(df_1_2, data_any)
    print(f"Les sèries que han començat el {any} i s'han cancel·lat són:\n")

    if df_filtrat is not None:
        print(df_filtrat['original_name'].head(20))
    else:
        print("No s'han trobat sèries que compleixin els criteris.")

    print("\nExercici 3.3:")
    idioma = 'ja'
    df_filtrat = filtrar_idioma(df_1_2, idioma)
    print(f"Les sèries en idioma <{idioma}> són:\n")

    if df_filtrat is not None:
        print(df_filtrat[['name', 'original_name', 'networks', 'production_companies']].head(20))
    else:
        print("No s'han trobat sèries que compleixin els criteris.")


def exercici_4():
    print("\nEXERCICI 4: ANÀLISI GRÀFICA")

    print("\nExercici 4.1:")
    print("Avís: Tancar figura per seguir amb l'execució")
    grafic_any(df_1_2)

    print("\nObservem que hi ha un fet interessant:"
          "\n- Hi ha series per més enllà de 2024")
    print("\nHi ha un possible error en la sèrie:")
    print(filtrat_any(df_1_2, 2029)[['name', 'first_air_date']])

    print("\nExercici 4.2:")
    print("Avís: Tancar figura per seguir amb l'execució")
    grafic_type(df_1_2)

    print("\nExercici 4.3:")
    print("Avís: Tancar figura per seguir amb l'execució")
    grafic_genres(df_1_2)


def exercici_aux():
    global df_1_2
    df_1_2 = llegir_to_df('..')


def comprova_exercicis_anteriors(num):
    return all(exercicis_executats[:num])


if __name__ == "__main__":
    if len(sys.argv) > 1:
        exercici = sys.argv[1]
        if exercici == '1':
            exercici_1()
        elif exercici == '2':
            exercici_aux()
            exercici_2()
        elif exercici == '3':
            exercici_aux()
            exercici_3()
        elif exercici == '4':
            exercici_aux()
            exercici_4()
        else:
            print("Argument incorrecte. Executant tot el programa.")
            exercici_1()
            exercici_2()
            exercici_3()
            exercici_4()
    else:
        exercici_1()
        exercici_2()
        exercici_3()
        exercici_4()

import zipfile
import tarfile

# Funció adaptada de l'exercici 2 de la PAC2
def descomprimir(ruta_fitxer: str, ruta_desti: str) -> None:
    """
    Descomprimeix un fitxer .zip o tar.gz a la ruta de destinació
    especificada.

    Args:
    ruta_fitxer (str): La ruta del fitxer a descomprimir
    ruta_desti (str): La ruta de destinació on es descomprimiran els arxius

    Returns:
    None
    """
    if ruta_fitxer.endswith('.zip'):
        with zipfile.ZipFile(ruta_fitxer, 'r') as zip_fitxer:
            zip_fitxer.extractall(ruta_desti)
            print('Fitxer descomprimit correctament.')
    elif ruta_fitxer.endswith('.tar.gz'):
        with tarfile.open(ruta_fitxer, 'r:gz') as tar_fitxer:
            tar_fitxer.extractall(ruta_desti)
            print('Fitxer descomprimit correctament.')
    else:
        print("Format no suportat. Només es poden descomprimir fitxers .zip i .tar.gz.")

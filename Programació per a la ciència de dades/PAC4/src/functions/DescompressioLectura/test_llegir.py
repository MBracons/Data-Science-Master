import unittest
import tempfile
import shutil
import csv
import os
from llegir import llegir_to_df, llegir_to_dict


class TestLecturaFuncions(unittest.TestCase):

    def setUp(self):
        # Directori temporal
        self.directori_temporal = tempfile.mkdtemp()

        # Crear fitxers CSV de prova
        self.crear_csv_prova('test1.csv')
        self.crear_csv_prova('test2.csv')

    def tearDown(self):
        # Neteja el directori temporal
        shutil.rmtree(self.directori_temporal)

    # Omplim el CSV amb id de 1 a 5, repetint l'1 dos cops.
    def crear_csv_prova(self, nom_fitxer):
        ruta_fitxer = os.path.join(self.directori_temporal, nom_fitxer)
        with open(ruta_fitxer, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['id'])
            for i in range(1, 6):
                writer.writerow([i])
                if i == 1:  # Repetim l'ID 1
                    writer.writerow([i])

    def test_llegir_to_df(self):
        df_resultat = llegir_to_df(self.directori_temporal)
        self.assertEqual(len(df_resultat), 5)  # Esperem 5 files úniques

    def test_llegir_to_dict(self):
        dict_resultat = llegir_to_dict(self.directori_temporal)
        self.assertEqual(len(dict_resultat), 5)  # Esperem 5 entrades úniques


if __name__ == '__main__':
    unittest.main()

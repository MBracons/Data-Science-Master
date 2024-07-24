from descomprimir import descomprimir
import os
import tarfile
import unittest
import tempfile
import shutil

class TestDescomprimir(unittest.TestCase):

    # https://docs.python.org/3.8/library/unittest.html#unittest.TestCase.debug
    def setUp(self):
        # directori temporal per generar fitxers
        self.directori_temporal = tempfile.mkdtemp()

    def tearDown(self):
        # Neteja el directori temporal després de cada test
        shutil.rmtree(self.directori_temporal)

    def test_descomprimir_tar_gz(self):
        # Creem fitxers csv
        ruta_csv1 = os.path.join(self.directori_temporal, "test1.csv")
        ruta_csv2 = os.path.join(self.directori_temporal, "test2.csv")
        open(ruta_csv1, 'a').close()
        open(ruta_csv2, 'a').close()

        # els comprimim
        ruta_fitxer_prova = os.path.join(self.directori_temporal, "prova.tar.gz")
        with tarfile.open(ruta_fitxer_prova, "w:gz") as tar:
            tar.add(ruta_csv1, arcname="test1.csv")
            tar.add(ruta_csv2, arcname="test2.csv")

        # Descomprimim el fitxer
        descomprimir(ruta_fitxer_prova, self.directori_temporal)

        # Comprovem si els fitxers descomprimits existeixen
        self.assertTrue(os.path.exists(os.path.join(self.directori_temporal, "test1.csv")))
        self.assertTrue(os.path.exists(os.path.join(self.directori_temporal, "test2.csv")))

if __name__ == '__main__':
    unittest.main()
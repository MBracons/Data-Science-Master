from filtrar import filtrar_idioma_resum, filtrat_any_cancellada, filtrar_idioma
import unittest
import pandas as pd

class TestFiltratgeSeries(unittest.TestCase):

    def test_filtrar_idioma_resum(self):
        # Creació df de testing
        data_test1 = {
            'original_language': ['en', 'en', 'en', 'en', 'cat', 'cat', 'cat', 'cat'],
            'overview': ['mystery', 'crime', 'mystery crime', 'hola', 'mystery', 'crime', 'mystery crime', 'hola']
        }
        df_test1 = pd.DataFrame(data_test1)


        # filtrem amb la funció
        result = filtrar_idioma_resum(df_test1)

        # Si tot va bé hauria de tindre 3 entrades
        self.assertIsNotNone(result)
        self.assertEqual(len(result), 3)

    def test_filtrat_any_cancellada(self):
        # Df testing
        data_test2 = {
            'name': ['Panda Vision', 'Transformers: el lado oscuro de Attention', 'House of Keras', 'Pytorchic'],
            'first_air_date': ['2024-03-02', '2024-03-02', '2020-03-02', '2020-03-02'],
            'status': ['Canceled', 'hola', 'Canceled', 'hola']
        }
        df_test2 = pd.DataFrame(data_test2)

        # Filtrem per any = 2024
        result = filtrat_any_cancellada(df_test2, 2024)

        # Hauria de tindre 1 registre
        self.assertIsNotNone(result)
        self.assertEqual(len(result), 1)

    def test_filtrar_idioma(self):
        # Df testing
        data_test3 = {
            'name': ['Gerardo de Revilla y su caballo Maravilla', 'I hate portals', 'Gerardo el magias'],
            'original_language': ['cat', 'esp', 'en'],
            'languages': ['cat esp', 'esp cat', 'en pl']
        }
        df_test3 = pd.DataFrame(data_test3)

        # Filtrem per idioma 'cat'
        result = filtrar_idioma(df_test3, 'cat')

        # Hauria d'haver 2 registres
        self.assertIsNotNone(result)
        self.assertEqual(len(result), 2)

if __name__ == '__main__':
    unittest.main()
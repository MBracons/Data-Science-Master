import unittest
import pandas as pd
from crear_diccionari import crear_diccionari

class TestCrearDiccionari(unittest.TestCase):

    def test_crear_diccionari(self):
        # Df testing
        data_test = {
            'name': ['Shrek', 'Shrik', 'Shroc'],
            'homepage': ['img.fruugo.com', 'Capybara', ''],
            'poster_path': ['/product/2/43/14581432_max.jpg', '', 'Chihuahua']
        }
        df_test = pd.DataFrame(data_test)

        # Executem la funció
        result = crear_diccionari(df_test)

        # Comprovem que el diccionari té el contingut esperat
        self.assertEqual(len(result), 3)
        self.assertEqual(result['Shrek'], 'img.fruugo.com/product/2/43/14581432_max.jpg')
        self.assertEqual(result['Shrik'], 'NOT AVAILABLE')
        self.assertEqual(result['Shroc'], 'NOT AVAILABLE')

if __name__ == '__main__':
    unittest.main()
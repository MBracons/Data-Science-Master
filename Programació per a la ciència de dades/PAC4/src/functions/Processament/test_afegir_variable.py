import unittest
import pandas as pd
from afegir_variable import afegir_variable

class TestAfegirVariable(unittest.TestCase):

    def test_afegir_variable(self):
        # Df testintg
        data_test = {
            'name': ['baldurs gate 3'],
            'first_air_date': ['1992-03-02'],
            'last_air_date': ['1992-03-03']
        }
        df_test = pd.DataFrame(data_test)

        result = afegir_variable(df_test)

        # Hauria de donar 1
        self.assertIn('air_days', result.columns)
        self.assertEqual(result.loc[0, 'air_days'], 1)

if __name__ == '__main__':
    unittest.main()

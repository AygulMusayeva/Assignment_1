import Task_4
import unittest
from io import StringIO
from unittest.mock import patch
from random import choice

class TestMainFunction(unittest.TestCase):
    
    @patch('builtins.input', side_effect=["3", "4", "5"])
    def test_main_input_calls(self, mock_input):
        Task_4.main() 
        expected_calls = ["Side 1: ", "Side 2: ", "Side 3: "]
        # Check if input was called with the expected arguments
        self.assertEqual(mock_input.call_args_list, [unittest.mock.call(arg) for arg in expected_calls])

    def _test_with_input(self, input_value, expected_output):
        with patch('builtins.input', side_effect=input_value), \
             patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            Task_4.main()
        self.assertEqual(mock_stdout.getvalue(), expected_output)
 
    def test_input(self):
        data = [[13, 11, 19, '69.26'], [14, 8, 13, '51.17'], [12, 9, 6, '26.14'], [8, 10, 3, '9.92'], [3, 15, 14, '20.40'], [19, 13, 14, '90.99'], [14, 19, 6, '26.91'], [9, 10, 8, '34.20'], [18, 10, 17, '83.43'], [9, 12, 15, '54.00'], [17, 7, 11, '24.44'], [11, 18, 17, '90.99'], [19, 18, 5, '44.90'], [9, 8, 7, '26.83'], [17, 7, 11, '24.44'], [20, 11, 18, '98.36'], [4, 16, 19, '23.00'], [12, 17, 6, '23.53'], [10, 16, 19, '79.99'], [4, 14, 14, '27.71'], [17, 16, 19, '127.98'], [12, 17, 8, '43.52'], [7, 3, 5, '6.50'], [14, 10, 6, '25.98'], [11, 16, 8, '40.26'], [10, 9, 5, '22.45'], [8, 14, 9, '33.67'], [13, 13, 16, '81.98'], [9, 14, 18, '61.89'], [13, 5, 11, '26.89'], [9, 8, 16, '22.93'], [13, 12, 20, '74.91'], [3, 9, 11, '11.05'], [15, 9, 11, '49.16'], [15, 9, 7, '20.69'], [11, 17, 13, '71.50'], [17, 15, 14, '99.68'], [8, 16, 18, '63.99'], [12, 5, 13, '30.00'], [9, 14, 12, '53.51'], [16, 20, 6, '39.69'], [12, 15, 12, '70.26'], [18, 11, 15, '82.32'], [9, 10, 14, '44.84'], [18, 17, 14, '111.99'], [11, 19, 16, '87.91'], [5, 10, 6, '11.40'], [8, 18, 20, '71.94'], [17, 20, 12, '101.67'], [14, 19, 8, '49.98'], [15, 13, 16, '91.19'], [16, 8, 19, '63.17'], [4, 5, 7, '9.80'], [18, 16, 10, '79.60'], [14, 9, 19, '59.40'], [13, 14, 9, '56.92'], [18, 15, 14, '102.16'], [6, 11, 16, '21.83'], [11, 17, 17, '88.47'], [10, 9, 4, '17.98'], [16, 12, 13, '76.69'], [7, 7, 2, '6.93'], [18, 16, 5, '38.53'], [7, 8, 8, '25.18'], [18, 3, 18, '26.91'], [8, 7, 12, '26.91'], [12, 10, 9, '44.04'], [19, 17, 13, '107.81'], [17, 16, 3, '23.24'], [15, 15, 14, '92.87'], [15, 3, 14, '20.40'], [8, 6, 3, '7.64'], [12, 11, 4, '21.93'], [17, 17, 18, '129.80'], [9, 8, 5, '19.90'], [3, 11, 9, '11.05'], [12, 13, 9, '52.15'], [8, 12, 10, '39.69'], [20, 12, 12, '66.33'], [15, 13, 13, '79.64'], [20, 14, 16, '111.24'], [12, 20, 15, '89.67'], [14, 14, 14, '84.87'], [14, 16, 15, '96.56'], [4, 13, 16, '19.00'], [5, 13, 15, '31.56'], [14, 20, 14, '97.98'], [11, 9, 4, '16.97'], [15, 20, 16, '118.28'], [16, 15, 11, '79.37'], [8, 9, 4, '16.00'], [10, 9, 6, '26.66'], [17, 13, 10, '64.81'], [14, 20, 11, '74.15'], [10, 12, 19, '52.39'], [19, 10, 12, '52.39'], [12, 8, 14, '47.91'], [16, 13, 8, '51.68'], [20, 9, 15, '63.28'], [20, 15, 12, '89.67']]
        sample = choice(list(data))
        print(sample)
        expected_output = f"Area of triangle: {float(sample[3]):.2f}\n"
        self._test_with_input(sample[:3], expected_output)

    def test_invalid_input(self):
        with patch('builtins.input', side_effect=["a", "b", "c"]), \
             self.assertRaises(ValueError):
            Task_4.main()
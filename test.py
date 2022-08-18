import unittest
from io import StringIO
import main
import unittest.mock
from unittest import mock


class Testing(unittest.TestCase):
    @unittest.mock.patch('sys.stdout', new_callable=StringIO)
    def test_replace_task(self, mock_stdout):
        test_data_1 = """5 6
        2 5 4 1 3
        4 4
        1 5
        1 4
        3 5
        4 5
        2 3"""

        test_data_2 = """6 3
        2 3 4 6 1 2
        5 6
        2 5
        2 3
        """

        test_data_3 = """1 1
        1
        1 1
        """

        test_data_4 = """10 10
        1 9 7 6 2 4 7 8 1 3
        10 10
        3 5
        6 7
        1 10
        6 6
        3 3
        6 7
        2 2
        4 9
        1 9"""


        expected_data_1 = """-1
        0
        1
        2
        3
        4"""

        expected_data_2 = """5
        1
        3
        """

        expected_data_3 = 0

        expected_data_4 = """-1
        -1
        -1
        0
        -1
        -1
        -1
        -1
        -1
        -1"""

        for time in range(1, 5):
            with mock.patch('builtins.input', side_effect=eval('test_data_'+str(time)).split('\n')):
                main.start_point()

                self.assertEqual(list(map(int, mock_stdout.getvalue().split())), list(map(int, str(eval('expected_data_' + str(time))).split())))

                mock_stdout.truncate(0)
                mock_stdout.seek(0)

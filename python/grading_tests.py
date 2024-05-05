# DO NOT CHANGE THIS FILE
import unittest

import app
import parser


class Phase1TestCases(unittest.TestCase):

    def test_1(self):
        input_values = "20 20 5 14 21 7 18 14 11 14 11 4 19 12 32 19"
        output = app.ParserOutput()

        parser.parse(input_values, output)

        self.assertEqual(2, len(output.output))
        self.assertEqual(-11, output.output[0])
        self.assertEqual(21, output.output[1])

    def test_2(self):
        input_values = "20 10 11 4 20 40 9 0 11 0 19"
        output = app.ParserOutput()

        parser.parse(input_values, output)

        self.assertEqual(1, len(output.output))
        self.assertEqual(31, output.output[0])

    def test_3(self):
        input_values = "19"
        output = app.ParserOutput()

        parser.parse(input_values, output)

        self.assertEqual(0, len(output.output))

    def test_4(self):
        input_values = "11 1 11 2 11 3 11 4 11 5 19"
        output = app.ParserOutput()

        parser.parse(input_values, output)

        self.assertEqual(5, len(output.output))
        self.assertEqual(1, output.output[0])
        self.assertEqual(11, output.output[1])
        self.assertEqual(2, output.output[2])
        self.assertEqual(11, output.output[3])
        self.assertEqual(3, output.output[4])


class Phase2TestCases(unittest.TestCase):

    def test_1(self):
        input_values = "30 a 3 30 a 5 30 b 4 30 b 9 31 a 22 31 b 22 31 a 23 20 -1 -1 0 11 0 19"
        output = app.ParserOutput()

        parser.parse(input_values, output)

        self.assertEqual(1, len(output.output))
        self.assertEqual(12, output.output[0])

    def test_2(self):
        input_values = "30 a 3 30 b 5 30 b 4 20 b a 0 11 0 19"
        output = app.ParserOutput()

        parser.parse(input_values, output)

        self.assertEqual(1, len(output.output))
        self.assertEqual(7, output.output[0])

    def test_3(self):
        input_values = "30 a 5 30 a 8 30 a 128 11 a 19"
        output = app.ParserOutput()

        parser.parse(input_values, output)

        self.assertEqual(1, len(output.output))
        self.assertEqual("128 8 5", output.output[0])

    def test_4(self):
        input_values = "30 x 1 30 x 32 21 x x 0 11 0 19"
        output = app.ParserOutput()

        parser.parse(input_values, output)

        self.assertEqual(1, len(output.output))
        self.assertEqual(31, output.output[0])

    def test_5(self):
        input_values = "30 j 14 21 j 5 0 11 0 19"
        output = app.ParserOutput()

        parser.parse(input_values, output)

        self.assertEqual(1, len(output.output))
        self.assertEqual(9, output.output[0])

    def test_6(self):
        input_values = "30 j 14 21 5 j 0 11 0 19"
        output = app.ParserOutput()

        parser.parse(input_values, output)

        self.assertEqual(1, len(output.output))
        self.assertEqual(-9, output.output[0])

    def test_7(self):
        input_values = "30 a 3 30 a 2 30 a 1 30 b -1 30 b 13 30 c 15 32 c 30 d 31 33 32 b 33 19"
        output = app.ParserOutput()

        parser.parse(input_values, output)

        self.assertEqual(8, len(output.output))
        self.assertIn("a: 1 2 3", output.output)
        self.assertIn("b: 13 -1", output.output)
        self.assertTrue(("c: " in output.output) or ("c:" in output.output))
        self.assertIn("d: 31", output.output)
        self.assertIn("a: 1 2 3", output.output)
        self.assertTrue(("b: " in output.output) or ("b:" in output.output))
        self.assertTrue(("c: " in output.output) or ("c:" in output.output))
        self.assertIn("d: 31", output.output)


class Phase3TestCases(unittest.TestCase):

    def test_1(self):
        input_values = "40 R 20 0 2 3 11 3 21 7 4 3 11 3 19"
        output = app.ParserOutput()

        parser.parse(input_values, output)

        self.assertEquals(2, len(output.output))
        self.assertEqual(60, output.output[0])
        self.assertEqual(1, output.output[1])

    def test_2(self):
        input_values = "40 R 30 20 21 30 22 23 30 24 25 20 20 20 26 11 26 33 19 0 a 12 a 31 a 17 0"
        output = app.ParserOutput()

        parser.parse(input_values, output)

        self.assertEqual(2, len(output.output))
        self.assertEqual(48, output.output[0])
        self.assertEqual("a: 12", output.output[1])

    def test_3(self):
        input_values = "40 L 20 20 5 16 21 7 18 16 11 16 11 6 19 12 32 19"
        output = app.ParserOutput()

        parser.parse(input_values, output)

        self.assertEqual(7, len(output.output))
        self.assertEqual("1: ADD 20 5 16", output.output[0])
        self.assertEqual("2: SUB 7 18 16", output.output[1])
        self.assertEqual("3: OUT 16", output.output[2])
        self.assertEqual(-11, output.output[3])
        self.assertEqual("4: OUT 6", output.output[4])
        self.assertEqual(21, output.output[5])
        self.assertEqual("5: END", output.output[6])

    def test_4(self):
        input_values = "40 L 30 a 5 30 a 8 30 a 800 11 a 19"
        output = app.ParserOutput()

        parser.parse(input_values, output)

        self.assertEqual(6, len(output.output))
        self.assertEqual("1: PUSH a 5", output.output[0])
        self.assertEqual("2: PUSH a 8", output.output[1])
        self.assertEqual("3: PUSH a 800", output.output[2])
        self.assertEqual("4: OUT a", output.output[3])
        self.assertEqual("800 8 5", output.output[4])
        self.assertEqual("5: END", output.output[5])

    def test_5(self):
        input_values = "40 L 30 a 3 30 a 2 30 a 1 30 b -1 30 b 13 30 c 15 32 c 30 d 31 33 32 b 33 19"
        output = app.ParserOutput()

        parser.parse(input_values, output)

        self.assertEqual(20, len(output.output))
        self.assertEqual("1: PUSH a 3", output.output[0])
        self.assertEqual("2: PUSH a 2", output.output[1])
        self.assertEqual("3: PUSH a 1", output.output[2])
        self.assertEqual("4: PUSH b -1", output.output[3])
        self.assertEqual("5: PUSH b 13", output.output[4])
        self.assertEqual("6: PUSH c 15", output.output[5])
        self.assertEqual("7: CLEAR c", output.output[6])
        self.assertEqual("8: PUSH d 31", output.output[7])
        self.assertEqual("9: DUMP", output.output[8])
        self.assertEqual("a: 1 2 3", output.output[9])
        self.assertEqual("b: 13 -1", output.output[10])
        self.assertTrue("c:" == output.output[11].strip())  # flex
        self.assertEqual("d: 31", output.output[12])
        self.assertEqual("10: CLEAR b", output.output[13])
        self.assertEqual("11: DUMP", output.output[14])
        self.assertEqual("a: 1 2 3", output.output[15])
        self.assertEqual("b:", output.output[16].strip())  # flex
        self.assertEqual("c:", output.output[17].strip())  # flex
        self.assertEqual("d: 31", output.output[18])
        self.assertEqual("12: END", output.output[19])

    def test_6(self):
        input_values = "40 RL 20 0 2 3 11 3 21 7 4 3 11 3 19"
        output = app.ParserOutput()

        parser.parse(input_values, output)

        self.assertEqual(7, len(output.output))
        self.assertEqual("1: ADD 0 2 3", output.output[0])
        self.assertEqual("2: OUT 3", output.output[1])
        self.assertEqual(60, output.output[2])
        self.assertEqual("3: SUB 7 4 3", output.output[3])
        self.assertEqual("4: OUT 3", output.output[4])
        self.assertEqual(1, output.output[5])
        self.assertEqual("5: END", output.output[6])


if __name__ == '__main__':
    unittest.main()

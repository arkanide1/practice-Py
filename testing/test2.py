import unittest
import main


class TestMain(unittest.TestCase):
    def test_do_stuff(self):
        test_param = 10
        result = main.do_stuff(test_param)
        self.assertEqual(result, 15)

    def test_do_stuff2(self):
        test_param = "hello"
        result = main.do_stuff(test_param)
        # self.assertEqual(isinstance(result,ValueError) )
        # self.assertTrue(isinstance(result,ValueError) )
        self.assertIsInstance(result, ValueError)

    def test_do_stuff3(self):
        test_param = None
        result = main.do_stuff(test_param)
        self.assertEqual(result, "enter a number")


if __name__ == '__main__':
    unittest.main()

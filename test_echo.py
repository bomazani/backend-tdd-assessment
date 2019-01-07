import unittest
import echo
import subprocess


class TestEcho(unittest.TestCase):
    def test_upper(self):
        """ Check for short upper flag"""
        args_list = ['-u', 'hello']
        self.assertEqual(echo.main(args_list), 'HELLO')

    def test_upper_long(self):
        """ Check for long upper flag"""
        args_list = ['--upper', 'hello']
        self.assertEqual(echo.main(args_list), 'HELLO')

    def test_lower(self):
        """ Check for short lower flag"""
        args_list = ['-l', 'hello']
        self.assertEqual(echo.main(args_list), 'hello')

    def test_lower_long(self):
        """ Check for long lower flag"""
        args_list = ['--lower', 'hello']
        self.assertEqual(echo.main(args_list), 'hello')

    def test_title(self):
        """ Check for short title flag"""
        args_list = ['-t', 'hello']
        self.assertEqual(echo.main(args_list), 'Hello')

    def test_title_long(self):
        """ Check for long title flag"""
        args_list = ['--title', 'hello']
        self.assertEqual(echo.main(args_list), 'Hello')

    def all(self):
        """ Check for all short flags"""
        args_list = ['-ult', 'hello']
        self.assertEqual(echo.main(args_list), 'Hello')

    def none(self):
        """ Check for no flags"""
        args_list = ['TestText']
        self.assertEqual(echo.main(args_list), 'TestText')

    def test_help(self):
        """ Running the program without arguments should show usage. """
        # Run the command `python ./echo.py -h` in a separate process, then
        # collect it's output.
        process = subprocess.Popen(
            ["python", "./echo.py", "-h"],
            stdout=subprocess.PIPE)
        stdout, _ = process.communicate()
        usage = open("./USAGE", "r").read()

        self.assertEquals(stdout, usage)

    def test_parser(self):
        """ Checks if parser recognizes a given argument flag"""
        parser = echo.create_parser()
        result = parser.parse_args(['-ult', 'hello'])
        self.assertTrue(result.upper)
        self.assertTrue(result.lower)
        self.assertTrue(result.title)
        self.assertEqual(result.text, 'hello')

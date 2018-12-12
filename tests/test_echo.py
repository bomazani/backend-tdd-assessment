#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import echo


class TestEcho(unittest.TestCase):
    def test_lower_case(self):
        arg_list = ["-l", "Hello World"]
        self.assertEqual(echo.main(arg_list), "hello world")

    def test_upper_case(self):
        arg_list = ["-u", "Hello World"]
        self.assertEqual(echo.main(arg_list), "HELLO WORLD")

    def test_title_case(self):
        arg_list = ["-t", "Hello World"]
        self.assertEqual(echo.main(arg_list), "Hello World")


if __name__ == '__main__':
    unittest.main()

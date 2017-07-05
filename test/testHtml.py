#-*- coding:utf-8 -*-
__author__ = "ting.yin"

import unittest
from unittest import defaultTestLoader

class Testhtml(unittest.TestCase):
    def test_hello(self):
        print ("i am test the hell")


if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTests()
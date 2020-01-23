# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 09:40:57 2019

@author: alberto.quesada

"""
import io
import sys
#import logging
import run_app
import unittest

class unit_test(unittest.TestCase):
    def test_print_hello_world(self):
#        log = logging.getLogger("TestLog")
#        log.debug("debug message")
        captured_output = io.StringIO()
        sys.stdout = captured_output
        run_app.print_hello_world()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue(), "Hello world\n")


#logging.basicConfig(stream=sys.stderr,level=logging.DEBUG)
unittest.main()
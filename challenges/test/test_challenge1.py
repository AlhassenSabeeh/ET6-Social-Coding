#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: AL-HASSEN SABEEH
"""

import unittest

from ..challenge1 import challenge1


class TestChallegne1(unittest.TestCase):
    """Test the binary_to_decimal function"""

    # Test Edge Cases
    def challenge1(self):
        """It should print 'Login is successful'"""
        self.assertEqual(challenge1("0"), "Login is successful")
# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testRightTriangleA(self): 
        self.assertEqual(classifyTriangle(3,4,5),'Right','3,4,5 is a Right triangle')

    def testRightTriangleB(self): 
        self.assertEqual(classifyTriangle(5,3,4),'Right','5,3,4 is a Right triangle')

    def testRightTriangleB(self): 
        self.assertEqual(classifyTriangle(4,5,3),'Right','4,5,3 is a Right triangle')
        
    def testEquilateralTriangles(self): 
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral','1,1,1 should be equilateral')

    def testEquilateralTriangles1(self): 
        self.assertEqual(classifyTriangle(155,155,155),'Equilateral','155,155,155 should be equilateral')

    def testNotEquilateralTriangles(self): 
        self.assertNotEqual(classifyTriangle(5,4,5),'Equilateral','5,4,5 should be isoceles')

    def testNotEquilateralTriangles(self): 
        self.assertEqual(classifyTriangle(155,145,125),'Equilateral','155,145,125 should be scalene')

    def testScaleneTriangle(self): 
        self.assertEqual(classifyTriangle(5,3,6),'Scalene','5,3,6 is a Scalene triangle')

    def testIsoscelesTriangle1(self): 
        self.assertEqual(classifyTriangle(5,6,6),'Isosceles','5,6,6 is a Isosceles triangle')

    def testIsoscelesTriangle2(self): 
        self.assertEqual(classifyTriangle(6,5,6),'Isosceles','6,5,6 is a Isosceles triangle')

    def testIsoscelesTriangle23(self): 
        self.assertEqual(classifyTriangle(6,6,5),'Isosceles','6,6,5 is a Isosceles triangle')

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()


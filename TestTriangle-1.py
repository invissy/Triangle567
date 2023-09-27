# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest
from datetime import date

from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testRightTriangle345(self): 
        self.assertEqual(classifyTriangle(3,4,5),'Right','3,4,5 is a Right triangle')

    def testRightTriangle534(self): 
        self.assertEqual(classifyTriangle(5,3,4),'Right','5,3,4 is a Right triangle')

    def testRightTriangle453(self): 
        self.assertEqual(classifyTriangle(4,5,3),'Right','4,5,3 is a Right triangle')
        
    def testEquilateralTriangle111(self): 
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral','1,1,1 should be equilateral')

    def testEquilateralTriangle155(self): 
        self.assertEqual(classifyTriangle(155,155,155),'Equilateral','155,155,155 should be equilateral')

    def testNotEquilateralTriangle545(self): 
        self.assertNotEqual(classifyTriangle(5,4,5),'Equilateral','5,4,5 should be isoceles')

    def testNotEquilateralTriangle155(self): 
        self.assertNotEqual(classifyTriangle(155,145,125),'Equilateral','155,145,125 should be scalene')

    def testScaleneTriangle536(self): 
        self.assertEqual(classifyTriangle(5,3,6),'Scalene','5,3,6 is a Scalene triangle')

    def testScaleneTriangle749(self): 
        self.assertEqual(classifyTriangle(7,4,9),'Scalene','7,4,9 is a Scalene triangle')

    def testIsoscelesTriangle566(self): 
        self.assertEqual(classifyTriangle(5,6,6),'Isosceles','5,6,6 is a Isosceles triangle')

    def testIsoscelesTriangle656(self): 
        self.assertEqual(classifyTriangle(6,5,6),'Isosceles','6,5,6 is a Isosceles triangle')

    def testIsoscelesTriangle665(self): 
        self.assertEqual(classifyTriangle(6,6,5),'Isosceles','6,6,5 is a Isosceles triangle')

    def testNotTriangle285(self): 
        self.assertEqual(classifyTriangle(2,8,5),'NotATriangle','2,8,5 is a Isosceles triangle')

def my_brand():
    print("=*=*=*= Cindy Lee =*=*=*=")
    print("=*=*=*= Course 2023S-SSW567 =*=*=*=")
    print("=*=*=*= HW 02a - Testing a legacy program and reporting on testing results =*=*=*=")
    print("=*=*=*=", date.today(), "=*=*=*=")
    print()

if __name__ == '__main__':
    my_brand()
    print('Running unit tests')
    unittest.main()


#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Triangle Project Code.

# Triangle analyzes the lengths of the sides of a triangle
# (represented by a, b and c) and returns the type of triangle.
#
# It returns:
#   'equilateral'  if all sides are equal
#   'isosceles'    if exactly 2 sides are equal
#   'scalene'      if no sides are equal
#
# The tests for this method can be found in
#   about_triangle_project.py
# and
#   about_triangle_project_2.py
#
def triangle(a, b, c):
    # DELETE 'PASS' AND WRITE THIS CODE
    sides = sorted([a,b,c])
    sides_sorted = sorted(set(sides))

    if sides_sorted[0] == 0:
        raise TriangleError("Sides cannot be 0")

    if sides[2] >= sides[0] + sides[1]:
        raise TriangleError("Sum of two sides cannot be greater than third")

    if len(sides_sorted) == 1:
         return "equilateral"
    elif len(sides_sorted) == 2: 
        return "isosceles"
    else: return "scalene"


    


# Error class used in part 2.  No need to change this code.
class TriangleError(Exception):
    pass

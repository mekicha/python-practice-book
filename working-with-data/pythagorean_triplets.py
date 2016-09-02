""" Find all Pythagorean triplets using numbers below 25. 
(x, y, z) is a called pythagorean triplet if x*x + y*y == z*z."""


n = 25
print [(x,y,z) for x in range(1,n) for y in range(x,n) 
       for z in range(y,n) if x*x + y*y == z*z
      ]
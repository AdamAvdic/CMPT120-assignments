# sources = pythonguides.com/find-area-of-a-triangle-in-python/
import math

a = int(input("Enter the length of side 1: "))
b = int(input("Enter the length of side 2: "))
c = int(input("Enter the length of side 3: "))


p = ((a+b+c)/2)



area = math.sqrt((p*(p-a)*(p-b)*(p-c)))

if (a + b) <= c:
    print("These lengths do not form a triangle")

elif a == c != b or a == b != c or b == a != c or b == c != a or c == a != b or c == b != a:
    print("These lengths form an Isosceles triangle.")
    print("The area of the triangle is {:.2f}".format(area))

elif a != c != b or a != b != c or b != a != c or b != c != a or c != a != b or c != b != a:
    print("These lengths do not form an Isosceles triangle.")
    print("The area of the triangle is {:.2f}".format(area))

else:
    print("")


          

import math
def db(c,m):
    print(c + m)
    print (c - m)
    print (c * m)
    print (c / m)
    print (c ** m)
    print (math.sqrt(c),'            ',          math.sqrt(m))
    print (math.factorial(c),'            ',           math.factorial(m))
    print (math.sin(c),'            ',    math.sin(m))
    print (math.cos(c),'            ',    math.cos(m)) 
    print (math.tan(c),'            ',math.tan(m) )
db(c = int(input("Введите число: ")), m = int(input("Введите число: ")))
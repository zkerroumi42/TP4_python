class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_x(self):
        return self.x
    
    def get_y(self):
        return self.y
    
    def set_x(self, x):
        self.x = x
    
    def set_y(self, y):
        self.y = y

    def __str__(self):
        return f"Point({self.x}, {self.y})"


class Rectangle(Point):
    def __init__(self, x, y,lon, lar):
        super().__init__(x, y)
        self.lon = lon
        self.lar = lar

    def get_lon(self):
        return self.lon
    
    def get_lar(self):
        return self.lar
    
    def set_lon(self, x):
        self.lon = lon
    
    def set_lar(self, y):
        self.lar = lar
        
    def aire(self):
        return self.lon * self.lar

    def __str__(self):
        return f"Rectangle({self.x}, {self.y}, {self.lon}, {self.lar})"


class Parallelepipede(Rectangle):
    def __init__(self, x, y, lon, lar, h):
        super().__init__(x, y, lon, lar)
        self.h = h

    def aire(self):
        return 2 * (self.lon * self.lar + self.lon * self.h + self.lar * self.h)

    def volume(self):
        return self.lon * self.lar * self.h

    def __str__(self):
        return f"Parallelepipede({self.x}, {self.y}, {self.lon}, {self.lar}, {self.h})"


# pour tester la classe point
p = Point(2,4)
print(p)
print(p.get_x(), p.get_y())

# pour tester la class rectangle
r = Rectangle(2,4,2,4)
print(r)
print(r.get_x(), r.get_y(), r.get_lon(), r.get_lar())
aire =r.aire()
print(aire) 
print("meters carre")
str=r.__str__()
print(str)


#pour tester la class Parallelepipede

Parallelepipede = Parallelepipede(2,4,2,4,2)
print(Parallelepipede)
airee =Parallelepipede.aire()
print(airee)
print("meters carre")

volume = Parallelepipede.volume()
print(volume)
print("meters cub")
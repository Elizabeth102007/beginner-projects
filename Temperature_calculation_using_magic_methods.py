class Temperature:
    def __init__(self, degree):
        self.degree = degree
    
    def __str__(self):
        return f"{self.degree}°C"
    
    def __add__(self, another):
        total_de = self.degree + another.degree
        return Temperature(total_de)
    
    def __sub__(self, another):
        total_de = self.degree - another.degree
        if total_de < -273:
            raise ValueError ("Temperature can't be less than or equal to zero")
        else:
            return Temperature(total_de)

t1 = Temperature(34)
t2 = Temperature(18)


print(t1 - t2)

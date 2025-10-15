#an online store hs base class product and two derived classes 1.electroics attr - brand,warranty2.clothing -size,fabric
class Product:
    def __init__(self,name):
        self.name = name
    def display(self):
        print(self.name,end=" ")
class Electronics(Product):
    def __init__(self,brand,warranty,*args):
        super().__init__(*args)
        self.brand = brand
        self.warranty = warranty
    def display(self):
        super().display()
        print(self.brand,self.warranty,end=" ")
class Clothing(Product):
    def __init__(self, size,fabric,*args):
        super().__init__(*args)
        self.size = size
        self.fabric = fabric
    def display(self):
        super().display()
        print(self.size,self.fabric,end=" ")
pr1 = Product("Shirt")
El1 = Electronics("Apple","5 years","I-Phone")
cl1 = Clothing("M","Woolen","Sweater")
for i in (pr1,El1,cl1):
    i.display()
    print()
        
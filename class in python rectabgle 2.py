class rec():
    _count = 0
    def __init__(self , largeur = 4 , longueur =-7 ):
        self.__largeur = largeur
        self.__longueur = longueur
        rec._count += 1


#THE GETTERS
    def getlongueur (self):
        return self.__longueur
    
    def getlargeur (self):
        return self.__largeur
    
    def getcount (self):
        return rec._count

#THE SETTERS
    def setlongueur(self,longueur):
        self.__longueur = longueur

    def setlargeur(self,largeur):
        self.__largeur = largeur


#methods
    def equals(self,rec2): #the comparison between two rectangle.
        #the first rectangle.
        long1 = self.getlongueur()
        lar1 = self.getlargeur()
        #the second vector.
        long2 = rec2.getlongueur()
        lar2 = rec2.getlargeur()
        if (long1 == long2) and (lar1 == lar2) :
            return True
        else:
            return False

    def perimetre(self):
        print("perimeter :",(self.__longueur + self.__largeur)*2)
     
    def surface(self):
        print("surface :", (self.__longueur * self.__largeur))
    
    def TOSTRING(self):
        print(f" longueur ={self.getlongueur()}")
        print(f" largeur ={self.getlargeur()}")


# child class
def parallepiped(rec):
    _counter = 0
    def __init__(self , largeur, longueur, height = 2 ):
        super().__init__(largeur,longueur)
        self.__height= height
        parallepiped._counter += 1

#GETTERS
    def getheight (self):
        return self.__height
    
    def getcounter (self):
        return rec._counter


 #THE SETTERS
    def setheight(self,height):
        self.__height = height


#methods
    def equals(self,rec3): #the comparison between two rectangle.
        #the first rectangle.
        long1 = self.getlongueur()
        lar1 = self.getlargeur()
        hei1 = self.getheight()
        #the second vector.
        long2 = rec3.getlongueur()
        lar2 = rec3.getlargeur()
        hei2 = rec3.getheight()
        if (long1 == long2) and (lar1 == lar2) and ( hei1 == hei2):
            return True
        else:
            return False

    def perimetre(self):
       print("perimeter of the parallepiped:",((self.__longueur + self.__largeur)*2)*self.__height)
    
    def surface(self):
        print("the surface of the parrallepiped:", ((self.__longueur * self.__largeur)+(self.__longueur * self.__height)+(self.__height * self.__largeur))*2)

    def TOSTRING(self):
        print(f" longueur ={self.getlongueur()}")
        print(f" largeur ={self.getlargeur()}")
        print(f" height ={self.getheight()}")

    def volume(self):
        print("the volume of the parallelipiped:", self.__largeur * self.__longueur * self.__height )
    
R1 = rec()
R2 = rec(3,6)
if R1.equals(R2)== True:
    print("is equal.")
else:
    print("is not equal.")
R1.TOSTRING()
R2.TOSTRING()
R1.surface()
R2.surface()
R1.perimetre()
R2.perimetre()

r1 = parallepiped(7)
r2 = parallepiped(2)
if r1.equals(r2) == True :
    print("is equals.")
else:
    print("not equals.")
r1.TOSTRING()
r2.TOSTRING()
r1.surface()
r2.surface()
r1.perimetre()
r2.perimetre()
r1.volume()
r2.volume()


    

    


    


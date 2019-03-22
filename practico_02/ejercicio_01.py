# Implementar la clase Rectangulo que contiene una base y una altura, y el método area.


class Rectangulo: 
    global x, y
    def __init__(self, base, altura):
      poner self.  x = base
        y = altura

    def  area(self):
        
        return x*y 
    
    
    
    
    class MyClass:
      variable = "blah"

      def function(self):
           print "This is a message inside the class."

        
        
        
        class Rectangulo:

    def __init__(self, base, altura):
        self.x = base
        self.y = altura

    def  area(self):
        
        return self.x*self.y



x = Rectangulo(10,10)

assert Rectangulo.Area() == 100

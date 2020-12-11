from stille_nacht.util import Abstract_Canvas
class Mock_Canvas(Abstract_Canvas):
    def __init__(self,height=400, width=400):
        self.__height = height
        self.__width = width

    def draw_circle(self,x,y,color,diameter):
        pass
    def get_width(self):
        return self.__width
    def get_height(self):
        return self.__height

def test_snow1():
    pass

def test_snow2():
    pass

def test_snow3():
    pass
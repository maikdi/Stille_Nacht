from stille_nacht.util import Canvas
import sys


class Snow:
    def __init__(self, index, x, y, canvas, diameter=2, color=Canvas.WHITE):
        self.__index = index
        self.__canvas = canvas
        self.__x = x
        self.__y = y
        self.__color = color
        self.__diameter = diameter

    def __str__(self):
        return "Snow number {}".format(self.__index)

    def fall(self):
        if self.__y >= self.__canvas.get_height():
            self.__y = 0
        else:
            self.__y = self.__y + 1

        self.__canvas.draw_circle(self.__x, self.__y, self.__color, self.__diameter)


class Star:
    def __init__(self, index, x, y, canvas, diameter=10, color=Canvas.RED):
        self.__index = index
        self.__c    anvas = canvas
        self.__color = color
        self.__x = x
        self.__y = y
        self.__diameter = diameter

    def blink(self):
        self.__canvas.draw_circle(
            self.__x,
            self.__y,
            self.__color,
            self.__diameter
        )

        if self.__color == Canvas.RED:
            self.__color = Canvas.YELLOW
        else:
            self.__color = Canvas.RED

    def __str__(self):
        return "Star number {} color {}".format(self.__index, self.__color)


class Moon:
    def __init__(self, x, y, canvas, color=Canvas.GRAY, diameter=50):
        self.__canvas = canvas
        self.__color = color
        self.__x = x
        self.__y = y
        self.__diameter = diameter

    def shine(self):
        self.__canvas.draw_circle(
            self.__x,
            self.__y,
            self.__color,
            self.__diameter
        )


class Painting:
    def __init__(self):
        # 1 canvas.
        self.__canvas = Canvas()

        # 5 snows
        self.__snows = [
            Snow(1, 50, 0, self.__canvas),
            Snow(2, 100, 0, self.__canvas),
            Snow(3, 150, 0, self.__canvas),
            Snow(4, 200, 0, self.__canvas),
        ]

        # 3 stars
        self.__region = self.__get_region()
        if self.__region == "INA":
            self.__stars = [
                Star(1, 50, 20, self.__canvas),
                Star(2, 150, 100, self.__canvas),
                Star(3, 250, 50, self.__canvas),
            ]
        elif self.__region == "DE":
            self.__stars = [CrossStar(1, 30, 30, self.__canvas)]

        self.__moon = Moon(350, 60, self.__canvas)

    def draw(self):
        running = True

        while running:
            # set all to black
            self.__canvas.reset_background()

            self.__moon.shine()

            for snow in self.__snows:
                snow.fall()
            for star in self.__stars:
                star.blink()

            self.__canvas.flip()

            running = not self.__canvas.is_quit()

        self.__canvas.quit()

    def __get_region(self):
        try:
            region = sys.argv[1]
        except:
            region = "DE"
        return region

    def __create_stars(self):
        region = self.__region
        if self.__region == "INA":
            self.__stars = [
                Star(1, 50, 20, self.__canvas),
                Star(2, 150, 100, self.__canvas),
                Star(3, 250, 50, self.__canvas),
            ]


class CrossStar(Star):
    # def __init__(self, index, x, y, canvas,diameter=10,color=Canvas.RED):
    #     super().__init__(index, x, y,canvas ,diameter,color)
    #     self.__index = index
    #     self.__canvas = canvas
    #     self.__x = x
    #     self.__y = y
    #     self.__diameter = diameter
    #     self.__color = color

    def blink(self):
        self.__canvas.draw_circle(self.__x, self.__y - self.__diameter, self.__color, self.__diameter)
        self.__canvas.draw_circle(self.__x, self.__y + self.__diameter, self.__color, self.__diameter)
        self.__canvas.draw_circle(self.__x - self.__diameter, self.__y, self.__color, self.__diameter)
        self.__canvas.draw_circle(self.__x + self.__diameter, self.__y, self.__color, self.__diameter)
        if self.__color == Canvas.RED:
            self.__color = Canvas.YELLOW
        else:
            self.__color = Canvas.RED

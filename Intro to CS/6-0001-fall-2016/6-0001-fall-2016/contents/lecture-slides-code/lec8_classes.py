#################
## EXAMPLE: simple Coordinate class
#################
class Coordinate(object):
    """ A coordinate made up of an x and y value """
    def __init__(self, x, y):
        """ Sets the x and y values """
        self.x = x
        self.y = y
    def __str__(self):
        """ Returns a string representation of self """
        return "<" + str(self.x) + "," + str(self.y) + ">"
    def distance(self, other):
        """ Returns the euclidean distance between two points """
        x_diff_sq = (self.x-other.x)**2
        y_diff_sq = (self.y-other.y)**2
        return (x_diff_sq + y_diff_sq)**0.5


c = Coordinate(3,4)
origin = Coordinate(0,0)
print(f"{c.x},{origin.x}")
print(c.distance(origin))
print(Coordinate.distance(c, origin))
print(origin.distance(c))
print(c)
print(Coordinate.distance(origin,c))
help(Coordinate)

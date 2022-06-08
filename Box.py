class Box:

    def __init__(self, color, weight, content_breakable):
        self.__color = color
        self.__weight = weight
        self.__content_breakable = content_breakable

    def getColor(self):
        return self.__color

    def getWeight(self):
        return self.__weight

    def isContentBreakable(self):
        return self.__content_breakable

    def compareBox(self, other):
        if (self.getColor().casefold() == other.getColor().casefold()
                and self.getWeight() == other.getWeight()
                and self.isContentBreakable() == other.isContentBreakable()):
            return True
        else:
            return False

    def __str__(self):
        return ("[ BOX: " + str(self.getColor()) + "-"
                + str(self.getWeight()) + "-"
                + str(self.isContentBreakable()) + "]")


class RedBox(Box):

    def __init__(self, weight, content_breakable):
        print("In red box")
        super().__init__("Red", weight, content_breakable)
        self.__price = 0

    def setPrice(self, price):
        self.__price = price

    def getPrice(self):
        return self.__price


class PerecibleItemBox(Box):

    def __init__(self, color, weight):
        print("In pereciable Items")
        super().__init__(color, weight, True)
        self.__price = 0

    def setPrice(self, price):
        self.__price = price

    def getPrice(self):
        return self.__price

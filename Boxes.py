class Boxes:
    number_of_boxes = 0

    def __init__(self):
        self.box_list = []
        Boxes.number_of_boxes = 0

    def addABox(self, box):
        self.box_list.append(box)
        Boxes.number_of_boxes += 1

    def getBoxes(self):
        return self.box_list

    def searchBox(self, bx):
        for box in self.getBoxes():
            if box.compareBox(bx):
                return box

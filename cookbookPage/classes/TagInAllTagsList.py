class TagInAllTagsList():
    def __init__(self,name):
        self.name = name
        self.selected = False
    def __str__(self):
        return self.name
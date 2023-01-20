"""You can use this class to represent how classy someone
or something is.
"Classy" is interchangable with "fancy".
If you add fancy-looking items, you will increase
your "classiness".
Create a function in "Classy" that takes a string as
input and adds it to the "items" list.
Another method should calculate the "classiness"
value based on the items.
The following items have classiness points associated
with them:
"tophat" = 2
"bowtie" = 4
"monocle" = 5
Everything else has 0 points.
Use the test cases below to guide you!"""


class Classy(object):
    def __init__(self):
        self.items = []

    def addItem(self,item):
        self.items.append(item)
        
    def getClassiness(self):
        data = []
        for item in self.items:
            if item == "tophat":
                x  = 2
                data.append(x)
            elif item == "bowtie":
                y = 4
                data.append(y)
            elif item == "monocle":
                z = 5
                data.append(z)
            else:
                data.append(0)
        return sum(data)

        

me = Classy()

me.addItem("tophat")
print(me.getClassiness())


me.addItem("bowtie")
me.addItem("jacket")
me.addItem("monocle")
# Should be 11
print (me.getClassiness())

me.addItems("bowtie")
# Should be 15
print (me.getClassiness())
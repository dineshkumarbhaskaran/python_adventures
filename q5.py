
class simple_class:
    def __init__(self):
        self.s = ""

    def get_string(self):
        print "Please enter a string"
        self.s = raw_input()

    def print_string(self):
        print self.s.upper()


if __name__ == "__main__":
    my_class = simple_class()
    my_class.get_string()
    my_class.print_string()
    

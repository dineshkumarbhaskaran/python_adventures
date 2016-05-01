class Person:
    '''This is a person class'''
    name = 'asdfgh'

    def __init__(self, uname = None):
        self.name = uname

if __name__ == '__main__':
    print Person.__doc__
    nperson = Person('one')
    print Person.name, nperson.name

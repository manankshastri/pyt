class Animal:

    def __init__(self, **kwargs):
        self._type = kwargs['type'] if 'type' in kwargs else 'dog'
        self._name = kwargs['name'] if 'name' in kwargs else 'tom'
        self._sound = kwargs['sound'] if 'sound' in kwargs else 'bark'

    def type(self):
        return self._type

    def name(self):
        return self._name

    def sound(self):
        return self._sound

def print_function(o):
    if not isinstance(o, Animal):
        raise TypeError('print_function() requires an Animal')
    print('The {} is named {} and says {}. '.format(o.type(), o.name(), o.sound()))

def main():
    a0 = Animal(type='kitten', name='fluffy', sound='rwar')
    a1 = Animal(type='duck', name='donald', sound='quack')
    print_function(a0)
    print_function(a1)
    print_function(Animal(type='velociraptor', name='veronica', sound='hello'))
    print_function(Animal())

if __name__ == '__main__' :
    main()

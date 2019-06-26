class Animal:

    def __init__(self, **kwargs):
        self._type = kwargs['type'] if 'type' in kwargs else 'dog'
        self._name = kwargs['name'] if 'name' in kwargs else 'tom'
        self._sound = kwargs['sound'] if 'sound' in kwargs else 'bark'

    def type(self, t=None):
        if t:
            self._type = t
        return self._type

    def name(self, n=None):
        if n:
            self._name = n
        return self._name

    def sound(self, s=None):
        if s:
            self._sound = s
        return self._sound

    def __str__(self):
        return f'The {self.type()} is named {self.name()} and says {self.sound()}.'


def main():
    a0 = Animal(type='kitten', name='fluffy', sound='meow')
    a1 = Animal(type='duck', name='donald', sound='quack')
    a2 = Animal()
    print(a0)
    print(a1)
    a2.name('tommy')
    print(a2)

if __name__ == '__main__':
    main()

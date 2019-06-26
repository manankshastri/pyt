class inclusive_range:
    def __init__(self, *args):
        numargs = len(args)
        self._start = 0
        self._step = 1

        if numargs < 1:
            raise TypeError(f'expected atleast 1 argument, got {numargs}')

        elif numargs == 1:
            self._stop = args[0]

        elif numargs == 2:
            (self._start, self._stop) = args

        elif numargs == 3:
            (self._start, self._stop, self._step) = args

        else:
            raise TypeError(f'expected atmost 3 arguments, got {numargs}')

        self._next = self._start

    def __iter__(self):
        return self

    def __next__(self):
        if self._next > self._stop:
            raise StopIteration
        else:
            r = self._next
            self._next += self._step
            return r

def main():
    for n in inclusive_range(6, 90, 8):
        print(n, end=" ")
    print()

if __name__ == '__main__':
    main()

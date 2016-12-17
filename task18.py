class FilteredSequence:
    def __init__(self, iterable):
        try:
            self._iter = iter(iterable)
            self._seq = []
            self._curiter = None
        except TypeError:
            print "Iterable object expected. Got: ({0}): {1}".format(e.errno, e.strerror)

    def __iter__(self):
        self._curiter = None
        return self

    def next(self):
        if self._curiter is None:
            self._curiter = iter(self._seq)

        e = next(self._curiter, None)
        if e is None:
            if self._curiter == self._iter:
                raise StopIteration
            else:
                self._curiter = self._iter
                e = next(self._curiter, None)
                if e is None:
                    raise StopIteration

        if self._curiter == self._iter:
            self._seq.append(e)

        return e

    def filtered(self, filter, *args, **kwargs):
        def _filtered_sequence():
            for i in iter(self):
                if filter(i, *args, **kwargs):
                    yield i
        return FilteredSequence(_filtered_sequence())

print "Seq 1."

seq = FilteredSequence(range(1,10))
for i in seq:
    print i


print "Seq 2."

def le(x, max):
    return x <= max

seq2 = seq.filtered(le, 7)
for i in seq2:
    print i


print "Seq 3."

def bounded(x, min, max):
    return min <= x and x <= max

seq3 = seq2.filtered(bounded, 2, 4)
for i in seq3:
    print i


print "Seq 4."

def even(x):
    return x % 2 == 0

seq4 = seq3.filtered(even)
for i in seq4:
    print i

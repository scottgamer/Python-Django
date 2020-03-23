# The Doppelganger Enigma

You have inherited some Python code related to high school physics. The previous coder is obviously on cracks since the codebase has this kind of pattern all over the place:

```python
LENGTH_UNITS = type('LENGTH_UNITS', (object,), {})
LENGTH_UNITS.pc = 3.08567758149137e16
LENGTH_UNITS.AU = 149597870700
LENGTH_UNITS.km = 10**3
LENGTH_UNITS.mm = 10**-3
LENGTH_UNITS.µm = 10**-6
LENGTH_UNITS.nm = 10**-9

EM_LABELS = type('EM_LABELS', (object,), {})
EM_LABELS.A = 'current'
EM_LABELS.V = 'voltage'
EM_LABELS.Ω = 'resistance'
EM_LABELS.W = 'power'
```

The enhancement you're tasked to do is to refactor these code to use [collections.namedtuple](https://docs.python.org/3/library/collections.html#collections.namedtuple) which is better suited for usages like this. It looks very easy, or so it seems... after you finished writing your code, there are some weird, headscratching errors when you run your unit test code. Looks like it's not as simple as you might think.

Note: If you understand the point of this kata, there are cases where ambiguities could arise: such cases will not appear in the tests. Also, attribute names passed in will not contain duplicates or invalid attributes (e.g `obj.def` or `obj.123`).

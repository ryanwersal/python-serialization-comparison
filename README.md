# Python Serialization Comparison

A primitive comparison between several serialization formats and their performance and serialized size.

Currently compares:

 - [JSON](https://docs.python.org/2/library/json.html)
 - [Pickle](https://docs.python.org/2/library/pickle.html)
 - [cPickle](https://docs.python.org/2/library/pickle.html#module-cPickle)
 - [Transit](https://github.com/cognitect/transit-python) (json & msgpack)
 - [msgpack](https://github.com/msgpack/msgpack-python)

More probably coming soon.

Samples generated with assistance from [JSON Generator](http://www.json-generator.com/).

## Running

Simply execute `benchmark.py`:

```
./benchmark.py
```

It supports a couple options for tweaking number of passes and the iteration count per pass.



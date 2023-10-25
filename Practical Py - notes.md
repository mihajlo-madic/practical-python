# Day 1

---

## 1. Intro to python

- REPL - _read-eval-print-loop_;
- `print('Hello', end=' ')`;
- `pass` - NOP;
- first program:

```python
# bounce.py
#
# Exercise 1.5

height = 100

for i in range(1, 11):
    height *= 0.6
    print(f"{i} {round(height, 4)}")

```

- native support for complex numbers;
- `math` module;
- triple quotes string;
- https://unicode.org/charts/;
- `str.strip()`, `str.lower()`, `str.upper()`, `str.replace()`;
  ![[Pasted image 20231023113306.png]]
- strings are immutable - read-only;
- `str()` - conversion to a string;
- `b''` byte string;

```python
text = data.decode('utf-8') # bytes -> text
data = text.encode('utf-8') # text -> bytes
# The `'utf-8'` argument specifies a character encoding. Other common values include `'ascii'` and `'latin1'`.
```

- `r''` - raw string - unintepreted `\` - filename itd.;
- `f''` - f-string - `print(f"{month:>5d} {total_paid:>10.2f} {principal:>10.2f}")`;
- string concatenation;
- `in` operator - membership testing;
- `dir()` function;
- `help()` function;
- `str.split(delim)`;
- lists - indexing, concatenation, mutable, replication, `for` iteration, `list.index()`, `list.remove()`, `del list[index]`;
- in-place sorting - `list.sort()` or `sorted()` for creating new list;
- `in` operator za liste;
- `symlist.sort(reverse=True)` - reverse sorting;
- `','.join(list)`;
- multiple indexing;
- `open(putanja, mod)`, `f.read()`, `f.read([maxbytes])`;
- `f.close()`;
- `with` statement - same sa `using` in C#;
- `try-except` block - catching errors;
- `raise` $\equiv$ `throw`;
- `csv` module - `csv.reader(csv_file)`;
- `sys` module - `sys.argv`;

## 2. Working with data

- `None` type;
- tuple - `()` - single row in db table;
  - tuple packing and tuple unpacking;
  - single item consisting of more parts, rather than more items (lists are used for this purpose);
- dictionaries;
  - `del` statement;
  - many different values;
  - conversion to `list`;
  - `for` looping over a dict - looping over keys;
  - `dict.keys()`;
  - `dict_keys` object - shares memory with the original `dict`;
  - `dict.items()` - key-value tuples;
- `list` - ordered data, `dict` - unordered data, `set` - unordered, unique data;
- buliding list from scratch - `[]` and `list.append()`;
- building dictionary from scratch - `{}` and `dict[new_key] = new_val`;
- `in` for a key in dictionary;
- `dict.get(key, default)`;
- dict key => must be immutable;
- set union `|`, set intersection `&`, set difference `-`;
- `pprint` za stampanje `dict`;
- formatiranje `f''`:
  ![[Pasted image 20231023135549.png]]
  - `str.format_map(dict)`;
  - `str.format(args, kwargs)`;
  - C-style formatiranje - jedino dozvoljeno za byte stringove;
  - [string formatting](https://docs.python.org/3/library/string.html#format-specification-mini-language);
- sequence datatypes - string - list - tuple;
  - indexing, concatenation, replication, slicing, re-assignment;
  - iteration, `break`, `continue`;
  - `enumerate` function - index + value;
  - `zip` function - same as RxJS zip - `d = dict(zip(columns, values))`
  - `min`, `max`, `sum` - sequence operations;
  - **`dict(zip(column_names, values))`** => !!!!!!!!!!!!!!!!!;
  - `pprint(dict(zip(prices.values(), prices.keys())))` - inverting a `dict`;
  - `zip()` stops once shortest input sequence gets exhausted;
- [`collections` module](https://docs.python.org/3/library/collections.html) - `Counter`, `defaultdict`, `deque`;
- list comprehensions - creating new lists, filtering;
  ![[Pasted image 20231023143038.png]]
- sequence reductions + list comprehensions - `sum(comprehension)`;
- set comprehension - exchange `[]` with a `{}`;
- dictionary comprehension => set + specify _key:value_;
- `is` operator - checking if two values refer to the same object;
- `id()` function;
- shallow copies - `list()`;
- deep copy - `copy` module => `copy.deepcopy(obj)`;
- `type()`;
- `isinstance(obj, tuple_of_types)`;
- first-class objects;
- zip + types - parsing;

## 3. Program organization

- functions are blackboxes - avoid logic leaks;
- doc-string;
- type annotations;
- python runs faster with use of functions;
- named arguments call;
- default arguments;
- `None` is returned by default;
- global and local variables;
- all assignments in functions are local;
- `global <var_name>` - changing global variables in functions;

> [!danger] EXERCISE
>
> - => `parse_csv` function - work with headers, types, and selectors, for arbitrary csv formats;

- [x] Done

- built-in exceptions
  ![[Pasted image 20231023152341.png]]
- [documentation](https://docs.python.org/3/library/exceptions.html) of built-in exceptions;
- `Exception` - root of exception hierarchy, do avoid;
- re-raising the exception - log + pass the error to caller;
- `finally` statement - safe resource management;
- `with` statement - `try-finally`;
- silencing errors;

# Day 2

---

## 3. Program organization (cont.)

- any python source file is a module;
- `import` - loads and _executes_ a module;
- module is a namespace;
- `import as` statement;
- `from import` statement;
- `sys.modules` - dict of all imported modules;
- `sys.path` - searching for modules;
- main module;
- main check
  ![[Pasted image 20231024105617.png]]
- `__name__` - name of the module;
- writing command line tools;
- `sys.argv` - CL arguments;
- `sys.stdout, sys.stderr, sys.stdin` - stdio;
- `os.environ` - dictionary containing envars;
- program exit - `SystemExit` error or `sys.exit(exitcode)`;
- `bash$ which python3` - `/usr/bin/python3`;
- `#! /usr/bin/python3` + `chmod +x` - making an executable;
- duck typing;
  - ![[Pasted image 20231024112319.png]]-> second one is better because of flexibility;

### 4. Classes and Objects

- `class` statement;
- `__init__` function;
- `self` always first argument - it has to be used for scope;
- inheritance `class Child(Parent): ...`;
- `super()` - extending something but using the original for extension;
  - use in `__init__`;
- beware of the Liskov principle;
- [ ] `TextTableFormatter`, `HTMLTableFormatter`, `HTMLTableFormatter`;
- factory method - use it instead of `if-elif-else`;
- magic methods;
  - `__init__`;
  - `__repr__`;
  - `__str__`;
  - arithmetic operators![[Pasted image 20231024120345.png]]
  - item access
    ![[Pasted image 20231024120445.png]]
  - method lookup `.` => method invocation `()`;
    - _bound methods_;
  - attributes manipulation![[Pasted image 20231024120711.png]]=> `getattr` is really flexible;
- user defined exceptions - inherited from `Exception`;

### 5. Inner Workings of Python Objects

- object layer is entirely written on top of `dict`s;
  - each instance has its own private dictionary;
- local dictionary (`my_instance.__dict__`) and class dictionary (`MyClass.__dict__` or `my_instance.__class__.__dict__`);
- immediate parents are stored in tuple in each class;
- inheritance chain - `__mro__` attribute (Method Resolution Order - MRO);
  - MRO in multiple inheritance - children first, parents inorder - C3 linearization algorithm;
- mixin pattern - primary use of multiple inheritance - `Loud` example;
- `super()` - delegates to next class in MRO;
- class variables - same as static attributes in C++;
- objects in Py are _open_ by default;
- `_my_attr` - private;
- accessor methods - `@property`, `@my_prop.setter`, ...;
- private attributes, simple attributes, managed attributes-properties;
- decorator syntax;
- `__slots__` attribute - more efficient memory;

### 6. Generators

- iteration protocol - iterables and iterators;
- `StopIteration` error;
- `__iter__` - returns iterator;
- `__next__`, or `next()` - iterator method;
- [ ] analyze this![[Pasted image 20231024125941.png]]
- Pythonic code;
- generator functions - functions that define iteration - function that uses `yield` statement;
  - calling a generator function creates generator object;
  - it only executes on `next()` call;
  - **feeding a for loop with customized iteration**;
  - `in` operator - `__contains__()`;

> [!important] Producer, Consumer and Pipelines => using GENERATORS

- generator (make parallel to RxJS creator) $\equiv$ producer, for-loop $\equiv$ consumer;
  ![[Pasted image 20231024140726.png]]=> fun stuff
- **generator expressions** => similar to list comprehensions;
- generators => filters applied to a stream;
- why generators
  ![[Pasted image 20231024144704.png]]
- `itertools` module - rxjs operators?

> [!danger] [Generator tricks for systems programmers](http://www.dabeaz.com/generators/)

### 7. Advanced topics

- `*args` and `**kwargs`;
  ![[Pasted image 20231024145518.png]]
- `*` - `tuple` expanding operator, `**` - `dict` expanding operator;
- anonymous functions;
- callback functions and `lambda` expressions (anonymous function);
- returning function from a function - **CLOSURES** (function + environment);
- `typedproperty` example!!!
- decorators
  - wrapper functions;
    ![[Pasted image 20231024152929.png]]
- `@timethis` custom decorator;
- built-in decorators;
  - `@staticmethod` - marking static methods,
  - `@classmethod` - receives `cls` object instead of `self`, making alternate constructors,
  - `@property` - defining properties;

---

## Day 3

### 8. Testing and debugging

- `assert` statement, `AssertionError` exception - used for conditions that should always be true;
  - `assert isinstance(10, int), 'Expected int'` - e.g.
- 'smoke test';
- `unittest` module;
  - `unittest.TestCase` subclass for testing;
  - assertion types![[Pasted image 20231025100830.png]]
  - [`pytest` module](https://docs.pytest.org/en/latest/);
  - test example
    ![[Pasted image 20231025103519.png]]
- `logging` module;
  - logging in `except` block;
  - perform startup configuration, get logger, and start logging;
- debugging
  - pasting the whole traceback into Google;
  - _REPL_ - `-i` flag when running;
  - `print` with `repr`;
  - `breakpoint()` and `pdb.set_trace()` from `pdb` module
  - `-m` - run in debugger;

### 9. Packages

- `import` _loads_ and _executes_ a module;
- package - namespace for imports
  ![[Pasted image 20231025104728.png]]
- 2 problems
  - imports in the package modules break;
    - all imports are absoulute;
  - main scripts break;
    - solution:![[Pasted image 20231025105122.png]]
    - another solution - top-level scripts:![[Pasted image 20231025105443.png]]
  - `__init__.py` - make names top level;
  - common code organization
    ![[Pasted image 20231025105404.png]]
- [PyPi](https://pypi.org/) - python package index;
- using `pip` for installing 3rd party packages;
- virtual environments;
- [packaging and distribution guide](https://packaging.python.org/en/latest/);
- [how a venv works](https://realpython.com/python-virtual-environments-a-primer/);
- distribution of code;
  - toplevel `setup.py`;
    ![[Pasted image 20231025110810.png]]
  - `MANIFEST.in` for additional files;
  - `bash % python setup.py sdist` - creates `.tar.gz`/`.zip`;

---

## Outline - What have I learned

- _basic_
  - basic datatypes;
  - working with strings and lists;
  - working with textual files;
  - writing functions;
- _built-in data structures_
  - containers - sets, lists, dicts;
  - formatted output - `f''`;
  - slicing, iterating, replicating, `zip()` - sequences;
  - `Counter`, `defaultdict` - from `collections`;
  - list, dict comprehensions;
  - references, shallow and deep copies, type-checking;
  - first-class data - functions, types, ...;
- _code organization_
  - doc-strings;
  - keyword args - prefer for optional;
  - exceptions and `try-except-finally`;
  - `with` statement;
  - modules (files, namespaces) and `import` statement;
    - how are modules located - `sys.path`;
  - `__name__ == '__main__'` - main module;
  - `sys`, `os` - interacting with CLI arguments, standard I/O, env. vars;
  - `#!/usr/bin/env python3`;
- _oop_
  - class definition;
  - `__init__` method;
  - `self` argument;
  - instance methods;
  - inheritance;
  - overriding and `super()`;
  - `object` base class;
  - multiple inheritance;
  - magic methods - `__init__`, `__repr__`, `__str__`, arithmetic, item access;
  - bound methods;
  - `getattr` and `setattr`;
  - user defined exceptions;
- _oop under the hood_
  - local instance and class dicts;
  - `del` operator;
  - `__MRO__` and C3 linerization;
  - mixin pattern;
  - private attributes and `@property`;
  - `__slots__` attribute;
- _generators_
  - iterables and iterators - `__iter__()` and `__next__()`;
  - `yield` keyword;
  - producer-processing-consumer - pipeline architecture;
  - generator expressions;
  - `count`, `takewhile` - itertools` module;
- _advanced topics_
  - `*args` (tuple) and `**kwargs` (dict);
  - `lambda` functions;
  - higher order (first class) functions;
  - closures;
  - delayed (lazy) evaluation;
    - `typedproperty` example - avoid code repetition;
  - function wrappers - decorators;
  - `@staticmethod`, `@classmethod` and `cls`;
- _testing and debugging_
  - native `assert`;
  - unit testing - `unittest.TestCase` class - `unittest` module;
  - logging - `logging` module (setup, logger, logging);
  - debugging - `breakpoint()`, `pdb.set_trace()`, `-m` option;
- _packages_
  - concept of packages;
  - 2 main problems with packages - module imports and main scripts;
  - `__init__.py` file - top level imports;
  - top level scripts - running main submodules;
  - `sys.path` - module search;
  - `pip` installer;
  - virtual environments - `python3 -m venv`;
  - code distribution `setup.py` - `setuptools` module;
  - `MANIFEST.in` configuration file for additional resources;

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
	- **`dict(zip(column_names, values))`** => genious;
	- `pprint(dict(zip(prices.values(), prices.keys())))` - inverting a dict;
	- `zip()` stops once shortest input sequence gets exhausted;
- [`collections` module](https://docs.python.org/3/library/collections.html) - `Counter`, `defaultdict`, `deque`;
- list comprehensions - creating new lists, filtering;
  ![[Pasted image 20231023143038.png]]
- sequence reductions + list comprehensions - `sum(comprehension)`;
- set comprehension - exchange `[]` with a `{}`;
- dictionary comprehension => specify _key:value_;
- `is` operator - checking if two values refer to the same object;
- `id()` function;
- shallow copies - `list()`;
- deep copy - `copy` module => `copy.deepcopy(obj)`;
- `type()`;
- `isinstance(obj, tuple_of_types)`;
- first-class objects;
- zip + types;

## Program organization

- functions are blackboxes - no logic leaks;
- doc-string;
- type annotations;
- python runs faster with use of functions;
- named arguments call;
- default arguments;
- `None` is returned by default;
- global and local variables;
- all assignments in functions are local;
- `global <var_name>`;
- EXERCISE => `parse_csv` function - work with headers, types, and selectors, for arbitrary csv formats;
- built-in exceptions
  ![[Pasted image 20231023152341.png]]
- `Exception`  - root of exception hierarchy, do avoid;
- re-raising the exception;
- `finally` statement - safe resource management;
- `with` statement - `try-finally`;
- silencing errors;
- any python source file is a module;
- 
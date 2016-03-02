# Tuples

A ordered sequence of elements. (An array?)

```
someTuple = (1, 'four', False, 'lol', 123)
print someTuple[0] # === 1
print someTuple[1] # === 'four'

# You can use the slicing syntax:
print someTuple[1:3] # === ('four', False)
```

You can concatenate tuples:

```
fooTuple = (1, 2, 'foo')
barTuple = (3, 4, 'bar')
bothTuple = fooTuple + barTuple
```

Differentiating a tuple from a value:

```
(3) === 3     # an Int
(3,) === (3,) # a Tuple -- trailing comma is always present for tuples with 1 value

Tuples are immutable!

# Lists

They use square brackets instead of parens:

```
someTuple = (1, 2, 3)
someList  = [1, 2, 3]
```

Lists have an `.append` method:

```
someList.append('foo') # And of course this mutates someList rather than creating a new List
```

## Operations on Lists

Iteration:

```
for item in someList:
	# do something with item
```

Concatenating (*Creates a new copy of all the data!*)

```
masterList = subList1 + subList2 # You can mutate subList1 without mutating masterList
```

Removing elements:

```
someList.remove(2) # Remove the first item from the list whose value is 2.
```

# Functions

They're objects
They're first class citizens
They can appear in expressions

# Dictionaries

A generalization of a list, but now indices don't have to be integers; they can be any immutable value type like strings or tuples. (But why would you use tuples?)

Syntax:

```
someDict = {'foo': 1, 'bar': 2}
someDict['foo'] # 1
```

You can get keys: someDict.keys()
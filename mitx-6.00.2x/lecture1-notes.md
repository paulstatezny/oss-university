# Function Defaults

In Python, function parameters can have defaults as in other languages:

```
def foo(bar, baz, qux = 100):
    # Qux is defaulted to 100 if not provided

foo(100, 200) # Qux is 100
foo(100, 200, 300) # Qux is 300 this time
```

Also, when there are multiple defaults you can specify them by name to single out only 1 or 2:

```
def foo(bar, baz, qux = 100, food = 'yes', barn = 'red', bass = 'fish', quacks = 'ducks'):
    # Do stuff

foo(100, 200, barn = 'blue') # Look, I'm only giving barn but not food
```

You can even choose to use that syntax with non-defaulted variables, and in whatever order:

```
foo(bass = 'lol', baz = 'whatever', quacks = 'duckies', bar = True)
```
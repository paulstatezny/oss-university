# Testing

Blackbox testing -- testing the code without looking into the implementation.
Glass box testing -- testing with a view into the code in order to (1) make it path complete [100% line coverage] and (2) identify boundary cases.

## Glass box Testing

For loops and recursive functions, test conditions where the loop/recursion will happen 0 times, 1 time, and many times.

## Picking good inputs

You should pick both:
1. Normal/expected inputs
2. Edge/boundary cases

## Types of Tests

1. Unit tests
2. Integration tests

Cycle in between these types of tests until you're convinced that the code is defect free.

3. Regression testing -- necessary after you've verified that the code works and then later changed the code.

## Test Drivers and Stubs

A test driver is a piece of code that does testing for us.

## Runtime bugs

Overt vs. Covert: Overt bugs have an obvious manifestation. With covert bugs, it's not obvious that they're happening.

Persistent vs. Intermittent: Persistent means it always happens, intermittent means it only happens sometimes.

Intermittent, covert bugs are the scariest. *Defensive programming* helps us protect ourselves against those bugs.

## Debugging skills

- Treat it as a search problem. Form a hypothesis.
- Use print statements, lol
- Use the principle of bisection search -- when you're not sure about the location of a bug, just put a print statement in the very middle of the code and check if the variables contain values you expect. This will eliminate locations in the code where the bug might be.

## Aliasing Bugs

By-reference bugs where 2 variables point to the same object, and you mutate both while trying to mutate one.

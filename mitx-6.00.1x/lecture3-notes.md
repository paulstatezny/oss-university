# Newton-Raphson Root Finding Algorithm

Searching for the root of a polynomial.
A polynomial is, e.g. p(x) = 5x^4 + 8x^3 + -24x^2 + x + 5
In high school we mainly did quadratic polynomials like f(x) = 5x^2 + 2x - 12

The Newton-Raphson algothim is about finding a value of X such that p(x) == 0 (The "root" of the polynomial)
Calculus -- the *derivative* of f(x) [i.e. f'(x)] is the "rate of change" e.g. measuring the slope of f(x).

The Newton-Raphson algorithm: g - p(g) / p'(g)
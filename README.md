# Lagrangian Polynomial

## Coordinates

$$
(0; 60), (-2; 0), (3; 0), (4; -12)
$$

$$


$$

## Formulas

$$
\ell_{i}(x)= \prod_{k=0,k\not ={i} }^{n}{\frac{(x-x_{k})}{(x_{i}-x_{k})}}
$$

$$
    L(x) = \sum_{i=0}^{n}y_{i} \cdot \ell_{i}(x)
$$

## Example

$$
\frac{(x+2)(x-3)(x-4)}{(0+2)(0-3)(0-4)} \cdot 60 + \frac{(x-0)(x-3)(x-4)}{(-2-0)(-2-3)(-2-4)} \cdot 0 + \frac{(x-0)(x+2)(x-4)}{(3-0)(3+2)(3-4)} \cdot 0 + \frac{(x-0)(x+2)(x-3)}{(4-0)(4+2)(4-3)} \cdot (-12)
$$

$\Leftrightarrow$

$$
\frac{(x+2)(x-3)(x-4)}{(0+2)(0-3)(0-4)} \cdot 60 + \frac{(x-0)(x+2)(x-3)}{(4-0)(4+2)(4-3)} \cdot (-12)
$$

$\Leftrightarrow$

$$
\frac{(x+2)(x-3)(x-4)}{2\cdot(-3)\cdot(-4)} \cdot 60 + \frac{x(x+2)(x-3)}{4\cdot6\cdot1} \cdot (-12)
$$

$\Leftrightarrow$

$$
\frac{(x+2)(x-3)(x-4)}{24} \cdot 60 + \frac{x(x+2)(x-3)}{24} \cdot (-12)
$$

$\Leftrightarrow$

$$
\frac{(x+2)(x-3)(x-4)}{2} \cdot 5 + \frac{x(x+2)(x-3)}{2} \cdot (-1)
$$

$\Leftrightarrow$

$$
\frac{(x^2-x-6)(x-4)}{2} \cdot 5 + \frac{x(x^2-x-6)}{2} \cdot (-1)
$$

$\Leftrightarrow$

$$


$$

## Answer

$$
60 - 2x -12x^2 + 2x^3 \Leftrightarrow [2, -12, -2, 60]
$$

# Solution

```python
def lagrange_polynomial(lst_points: List[Tuple[float, float]]) -> List[float]:
    '''
    Function that returns a list of coefficients representing a polynomial of
    deg(N) given (N + 1) points.

    Parameters:
    - lst_points: List[Tuple[float, float]] -> a list of coordinates
    '''

    lst_coeffs = []
    res = []

    for i in range(0, len(lst_points)):
        numerator_pol = []
        denominator = 1
        product_tmp = lst_points[i][1]

        for j in range(0, len(lst_points)):
            if j != i:
                numerator_pol.append([(-1) * lst_points[j][0], 1])
                denominator *= lst_points[i][0] + ((-1) * lst_points[j][0])

        for p in range(len(numerator_pol)):
            # Resetting the index for each iteration
            p = 0
            if p + 1 < len(numerator_pol):
                numerator_pol[p] = multiplication(
                    numerator_pol[p], numerator_pol[p+1])
                numerator_pol.remove(numerator_pol[p+1])

        for coeff in range(len(numerator_pol[0])):
            numerator_pol[0][coeff] *= product_tmp
            numerator_pol[0][coeff] /= denominator
        lst_coeffs.append(numerator_pol[0])

    for poly_coeff in range(len(lst_coeffs)):
        # Resetting the index for each iteration
        poly_coeff = 0
        if poly_coeff + 1 < len(lst_coeffs):
            lst_coeffs[poly_coeff] = addition(
                lst_coeffs[poly_coeff], lst_coeffs[poly_coeff + 1])
            lst_coeffs.remove(lst_coeffs[poly_coeff + 1])

    res = lst_coeffs[0]
    res.reverse()

    return res

```

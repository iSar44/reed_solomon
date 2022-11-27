from pol_op import addition, multiplication
from typing import Tuple, List


def solve_polynomial(lst_coeffs: List[float], x: float) -> float:
    '''
    Function that returns the value of polynomial given an input x.

    Parameters:
    - lst_coeffs: List[float] -> a list of coefficients representing
    a polynomial (the list starts with the coefficient associated with
    the highest degree of the polynomial)

    - x: float -> value at which the user wants to evaluate the given
    polynomial
    '''

    lst_pows = []
    res = 0

    for coeff in range(len(lst_coeffs)):
        lst_pows.append(coeff)

    lst_pows.reverse()

    for (index, coeff) in enumerate(lst_coeffs):

        res += coeff * (x ** lst_pows[index])

    return res


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


def main():

    lst_coeffs = [2, 34, 121, 3, 54]
    lst_points = [(0, 60), (-2, 0), (3, 0), (4, -12)]
    # lst_points = [(0, 2), (1, 34), (2, 121), (3, 3), (4, 54)]

    print(solve_polynomial(lst_coeffs, 1))
    res = lagrange_polynomial(lst_points)
    print(res)


main()

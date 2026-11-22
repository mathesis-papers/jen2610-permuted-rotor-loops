#!/usr/bin/env python3
"""Exact finite polynomial identities for permuted rotor loops."""

from fractions import Fraction
from itertools import combinations, permutations, product
from math import comb


def blade_product(left, right, signature):
    coefficient = 1
    for index, square in enumerate(signature):
        if left & (1 << index):
            if (right & ((1 << index) - 1)).bit_count() % 2:
                coefficient = -coefficient
            if right & (1 << index):
                coefficient *= square
    return left ^ right, coefficient


def nonzero(entries):
    return {key: value for key, value in entries.items() if value}


def multiply_multivectors(left, right, signature):
    result = {}
    for left_mask, left_value in left.items():
        for right_mask, right_value in right.items():
            mask, sign = blade_product(left_mask, right_mask, signature)
            result[mask] = result.get(mask, 0) + sign * left_value * right_value
    return nonzero(result)


def word_coefficients(family, order, signature):
    coefficients = {(0, 0): 1}
    word = [(index, 1) for index in range(len(family))]
    word += [(index, -1) for index in order]
    for index, factor_sign in word:
        updated = {}
        for (mask, exponent), value in coefficients.items():
            key = mask, exponent
            updated[key] = updated.get(key, 0) + value
            for family_mask, family_value in family[index].items():
                new_mask, sign = blade_product(mask, family_mask, signature)
                key = new_mask, exponent + 3 ** index
                updated[key] = updated.get(key, 0) + value * factor_sign * family_value * sign
        coefficients = nonzero(updated)
    return coefficients


def subset_formula(signature, order):
    count = len(signature)
    positions = {index: position for position, index in enumerate(order)}
    expected = {}
    for mask in range(1 << count):
        subset = [index for index in range(count) if mask & (1 << index)]
        size = len(subset)
        inversion_count = sum(positions[left] > positions[right]
                              for left, right in combinations(subset, 2))
        coefficient = (-1) ** (size * (size + 1) // 2 + inversion_count)
        for index in subset:
            coefficient *= signature[index]
        exponent = sum(2 * 3 ** index for index in subset)
        expected[exponent] = coefficient
    return expected


def check_formal(count, signature, order):
    family = [{1 << index: 1} for index in range(count)]
    actual = word_coefficients(family, order, signature)
    scalar = {exponent: value for (mask, exponent), value in actual.items() if mask == 0}
    assert scalar == subset_formula(signature, order), ('scalar', signature, order)
    if count % 2:
        full = (1 << count) - 1
        assert not any(mask == full for mask, exponent in actual), ('odd support', signature, order)


def check_exterior(count, order):
    coefficients = {0: 1}
    word = [(index, 1) for index in range(count)]
    word += [(index, -1) for index in order]
    for index, factor_sign in word:
        updated = dict(coefficients)
        for mask, value in coefficients.items():
            if not mask & (1 << index):
                result_mask, sign = blade_product(mask, 1 << index, (0,) * count)
                updated[result_mask] = updated.get(result_mask, 0) + value * factor_sign * sign
        coefficients = nonzero(updated)
    assert all(mask.bit_count() % 2 == 0 for mask in coefficients), ('exterior', count, order)


def check_trace_support(count, signature):
    for mask in range(1, 1 << count):
        if count % 2 and mask == (1 << count) - 1:
            continue
        witnesses = []
        for index, square in enumerate(signature):
            first_mask, first_sign = blade_product(1 << index, mask, signature)
            final_mask, final_sign = blade_product(first_mask, 1 << index, signature)
            assert final_mask == mask
            witnesses.append(first_sign * final_sign * square)
        assert -1 in witnesses, ('trace support', signature, mask)


def check_geometric(family, signature):
    for index, element in enumerate(family):
        assert all(mask.bit_count() == 2 for mask in element)
        assert multiply_multivectors(element, element, signature) == {0: -1}
        for other in family[:index]:
            forward = multiply_multivectors(element, other, signature)
            backward = multiply_multivectors(other, element, signature)
            assert forward == {mask: -value for mask, value in backward.items()}
    full = {0: 1}
    for element in family:
        full = multiply_multivectors(full, element, signature)
    assert full == {0: -1}
    total = 0
    for order in permutations(range(len(family))):
        actual = word_coefficients(family, order, signature)
        scalar = {exponent: value for (mask, exponent), value in actual.items() if mask == 0}
        assert scalar == subset_formula((-1,) * len(family), order)
        total += 1
    return total


def evaluate_subset(signature, order, cosine_squares, sine_squares):
    result = Fraction(0)
    for exponent, coefficient in subset_formula(signature, order).items():
        term = Fraction(coefficient)
        for index in range(len(signature)):
            term *= sine_squares[index] if exponent // 3 ** index % 3 else cosine_squares[index]
        result += term
    return result


def check_mixed_compact():
    total = 0
    for count in range(1, 7):
        for signature in product((-1, 1), repeat=count):
            for sample in range(3):
                weights = [Fraction(0) if sample == 0 else
                           Fraction((index + sample) % 4, 3 if square == -1 else 2)
                           for index, square in enumerate(signature)]
                cosine_squares = [1 + square * weight for square, weight in zip(signature, weights)]
                real_part, imaginary_part = Fraction(1), Fraction(0)
                for square, cosine_square, weight in zip(signature, cosine_squares, weights):
                    imaginary = square * weight
                    real_part, imaginary_part = (real_part * cosine_square - imaginary_part * imaginary,
                                                 real_part * imaginary + imaginary_part * cosine_square)
                actual = evaluate_subset(signature, tuple(range(count)), cosine_squares, weights)
                assert actual == real_part - imaginary_part, ('mixed compact', signature, sample)
                assert all(cosine_square or weight for cosine_square, weight in zip(cosine_squares, weights))
                total += 1
    assert total == 378
    return total


def graph_components(count, edges):
    components = []
    remaining = set(range(count))
    while remaining:
        component = {min(remaining)}
        while True:
            expanded = component | {endpoint for edge in edges if component.intersection(edge)
                                    for endpoint in edge}
            if expanded == component:
                break
            component = expanded
        remaining -= component
        components.append(component)
    return components


def check_graphs():
    orders = vertices = 0
    for count in range(1, 7):
        for order in permutations(range(count)):
            positions = {index: position for position, index in enumerate(order)}
            edges = [(left, right) for left, right in combinations(range(count), 2)
                     if positions[left] < positions[right]]
            assert bool(edges) == (order != tuple(reversed(range(count))))
            components = graph_components(count, edges)
            diagonal = subset_formula((-1,) * count, order)
            for mask in range(1 << count):
                subset = {index for index in range(count) if mask & (1 << index)}
                induced = sum(left in subset and right in subset for left, right in edges)
                exponent = sum(2 * 3 ** index for index in subset)
                assert diagonal[exponent] == (-1) ** induced
                separated = sum(sum(left in subset.intersection(component) and
                                    right in subset.intersection(component) for left, right in edges)
                                for component in components)
                assert induced == separated
                vertices += 1
            if edges:
                left, right = edges[0]
                weights = [Fraction(0)] * count
                weights[left], weights[right] = Fraction(1), Fraction(1, 2)
                assert evaluate_subset((-1,) * count, order, [1 - weight for weight in weights], weights) == 0
            orders += 1
    assert orders == 873 and vertices == 50362
    return orders, vertices


def normalized_parameters(squares, sample):
    result = []
    for index, square in enumerate(squares):
        if sample == 0:
            parameter = Fraction(0)
        elif sample == 1:
            parameter = Fraction(index + 1, 7)
        else:
            parameter = Fraction(1) if square == -1 and index == 0 else Fraction(1, 2)
        denominator = 1 - square * parameter ** 2
        cosine = (1 + square * parameter ** 2) / denominator
        sine = 2 * parameter / denominator
        assert cosine ** 2 - square * sine ** 2 == 1
        result.append((cosine, sine))
    return result


def normalized_loop(family, order, signature, parameters):
    result = {0: Fraction(1)}
    word = [(index, 1) for index in range(len(family))]
    word += [(index, -1) for index in order]
    for index, factor_sign in word:
        cosine, sine = parameters[index]
        factor = {mask: factor_sign * sine * coefficient for mask, coefficient in family[index].items()}
        factor[0] = cosine
        result = multiply_multivectors(result, nonzero(factor), signature)
    return result


def check_short_loop(family, squares, signature, order, sample):
    rotor = normalized_loop(family, order, signature, normalized_parameters(squares, sample))
    assert all(mask.bit_count() in (0, 2) for mask in rotor), ('short grades', order, sample)
    reverse = {mask: coefficient * (-1) ** (mask.bit_count() * (mask.bit_count() - 1) // 2)
               for mask, coefficient in rotor.items()}
    assert multiply_multivectors(rotor, reverse, signature) == {0: 1}
    scalar = rotor.get(0, 0)
    expected_square = {mask: 2 * scalar * coefficient for mask, coefficient in rotor.items()}
    expected_square[0] = expected_square.get(0, 0) - 1
    assert multiply_multivectors(rotor, rotor, signature) == nonzero(expected_square)
    current_power = {0: Fraction(1)}
    previous, current = Fraction(1), scalar
    for exponent in range(9):
        target = Fraction(1) if exponent == 0 else current
        assert current_power.get(0, 0) == target, ('Chebyshev', order, sample, exponent)
        if exponent:
            previous, current = current, 2 * scalar * current - previous
        current_power = multiply_multivectors(current_power, rotor, signature)


def check_short_powers():
    total = 0
    for count in range(1, 4):
        family = [{1 | (1 << (index + 1)): 1} for index in range(count)]
        for squares in product((-1, 1), repeat=count):
            signature = (-1,) + squares
            for order in permutations(range(count)):
                for sample in range(3):
                    check_short_loop(family, squares, signature, order, sample)
                    total += 1
    triangle = [{3: 1}, {5: 1}, {6: 1}]
    rotated = [{3: Fraction(3, 5), 5: Fraction(4, 5)},
               {3: Fraction(-4, 5), 5: Fraction(3, 5)}, {6: 1}]
    for family in [triangle, rotated]:
        for order in permutations(range(3)):
            for sample in range(3):
                check_short_loop(family, (-1,) * 3, (-1,) * 3, order, sample)
                total += 1
    assert total == 210
    return total


def check_four_factor_boundary():
    signature = (-1,) * 5
    family = [{1 | (1 << index): 1} for index in range(1, 5)]
    result = {0: Fraction(1)}
    for factor_sign in (1, -1):
        for element in family:
            factor = {0: 1, **{mask: factor_sign * coefficient for mask, coefficient in element.items()}}
            result = multiply_multivectors(result, factor, signature)
    result = {mask: coefficient / 16 for mask, coefficient in result.items()}
    grade_four = {mask: coefficient for mask, coefficient in result.items() if mask.bit_count() == 4}
    assert grade_four == {15: Fraction(1, 4), 23: Fraction(-1, 4), 27: Fraction(1, 4),
                          29: Fraction(-1, 4), 30: Fraction(1, 4)}
    assert result[0] == Fraction(-1, 4)
    assert multiply_multivectors(result, result, signature)[0] == Fraction(-1, 4)
    assert 2 * result[0] ** 2 - 1 == Fraction(-7, 8)


def check_equal_weight_sequence():
    previous, current = 0, 1
    for count in range(65):
        expected = sum(comb(count, size) * (-1) ** (size * (size + 3) // 2)
                       for size in range(count + 1))
        assert expected == current
        previous, current = current, 2 * current - 2 * previous


def main():
    formal_total = exterior_total = mixed_total = 0
    for count in range(1, 7):
        signature = (-1,) * count
        check_trace_support(count, signature)
        orders = 0
        for order in permutations(range(count)):
            check_formal(count, signature, order)
            check_exterior(count, order)
            orders += 1
        formal_total += orders
        exterior_total += orders
        print(f'SQUARE_MINUS_ONE k={count}: {orders} exact polynomial identities')
    assert formal_total == exterior_total == 873
    print('EXTERIOR_PARITY: 873 return orders, every odd-degree coefficient zero')
    for count in range(1, 5):
        for signature in product((-1, 1), repeat=count):
            check_trace_support(count, signature)
            for order in permutations(range(count)):
                check_formal(count, signature, order)
                mixed_total += 1
    assert mixed_total == 442
    print('MIXED_SIGNS k=1..4: 442 exact polynomial identities')
    triangle = [{3: 1}, {5: 1}, {6: 1}]
    rotated = [{3: Fraction(3, 5), 5: Fraction(4, 5)},
               {3: Fraction(-4, 5), 5: Fraction(3, 5)}, {6: 1}]
    assert check_geometric(triangle, (-1, -1, -1)) == 6
    assert check_geometric(rotated, (-1, -1, -1)) == 6
    print('NON_STAR_TRIANGLES: 12 exact identities; full product equals -1')
    print(f'MIXED_COMPACT k=1..6: {check_mixed_compact()} exact rational cases')
    graph_orders, graph_vertices = check_graphs()
    print(f'PERMUTATION_GRAPHS k=1..6: {graph_orders} orders, {graph_vertices} vertex signs and component factorizations')
    short_total = check_short_powers()
    print(f'SHORT_LOOPS k=1..3: {short_total} exact normalized loops, scalar-plus-bivector and quadratic identities')
    print(f'CHEBYSHEV_POWERS n=0..8: {short_total * 9} exact scalar identities')
    check_four_factor_boundary()
    print('FOUR_FACTOR_BOUNDARY: scalar=-1/4, squared scalar=-1/4, T2(scalar)=-7/8, five grade-four coefficients of magnitude 1/4')
    check_equal_weight_sequence()
    print('EQUAL_WEIGHT_SEQUENCE k=0..64: 65 exact signed binomial sums equal A009545(k+1)')
    print('SCOPE: finite polynomial coefficient comparisons and exact rational geometric cases')
    print('ALL_CHECKS_OK')


if __name__ == '__main__':
    main()

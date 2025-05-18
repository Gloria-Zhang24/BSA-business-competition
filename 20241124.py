def maximize_s_given_a(year, total_a):
    """
    Maximize S by distributing total A into A1, A2, A3 under given constraints.

    :param year: Fiscal year (1, 2, 3, or 4).
    :param total_a: Total quantity of items (A = A1 + A2 + A3).
    :return: Tuple (A1, A2, A3, max_S) where max_S is the maximum S.
    """
    best_a1, best_a2, best_a3 = 0, 0, 0
    max_s = 0

    year_factor = (year + 1) * 5

    # Iterate over all possible A1 and A2 values, A3 is determined by total_a - A1 - A2
    for a1 in range(total_a + 1):
        e1 = a1 / year_factor
        s1 = e1  # S1 = E1

        for a2 in range(total_a - a1 + 1):
            e2 = a2 / year_factor
            s2 = (e1 * e2) / 100  # S2 = E1 * E2 / 100

            a3 = total_a - a1 - a2
            e3 = a3 / year_factor
            s3 = (e1 * e3) / 75  # S3 = E1 * E3 / 75

            # Total S
            s = s1 + s2 + s3

            # Update the best result if a higher S is found
            if s > max_s:
                best_a1, best_a2, best_a3 = a1, a2, a3
                max_s = s

    return best_a1, best_a2, best_a3, max_s

# Example: Test with year=1 and total A=50
year = 1
total_a = 50
maximize_s_given_a(year, total_a)

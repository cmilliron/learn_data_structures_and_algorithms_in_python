def power_set(input):
    # intialize empty subsets.
    all_subsets = [[]]
    if len(input) == 0:
        return all_subsets
    for i in input:
        new_subset = []
        for subsets in all_subsets:
            temp_list = [i]
            temp_list.extend(subsets)
            new_subset.append(temp_list)
        all_subsets.extend(new_subset)
    return all_subsets

"""
Solution from class

def power_set(input):
    if len(input) == 0:
        return [[]]

    all_subsets = [[]]
    for element in input:
        new_subsets = []
        for subset in all_subsets:
            new_subsets.append(subset + [element])
        all_subsets.extend(new_subsets)
    return all_subsets


"""


# ---------------------- Test Data -----------------------

run_cases = [
    ([1, 2], [[], [1], [2], [1, 2]]),
    ([1, 2, 3], [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]),
]

submit_cases = run_cases + [
    ([], [[]]),
    ([1], [[], [1]]),
    (
        [1, 2, 3, 4],
        [
            [],
            [1],
            [2],
            [1, 2],
            [3],
            [1, 3],
            [2, 3],
            [1, 2, 3],
            [4],
            [1, 4],
            [2, 4],
            [1, 2, 4],
            [3, 4],
            [1, 3, 4],
            [2, 3, 4],
            [1, 2, 3, 4],
        ],
    ),
]


def test(input1, expected_output):
    print("---------------------------------")
    print(f"Inputs:")
    for i in input1:
        print(f" * {i}")
    print(f"Expected: {expected_output}")
    result = power_set(input1)
    print(f"Actual:   {result}")
    sorted_result = sorted([sorted(inner) for inner in result])
    sorted_expected_output = sorted([sorted(inner) for inner in expected_output])
    if sorted_result == sorted_expected_output:
        print("Pass")
        return True
    print("Fail")
    return False


def main():
    passed = 0
    failed = 0
    skipped = len(submit_cases) - len(test_cases)
    for test_case in test_cases:
        correct = test(*test_case)
        if correct:
            passed += 1
        else:
            failed += 1
    if failed == 0:
        print("============= PASS ==============")
    else:
        print("============= FAIL ==============")
    if skipped > 0:
        print(f"{passed} passed, {failed} failed, {skipped} skipped")
    else:
        print(f"{passed} passed, {failed} failed")


test_cases = submit_cases
if "__RUN__" in globals():
    test_cases = run_cases

main()

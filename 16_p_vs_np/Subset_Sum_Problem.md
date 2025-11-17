Assignment

Complete the subset_sum function.

It should take a list of integers nums and an integer target, and return True if there exists a subset of nums that adds up to target, and False otherwise. We'll use a recursive, brute-force approach to solve the problem. Brute-force just means we'll try every possible combination to see if any of them add up to the target.
Pseudocode: subset_sum(nums, target)
Inputs

    nums: A list of integers representing the follower counts of influencers.
    target: The target sum we want to find a subset for.

Output

True if there exists a subset of nums that adds up to target. False otherwise.
Algorithm

    Call the helper function starting with the last index in nums and return its result.

Pseudocode: find_subset_sum(nums, target, index)
Inputs

    nums: A list of integers representing the follower counts of influencers.
    target: The target sum we want to find a subset for.
    index: The index of the current element we're considering.

Output

True if there exists a subset of nums that adds up to target. False otherwise.
Algorithm

    If the target is 0, return True.
    If the index is less than 0 and the target is not 0, return False.
    If the number at the current index is greater than the target, call the helper function with the same target but with the index decremented by 1, and return the result, we're done.
    Otherwise, call the helper function with the same target and index decremented by 1, and save the result.
    Also, call the helper function with the target reduced by the value of the current element and the index decremented by 1
    If either of these calls returns True, return True. Otherwise, return False.

<!--  -->

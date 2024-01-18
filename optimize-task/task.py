def find_sum_pairs_n2(nums, target):
    """Finds all pairs in a list that sum to a target, using nested loops (O(n^2) complexity)."""
    pairs = []
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                pairs.append((nums[i], nums[j]))
    return pairs


# Question: Can you optimize this code to achieve a time complexity of O(N)?

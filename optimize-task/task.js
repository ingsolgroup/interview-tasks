/**
 * Finds a pair in given array that sums to a target
 * @param {Number[]} nums
 * @param {Number} target
 */
function findPairs(nums, target) {
  for (let i = 0; i < nums.length; i++) {
    for (let j = i + 1; j < nums.length; j++) {
      if (nums[i] + nums[j] == target) {
        return [nums[i], nums[j]];
      }
    }
  }
}

// Question: Can you optimize this code to achieve a time complexity of O(N)?

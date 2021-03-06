'''
Problem: Three Sum
algorithm:
    sort items and find the middle point
tags: sort and find
'''


class Solution:
    @classmethod
    # Time: O(n)
    # Space: O(n)
    def solve(self, problems):
        # Solution here
        nums, target = problems

        def quick_sort(array):
            def partition(array, low, high):
                pivot = array[low]
                i, j = low, high
                while i < j:
                    while i <= high and array[i] <= pivot:
                        i += 1
                    while j >= low and array[j] > pivot:
                        j -= 1
                    if i < j:
                        array[i], array[j] = array[j], array[i]
                array[low], array[j] = array[j], array[low]
                return j

            def qst_rec(array, low, high):
                if low < high:
                    pivot = partition(array, low, high)
                    qst_rec(array, low, pivot - 1)
                    qst_rec(array, pivot + 1, high)

            qst_rec(array, 0, len(array) - 1)
            return
        quick_sort(nums)

        result = []
        for i in range(len(nums) - 2):
            j = i + 1
            k = len(nums) - 1
            while j < k:
                if nums[i] + nums[j] + nums[k] > target:
                    k -= 1
                elif nums[i] + nums[j] + nums[k] < target:
                    j += 1
                else:
                    item = [nums[i], nums[j], nums[k]]
                    if item not in result:
                        result.append(item)
                    k -= 1
                    j += 1
        return result

# Think:

# ReThink:

# Summary:

    @classmethod
    # Time: O(n)
    # Space: O(n)
    def better_solve(self, problems):
        # Solution here
        pass

if __name__ == '__main__':
    problems = [-1, 0, 1, 2, -1, -4], 0  # input
    r = [[-1, 0, 1], [-1, -1, 2]].sort()
    result = Solution.solve(problems)

    print result
    assert result.sort() == r, "Solution Error."  # output check

    print "problems solved."

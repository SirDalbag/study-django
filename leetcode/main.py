# TODO Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
def searchInsert(nums: list[int], target: int) -> int:
    if target in nums:
        return sorted(nums).index(target)
    else:
        nums.append(target)
        return sorted(nums).index(target)


# TODO Given a string s consisting of words and spaces, return the length of the last word in the string.
def lengthOfLastWord(s: str) -> int:
    s = s.split()
    return len(s[len(s) - 1])

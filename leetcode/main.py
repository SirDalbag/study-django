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


# TODO Given an integer, convert it to a roman numeral.
def intToRoman(num: int) -> str:
    values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    symbols = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    result = ""
    for i, value in enumerate(values):
        while num >= value:
            num -= value
            result += symbols[i]
    return result

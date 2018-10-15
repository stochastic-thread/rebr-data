def lengthOfLongestSubstring(str):
    seen = dict()
    for i, c in enumerate(str):
        if seen[c] is None:
            seen[c] = 1
        else:
            seen[c] += 1

        if seen[str[0:i]] is None:
            seen[str[0:i]] = 1
        else:
            seen[str[0:i]] += 1
    return (None, seen)


def main():
    testCases = dict()
    testCases["abcabcbb"] = ("abc", 3)
    testCases["bbbbb"] = ("b", 1)
    testCases["pwwkew"] = ("wke", 3)

    for i, k in enumerate(testCases):
        strAnswer, strLen = lengthOfLongestSubstring(k)
        correctStr, correctLen = testCases[k]
        if strAnswer == correctStr and strLen == correctLen:
            return "A+"

print(main())
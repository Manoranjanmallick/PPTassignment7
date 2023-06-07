def reverseStr(s, k):
    chars = list(s)
    n = len(chars)

    for i in range(0, n, 2 * k):
        start = i
        end = min(i + k - 1, n - 1)

        while start < end:
            chars[start], chars[end] = chars[end], chars[start]
            start += 1
            end -= 1

    return "".join(chars)

s = "abcdefg"
k = 2
print(reverseStr(s, k))

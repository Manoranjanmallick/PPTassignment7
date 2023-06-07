def reverseWords(s):
    words = s.split()
    reversed_words = [word[::-1] for word in words]

    reversed_sentence = " ".join(reversed_words)

    return reversed_sentence

s = "Let's take LeetCode contest"
print(reverseWords(s))

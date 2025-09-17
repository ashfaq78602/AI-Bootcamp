def revString(phrase):
    return phrase[::-1]

def countVowels(phrase):
    # count = 0
    # vowels = "aeiouAEIOU"
    # for char in phrase:
    #     if char in vowels:
    #         count += 1
    # return count
    count = 0
    count = sum(1 for c in phrase if c.lower() in "aeiou")
    return count

def checkStrictPalindrome(phrase):
    # reversed = revString(phrase)
    # for i in range(len(phrase)):
    #     if reversed[i] != phrase[i]:
    #         return "Not palindrom"
    # return "Palindrome"
    if phrase == phrase[::-1]:
        return "Strictly Palindrome"
    else:
        return "Not Strictly Palindrome"

def checkLenientPalindrome(phrase):
    clean = ''.join(c.lower() for c in phrase if c.isalnum())
    if clean == clean[::-1]:
        return "Palindrome"
    else: 
        return "Not Palindrome"
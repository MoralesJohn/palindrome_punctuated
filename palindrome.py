import string

# returns true if string contains no alpha
def is_palindrome(s):
    length = len(s)
    if length < 2:
        return True
    left_ndx = -1
    right_ndx = length
    result = True
    while result and left_ndx < right_ndx:
        left_ndx += 1
        left_char = s[left_ndx]
        right_ndx -= 1
        right_char = s[right_ndx]
        while left_char not in string.ascii_letters and left_ndx < right_ndx:
            left_ndx += 1
            left_char = s[left_ndx]
        while right_char not in string.ascii_letters and left_ndx < right_ndx:
            right_ndx -= 1
            right_char = s[right_ndx]
        result = (right_char.lower() == left_char.lower())
    return result    

vals = ["", "hapaH", "Ma......a.m!", "No!....devil...,.'....lived......on", "no"]

for val in vals:
    print(val, is_palindrome(val))

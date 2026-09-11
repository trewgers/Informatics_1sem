mirror = {
    'A': 'A', 'H': 'H', 'I': 'I', 'M': 'M', 'O': 'O', 'T': 'T',
    'U': 'U', 'V': 'V', 'W': 'W', 'X': 'X', 'Y': 'Y',
    '1': '1', '8': '8',
    'E': '3', 'J': 'L', 'S': '2', 'Z': '5',
    '3': 'E', 'L': 'J', '2': 'S', '5': 'Z'
}

s = input().strip()
is_palindrome = (s == s[::-1])
is_mirrored = True
for i in range(len(s)):
    ch = s[i]
    opposite = s[len(s) - 1 - i]
    if ch not in mirror or mirror[ch] != opposite:
        is_mirrored = False
        break
if is_palindrome and is_mirrored:
    print(s, "is a mirrored palindrome.")
elif is_palindrome:
    print(s, "is a regular palindrome.")
elif is_mirrored:
    print(s, "is a mirrored string.")
else:
    print(s, "is not a palindrome.")
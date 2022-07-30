i = 0
magazine = "aab"
ransomNote = "aa"
while len(magazine) > 0:
    for letter in magazine:
        if letter in ransomNote:
            magazine -= letter
            i += 1
len(ransomNote) == i
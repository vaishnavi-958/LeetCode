from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)

# Approach B: Fixed Array / Manual Count (Low-level performance)
def isAnagram_array(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    counts = [0] * 26
    for char_s, char_t in zip(s, t):
        counts[ord(char_s) - ord("a")] += 1
        counts[ord(char_t) - ord("a")] -= 1

    return all(count == 0 for count in counts) 
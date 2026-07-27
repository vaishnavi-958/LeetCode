class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        count = {}

        # Count letters available in magazine
        for char in magazine:
            count[char] = count.get(char, 0) + 1

        # Use letters for ransomNote
        for char in ransomNote:
            if char not in count or count[char] == 0:
                return False

            count[char] -= 1

        return True
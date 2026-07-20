from collections import Counter, defaultdict

class Solution:
    def findSubstring(self, s: str, words: list[str]) -> list[int]:
        if not s or not words:
            return []

        word_len = len(words[0])
        num_words = len(words)
        total_len = word_len * num_words

        if len(s) < total_len:
            return []

        word_count = Counter(words)
        result = []

        # Try every possible starting offset
        for offset in range(word_len):
            left = offset
            curr_count = defaultdict(int)
            matched = 0

            # Move right one word at a time
            for right in range(offset, len(s) - word_len + 1, word_len):
                word = s[right:right + word_len]

                if word in word_count:
                    curr_count[word] += 1
                    matched += 1

                    # Too many copies of current word
                    while curr_count[word] > word_count[word]:
                        left_word = s[left:left + word_len]
                        curr_count[left_word] -= 1
                        matched -= 1
                        left += word_len

                    # Found valid window
                    if matched == num_words:
                        result.append(left)

                        left_word = s[left:left + word_len]
                        curr_count[left_word] -= 1
                        matched -= 1
                        left += word_len

                else:
                    # Reset window
                    curr_count.clear()
                    matched = 0
                    left = right + word_len

        return result
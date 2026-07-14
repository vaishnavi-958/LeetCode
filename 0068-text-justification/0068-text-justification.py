class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        result = []
        i = 0

        while i < len(words):
            line = []
            line_length = 0

            # Collect words for the current line
            while i < len(words) and line_length + len(words[i]) + len(line) <= maxWidth:
                line.append(words[i])
                line_length += len(words[i])
                i += 1

            # Last line or only one word
            if i == len(words) or len(line) == 1:
                current = " ".join(line)
                current += " " * (maxWidth - len(current))
                result.append(current)
            else:
                spaces = maxWidth - line_length
                gaps = len(line) - 1

                even = spaces // gaps
                extra = spaces % gaps

                current = ""

                for j in range(gaps):
                    current += line[j]
                    current += " " * (even + (1 if j < extra else 0))

                current += line[-1]
                result.append(current)

        return result
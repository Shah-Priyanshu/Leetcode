class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        result = []
        line = []
        line_length = 0

        for word in words:
            if line_length + len(word) + len(line) <= maxWidth:
                line.append(word)
                line_length += len(word)
            else:
                result.append(self.format_line(line, maxWidth, False))
                line = [word]
                line_length = len(word)

        # Format the last line (left-justified)
        result.append(self.format_line(line, maxWidth, True))

        return result

    def format_line(self, words, maxWidth, is_last_line):
        if is_last_line or len(words) == 1:
            # Left-justify for the last line or if there's only one word
            return ' '.join(words).ljust(maxWidth)
        else:
            # Distribute extra spaces evenly between words
            total_spaces = maxWidth - sum(len(word) for word in words)
            spaces_between_words = total_spaces // (len(words) - 1)
            extra_spaces = total_spaces % (len(words) - 1)
            formatted_line = words[0]
            for i in range(1, len(words)):
                spaces = spaces_between_words + (1 if i <= extra_spaces else 0)
                formatted_line += ' ' * spaces + words[i]
            return formatted_line

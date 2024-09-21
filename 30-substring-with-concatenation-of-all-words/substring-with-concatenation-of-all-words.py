class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
            #def find_substring(s, words):
        """
        Finds indices where a substring in `s` is a concatenation of all words in `words` in any order.

        Args:
            s: The main string.
            words: A list of words.

        Returns:
            A list of starting indices of the concatenated substrings.
        """  

        result = []
        if not words or len(s) < len(words) * len(words[0]):
            return result

        N = len(s)
        M = len(words)
        wl = len(words[0])

        # Use a dictionary to store word counts
        word_count = {}
        current_count = {}
        for word in words:
            word_count[word] = word_count.get(word, 0) + 1

        for i in range(wl):
            count = 0  # Reset count for each window
            start = i

            # Iterate over the string with a sliding window
            for r in range(i, N, wl):
                str_slice = s[r:r + wl]  # Pythonic string slicing
                if str_slice in word_count:
                    current_count[str_slice] = current_count.get(str_slice, 0) + 1
                    if current_count[str_slice] <= word_count[str_slice]:
                        count += 1

                    # Adjust the window based on word counts
                    while current_count[str_slice] > word_count[str_slice]:
                        tmp_slice = s[start:start + wl]
                        current_count[tmp_slice] -= 1
                        start += wl
                        if current_count[tmp_slice] < word_count[tmp_slice]:
                            count -= 1

                    # Add starting index to result if all words are found
                    if count == M:
                        result.append(start)
                        tmp_slice = s[start:start + wl]
                        current_count[tmp_slice] -= 1
                        start += wl
                        count -= 1
                else:
                    current_count.clear()
                    count = 0
                    start = r + wl  # Move start if the window doesn't contain a word

            current_count.clear()

        return result
                
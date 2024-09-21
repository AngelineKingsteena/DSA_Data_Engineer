class Solution:
    def findAnagrams(self, s: str, t: str) -> List[int]:
        #def findAnagrams(s, t):
        result = []
        if len(t) > len(s):
            return result

        # Create a dictionary to count the frequency of characters in `t`.
        char_count = {}
        for char in t:
            char_count[char] = char_count.get(char, 0) + 1

        counter = len(char_count)  # This keeps track of how many unique characters need to be matched.

        begin, end = 0, 0  # Pointers for the sliding window.
        
        # Start sliding the window over the string `s`.
        while end < len(s):
            char = s[end]
            
            # If the character is in the dictionary, decrease its count.
            if char in char_count:
                char_count[char] -= 1
                if char_count[char] == 0:  # If the count reaches zero, we have a match for this character.
                    counter -= 1
            
            end += 1

            # When all characters are matched, try to shrink the window from the left.
            while counter == 0:
                temp_char = s[begin]

                # If the current window is the same length as `t`, it is an anagram.
                if end - begin == len(t):
                    result.append(begin)

                # Try to remove the leftmost character from the window and adjust the count.
                if temp_char in char_count:
                    char_count[temp_char] += 1
                    if char_count[temp_char] > 0:  # If the count goes above zero, we need to match this character again.
                        counter += 1

                begin += 1

        return result

            
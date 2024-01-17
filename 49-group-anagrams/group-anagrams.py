class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
      # Hash Map
        hash_map = defaultdict(list)
        # Iterate over each string in given list
        for s in strs:
            # Hash function to get key
            key = ''.join(sorted(s))
            # CASE: If key is in hash map
            hash_map[key].append(s)
        return hash_map.values()

# OR SHORTENED VERSION USING DEFAULTDICT

# s=defaultdict(list)
# for st in strs:
#     a=''.join(sorted(st))
#     s[a].append(st)
# return s.values()

# T.C

# O(nlogn)

# The time complexity  is O(n log(n)), where n is the length of the string.

# The sorting algorithm used is the merge sort algorithm. The merge sort algorithm works by recursively dividing the array in half and then merging the two halves back together. The merge sort algorithm has a worst-case time complexity of O(n log(n)).
        
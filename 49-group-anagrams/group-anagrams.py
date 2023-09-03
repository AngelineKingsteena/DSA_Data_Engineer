class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
      # Hash Map
        hash_map = {}
        # Iterate over each string in given list
        for s in strs:
            # Hash function to get key
            key = ''.join(sorted(s))
            # CASE: If key is in hash map
            if key in hash_map:
                hash_map[key].append(s)
            # CASE: If key is not in hash map
            else:
                hash_map[key] = [s]
        return hash_map.values()
        
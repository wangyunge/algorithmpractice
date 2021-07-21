class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        table = {}
        for item in strs:
            key = ''.join(sorted(item))
            table.setdefault(key, [])
            table[key].append(item)
        return table.values()

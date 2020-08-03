#哈希
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict = {}
        for item in strs:
            key = tuple(sorted(item))
            dict[key] = dict.get(key, []) + [item]
        return list(dict.values())

#时间更短
class Solution:       
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict
        lookup = defaultdict(list)  #这里必须要标注是list，否则字典内的类型为：None
        for s in strs:
            lookup["".join(sorted(s))].append(s)
        return list(lookup.values())        
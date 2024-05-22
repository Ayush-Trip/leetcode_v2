class Solution:
	def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
		ga = collections.defaultdict(list)
		for s in strs:
			l = ''.join(sorted(s))
			ga[l].append(s)
		return list(ga.values())
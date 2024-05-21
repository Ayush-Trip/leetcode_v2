class Solution:
	def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
		grouped_anagrams = collections.defaultdict(list)
		for s in strs:
			sorted_s = ''.join(sorted(s))
			grouped_anagrams[sorted_s].append(s)
		return list(grouped_anagrams.values())
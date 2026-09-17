class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        a = Counter(nums)
        result = list()
        for i in range(k):
            result.append(a.most_common(k)[i][0])
        return result
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        hashset = {}
        for i in nums:
            if(i in hashset):
                hashset[i] += 1
            else:
                hashset[i] = 1

        sorted_hash = dict(sorted(hashset.items(), 
        key=lambda item: item[1], reverse = True))
        print(sorted_hash)
        temp = list(sorted_hash.keys())

        output_lst = []
        for i in range(k):
            output_lst.append(temp[i])
        return output_lst
        

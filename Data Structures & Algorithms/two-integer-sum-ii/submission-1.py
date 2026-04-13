class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # approach
        # iterate numbers
        # use temp to store it and check if there is another number that 
        
        temp = 0
        for i in range(len(numbers)):
            temp = numbers[i]
            j = 0
            while(j < len(numbers)):
                if(j != i):
                    if numbers[j] + numbers[i] == target:
                        return sorted([j+1, i+1])
                j += 1
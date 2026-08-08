class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        new_list = []
        for i,value in enumerate(arr):
            if i == (len(arr) - 1):
                new_list.append(-1)
            else:
                greatest = max(arr[i+1:])
                new_list.append(greatest)
        return new_list
        
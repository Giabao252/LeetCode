class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        found_top = False
        p1 = 0
        p2 = 1

        if len(arr) < 3: 
            return False

        while found_top != True:
            if arr[p1] >= arr[p2]:
                return False
            if p2 == len(arr) - 1:
                return False
            if (arr[p1] < arr[p2]) and (arr[p2] > arr[p2+1]):
                print(p1)
                print(p2)
                found_top = True
            p1 += 1
            p2 += 1
        
        while p2 <= (len(arr) - 1):
            if arr[p1] <= arr[p2]:
                return False
            p1 += 1
            p2 += 1
        
        return True
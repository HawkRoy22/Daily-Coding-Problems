class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False

        # Finding the Peak
        peak = arr.index(max(arr))

        if peak == len(arr) - 1 or peak == 0:
            return False

        # checking the uphill portion
        counterUp = 0
        for x in range(0, peak - 1):
            if arr[x + 1] > arr[x]:
                counterUp += 0
            else:
                counterUp += 1

        counterDown = 0
        for z in range(peak, len(arr) - 1):
            if arr[z + 1] < arr[z]:
                counterDown += 0
            else:
                counterDown += 1

        if counterUp == 0 and counterDown == 0:
            return True
        else:
            return False

    validMountainArray([0,1,3,4,3,2,1])
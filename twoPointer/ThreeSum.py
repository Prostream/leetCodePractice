def find_sum_of_three(nums, target):
   nums.sort()#O（nlogn）复杂度，直接drop了
   n = len(nums)
   for i in range(n - 2):
     left = i+1
     right = n-1
     while left < right:
       now_sum = nums[i] + nums[left] + nums[right]
       if target == now_sum:
         return True
       elif now_sum > target:
         right = right - 1
       else:
         left = left + 1
   # Replace this placeholder return statement with your code
   return False
# Driver code
def main():
    nums_lists = [[3, 7, 1, 2, 8, 4, 5],
                  [-1, 2, 1, -4, 5, -3],
                  [2, 3, 4, 1, 7, 9],
                  [1, -1, 0],
                  [2, 4, 2, 7, 6, 3, 1]]

    targets = [10, 7, 20, -1, 8]

    for i in range(len(nums_lists)):
        print(i + 1, ".\tInput array: ", nums_lists[i], sep="")
        if find_sum_of_three(nums_lists[i], targets[i]):
            print("\tSum for", targets[i], "exists")
        else:
            print("\tSum for", targets[i], "does not exist")
        print("-"*100)

if __name__ == '__main__':
    main()
# naive approach需要O（n^3）的时间复杂度
# 这个two pointer方案只需要nlogn+n^2时间复杂度，O(n)空间复杂度
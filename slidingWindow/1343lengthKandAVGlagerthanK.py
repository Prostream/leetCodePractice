def numOfSubarrays(arr,k,threshold):
    subsum = 0
    ans = 0
    for i in range(len(arr)):
        subsum += arr[i]
        if i >= k:
            subsum -= arr[i-k]
        if i >= k-1 and subsum/k >= threshold:
            ans += 1
    return ans

print(numOfSubarrays([2,2,2,2,5,5,5,8],3,4))
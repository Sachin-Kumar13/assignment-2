
def subArraySum(arr, n, sum):
    for i in range(n):
        curr_sum = arr[i]


        j = i + 1
        while j <= n:
            temp=[]
            if curr_sum == sum:
                for h in range(i,j):
                    temp.append(arr[h])
                print(temp)


                return 1

            if curr_sum > sum or j == n:
                break

            curr_sum = curr_sum  + arr[j]
            j += 1

    print("No subarray found")
    return 0

arr= list (map (int,input().split()))
n=len(arr)
sum=int(input())
subArraySum(arr, n, sum)


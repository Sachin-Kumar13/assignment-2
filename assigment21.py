def solve( s , k):
    arr = s.split()
    output = []
    buffer_arr = []
    buffer_len = -1
    i = 0

    while i < len(arr):
        w = arr[i]
        if len(w) > k:
            print('\n[*] Cannot complete because of this word: "%s"' % w)
            return
        if (len(w) + buffer_len + 1) <= k:
            buffer_len += len(w) + 1
            buffer_arr.append(w)
            i += 1
        else:
            result = ' '.join(buffer_arr)
            output.append(result)
            buffer_arr = []
            buffer_len = -1
    if buffer_arr:
        result = ' '.join(buffer_arr)
        output.append(result)
    return output



input_str=input()
k = int(input())
X = solve(input_str, k)
for s in X:
    print(s)
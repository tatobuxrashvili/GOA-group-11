def count_positives_sum_negatives(arr):
    if len(arr) == 0:
        return arr
    count = 0
    sum = 0
    for i in arr:
        if i > 0:
            count += 1
        else:
            sum += i
    return [count , sum]
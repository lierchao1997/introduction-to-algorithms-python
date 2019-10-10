# --- 归并排序的实现 ---
# - author: 轩辕御龙
# - date: 2019-10-10

def merge_sort(array):
    if len(array) < 2:
        return array
    else:
        mid = len(array) // 2
        left = merge_sort(array[:mid])
        right = merge_sort(array[mid:])
        return merge(left, right)


def merge(left, right):
    result = []
    length = len(left) + len(right)
    left_length = len(left)
    right_length = len(right)
    p, q = 0, 0
    for i in range(length):
        if p >= left_length:
            result += right[q:]
            break
        if q >= right_length:
            result += left[p:]
            break
        if left[p] <= right[q]:
            result.append(left[p])
            p += 1
        else:
            result.append(right[q])
            q += 1
    return result
    

print(merge_sort([5,8,9,6,3,7,4,1,5,6,9,1,1]))

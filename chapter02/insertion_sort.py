# --- 插入排序的实现 ---
# - author: 轩辕御龙
# - date: 2019-10-10


def insertion_sort(array):
    for i in range(1,len(array)):
        key = array[i]
        li = list(range(i))
        li.reverse()
        for j in li:
            if array[j] < key:
                del array[i]
                array.insert(j+1, key)
                break
            elif j == 0:
                del array[i]
                array.insert(0, key)
    return array

print(insertion_sort([5,9,6,3,7,8,5,1,9,4,1,5,4,8,91]))

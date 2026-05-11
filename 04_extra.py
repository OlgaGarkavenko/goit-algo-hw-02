# алгоритм Merge Sort

def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result


def merge_sort(lists):
    if len(lists) <= 1:
        return lists

    mid = len(lists) // 2
    left = merge_sort(lists[:mid])
    right = merge_sort(lists[mid:])

    return merge(left, right)


lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
merged_list = merge_sort(lists)

print("Відсортований список:", merged_list)

# [:1] - до i
# [1:] - від і до кінця
# [:] - весь список
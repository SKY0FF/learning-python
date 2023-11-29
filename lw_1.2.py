def sort(list, start, end):
    if end - start > 1:
        mid = (start + end)//2
        sort(list, start, mid)
        sort(list, mid, end)
        lst_sort(list, start, mid, end)
 
def lst_sort(list, start, mid, end):
    left = list[start:mid]
    right = list[mid:end]
    k = start
    i = 0
    j = 0
    while (start + i < mid and mid + j < end):
        if (left[i] <= right[j]):
            list[k] = left[i]
            i = i + 1
        else:
            list[k] = right[j]
            j = j + 1
        k = k + 1
    if start + i < mid:
        while k < end:
            list[k] = left[i]
            i = i + 1
            k = k + 1
    else:
        while k < end:
            list[k] = right[j]
            j = j + 1
            k = k + 1
 
lst = [1, 2, 7, 123, 93213, 478, 5, -123, 0]
print(f"Список до сортировки: {lst}")
sort(lst, 0, len(lst))
print(f"Отсортированный список: {lst}")
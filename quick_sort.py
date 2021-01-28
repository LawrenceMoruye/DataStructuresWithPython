def quick_sort(seq):
    l = len(seq)
    if l <=1:
        return seq
    else:
        pivot = seq.pop()

    elm_grt_than_pivot = []
    elm_less_than_pivot = []

    for item in seq:
        if item > pivot:
            elm_grt_than_pivot.append(item)

        else:
            elm_less_than_pivot.append(item)

    return quick_sort(elm_grt_than_pivot) + [pivot] + quick_sort(elm_less_than_pivot)


print(quick_sort([2,9,0,5,3,79,90,4]))    
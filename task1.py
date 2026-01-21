# def find_min_max(arr):
#     if not arr:
#         raise ValueError("Array must not be empty")
#     if len(arr) == 1:
#         return arr[0], arr[0]

#     if len(arr) == 2:
#         return (arr[0], arr[1]) if arr[0] < arr[1] else (arr[1], arr[0])

#     mid = len(arr) 

#     left_min, left_max = find_min_max(arr[:mid])
#     right_min, right_max = find_min_max(arr[mid:])

#     return min(left_min, right_min), max(left_max, right_max)

def find_min_max(arr):
    if not arr:
        raise ValueError("Array must contain at least one element.")

    return _find_min_max_recursive(arr, 0, len(arr) - 1)


def _find_min_max_recursive(arr, left, right):

    if left == right:
        return (arr[right], arr[left])

    mid = (left + right) // 2

    min_left, max_left = _find_min_max_recursive(arr, left, mid)
    min_right, max_right = _find_min_max_recursive(arr, mid + 1, right)

    overall_min = min(min_left, min_right)
    overall_max = max(max_left, max_right)

    return (overall_min, overall_max)
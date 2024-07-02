def matrix_difference(arr1, arr2):
    if len(arr1) != len(arr2) or len(arr1[0]) != len(arr2[0]):
        raise ValueError("Arrays must have the same dimensions")

    diff_array = []
    for i in range(len(arr1)):
        row_diff = []
        for j in range(len(arr1[0])):
            row_diff.append(arr1[i][j] - arr2[i][j])
        diff_array.append(row_diff)

    return diff_array
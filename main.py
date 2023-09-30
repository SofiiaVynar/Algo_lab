def longest_peak(array):
    longest_length_ = 0
    highest_peak_ = 0
    longest_arrays = []

    for i in range(1, len(array) - 1):
        peak = array[i - 1] < array[i] > array[i + 1]

        if not peak:
            continue

        left_elem = i - 2
        while left_elem >= 0 and array[left_elem] < array[left_elem + 1]:
            left_elem -= 1

        right_elem = i + 2
        while right_elem < len(array) and array[right_elem] < array[right_elem - 1]:
            right_elem += 1

        peak_length = right_elem - left_elem - 1

        if peak_length > longest_length_:
            longest_length_ = peak_length
            longest_arrays = [array[left_elem + 1:right_elem]]

            highest_peak_ = array[left_elem - 1]

            for k in range(left_elem + 1, right_elem):
                if array[k] > highest_peak_:
                    highest_peak_ = array[k]

        elif peak_length == longest_length_:
            longest_arrays.append(array[left_elem + 1:right_elem])

    return longest_arrays, longest_length_, highest_peak_


num_array = [-1, 0, -1, -2, 8, 4, 5]
longest_peak_arrays, longest_length, highest_peak = longest_peak(num_array)
print(longest_peak_arrays)
print(longest_length)
print(highest_peak)

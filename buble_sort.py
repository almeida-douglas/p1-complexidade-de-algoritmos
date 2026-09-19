def bubble_sort(items):
	result = list(items)
	for end in range(len(result) - 1, 0, -1):
		swapped = False
		for index in range(end):
			if result[index] > result[index + 1]:
				result[index], result[index + 1] = result[index + 1], result[index]
				swapped = True
		if not swapped:
			break

	return result

print(bubble_sort([5, 3, 8, 6, 2]))
def bubble_sort(numbers):
    length = len(numbers)
    comp_count = 0
    swap_count = 0

    print("Original Array:")
    print(numbers)
    print()

    for outer in range(length - 1):
        swapped = False
        pass_comp = 0
        print("========== PASS " + str(outer + 1) + " ==========")
        print()

        for inner in range(length - 1 - outer):
            pass_comp = pass_comp + 1
            comp_count = comp_count + 1
            print("Comparison " + str(pass_comp) + ":")
            print("Compare " + str(numbers[inner]) + " and " + str(numbers[inner + 1]))

            if numbers[inner] > numbers[inner + 1]:
                numbers[inner], numbers[inner + 1] = numbers[inner + 1], numbers[inner]
                swap_count = swap_count + 1
                swapped = True
                print("Swap!")
            else:
                print("No swap.")

            print(numbers)
            print()

        if swapped == False:
            print("No swaps were made.")
            print("Array is already sorted.")
            print()
            break

    print("========== RESULT ==========")
    print("Final Sorted Array:")
    print(numbers)
    print()
    print("Total Comparisons: " + str(comp_count))
    print("Total Swaps: " + str(swap_count))

# TEST CASE 1
print("TEST CASE 1")
bubble_sort([5, 3, 8, 4, 2])
print()
print("=" * 50)
print()

# TEST CASE 2
print("TEST CASE 2")
bubble_sort([1, 2, 3, 4, 5])
print()
print("=" * 50)
print()

# TEST CASE 3
print("TEST CASE 3")
bubble_sort([5, 4, 3, 2, 1])
print()
print("=" * 50)
print()

# TEST CASE 4
print("TEST CASE 4")
bubble_sort([3, 1, 4, 1, 5])





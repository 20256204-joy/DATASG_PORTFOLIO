# ============================================================
# SELECTION SORT PROGRAM
# Activity 2 - Implementing Selection Algorithm
# ============================================================

def display_menu():
    """Display the main menu."""
    print("=" * 45)
    print("         SELECTION SORT PROGRAM")
    print("=" * 45)
    print("1. Sort Ascending")
    print("2. Sort Descending")
    print("3. Exit")
    print("=" * 45)


def selection_sort(arr, ascending=True):
    """
    Manual Selection Sort implementation.
    Displays every pass, comparison, min/max update, and swap.
    Returns total comparisons and swaps.
    """
    n = len(arr)
    comparisons = 0
    swaps = 0

    for i in range(n - 1):
        target_idx = i

        print(f"\n========== PASS {i + 1} ==========")
        label = "minimum" if ascending else "maximum"
        print(f"Current {label}: {arr[target_idx]}")

        # Inner loop: find min (ascending) or max (descending)
        for j in range(i + 1, n):
            comparisons += 1
            print(f"Compare {arr[j]} with {arr[target_idx]}")

            if ascending:
                if arr[j] < arr[target_idx]:
                    target_idx = j
                    print(f"New minimum: {arr[j]}")
                else:
                    print("No change.")
            else:
                if arr[j] > arr[target_idx]:
                    target_idx = j
                    print(f"New maximum: {arr[j]}")
                else:
                    print("No change.")

        print(f"{'Minimum' if ascending else 'Maximum'} found: {arr[target_idx]}")

        # Swap if needed
        if target_idx != i:
            print(f"Swap {arr[i]} and {arr[target_idx]}")
            arr[i], arr[target_idx] = arr[target_idx], arr[i]
            swaps += 1
        else:
            print("No swap needed.")

        print(f"Array after Pass {i + 1}:")
        print(arr)

    return comparisons, swaps


def main():
    while True:
        display_menu()
        choice = input("\nEnter your choice: ").strip()

        if choice == "3":
            print("\nExiting program. Goodbye!")
            break

        if choice not in ("1", "2"):
            print("\nInvalid choice. Please enter 1, 2, or 3.")
            continue

        ascending = (choice == "1")
        order_name = "ASCENDING" if ascending else "DESCENDING"

        # Horizontal input, space-separated
        raw = input("\nEnter the elements separated by spaces: ")
        arr = list(map(int, raw.split()))

        print(f"\nOriginal Array:")
        print(arr)
        print(f"\nSorting Order: {order_name}")

        comparisons, swaps = selection_sort(arr, ascending)

        print("\n========== SORTING COMPLETE ==========")
        print("Sorted Array:")
        print(arr)
        print(f"Total Comparisons: {comparisons}")
        print(f"Total Swaps: {swaps}")
        print("=" * 45)


if __name__ == "__main__":
    main()




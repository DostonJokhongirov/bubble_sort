def main():
    unordered_list = [2, 5, 4, 1, 3, 7, 9, 8, 6]
    sorted_list = bubble_sort(unordered_list)
    print(sorted_list)
    
def bubble_sort(list_to_sort):
    processed_list = list_to_sort.copy()
    sorting_boundary = 1
    was_swap = True
    while was_swap:
        was_swap = False
        for i in range(len(processed_list) - sorting_boundary):
            if processed_list[i] > processed_list[i + 1]:
                was_swap = True
                processed_list[i], processed_list[i + 1] = processed_list[i + 1], processed_list[i]
        sorting_boundary += 1

    return processed_list
    
main()

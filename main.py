def main():
    unordered_list = [2, 5, 4, 1, 3, 7, 9, 8, 6]
    sorted_list = bubble_sort(unordered_list)
    print(sorted_list)
    
def bubble_sort(list_to_sort):
    prss_list = list_to_sort.copy()
    last_ndx = 1
    swap = True
    while swap:
        swap = False
        for i in range(len(prss_list) - last_ndx):
            if prss_list[i] > prss_list[i + 1]:
                swap = True
                prss_list[i], prss_list[i + 1] = prss_list[i + 1], prss_list[i]
        last_ndx += 1

    return prss_list
    
main()

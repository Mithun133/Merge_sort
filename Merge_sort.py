
# Merge sort Implementation

def merge_sort(data_list):
    #  funcation

    if len(data_list) > 1:
        #  Splitting
        mid = len(data_list) // 2
        left = data_list [:mid]
        right = data_list [mid:]
        merge_sort(left)
        merge_sort(right)

        # Initialize
        i, j, k = 0, 0, 0

        # Merging
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                data_list[k] = left[i]
                i +=1
            else:
                data_list[k] = right[j]
                j +=1
            k +=1
        # insert remaing elements from left side list
        while i < len(left):
            data_list[k] = left[i]
            i +=1
            k +=1
        # insert remaing elements from right side list
        while j < len(right):
            data_list[k] = right[j]
            j +=1
            k +=1

if __name__ == '__main__':
    data_list = [5,2,7,6,20,30]
    print('Before Merge Sort: ' , data_list)
    merge_sort(data_list)
    print('After Merge Sort: ', data_list)



def merge_sort(data_list):
    if len(data_list) > 1:
        # spliting
        mid = len(data_list) // 2
        left = data_list [:mid]
        right = data_list [mid:]
        merge_sort(left)
        merge_sort(right)

        i, j, k = 0, 0, 0

        # Merging
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                data_list[k] = left[i]
                i +=1
                k +=1
            else:
                data_list[k] = right[j]
                j +=1
                k +=1
        # insert left element
        while i < len(left):
            data_list[k] = left[i]
            i +=1
            k +=1

        # insert right element
        while j < len(right):
            data_list[k] = right[j]
            j +=1
            k +=1

if __name__ == '__main__':
    data_list = [5, 7, 2, 9, 3, 8, 15, 20]
    print('\nBefore Merge Sort: ', data_list)
    merge_sort(data_list)
    print('After Merg Sort: ', data_list)

            




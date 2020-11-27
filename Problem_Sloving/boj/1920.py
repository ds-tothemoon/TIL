def binary_search(find_value, base_list):
    left = 0
    right = len(base_list) - 1
    mid = right // 2

    while left < right:
        if base_list[mid] == find_value:
            break
        if base_list[mid] > find_value:
            right = mid - 1
        else:
            left = mid + 1
        mid = ( right + left ) //2

    if base_list[mid] == find_value:
        return 1
    return 0


n = int(input())
base_list  = sorted(list(map(int,input().split(' '))))
m = int(input())
find_list  = list(map(int,input().split(' ')))
#print(n,m,base_list,find_list)

for element in find_list:
    print(binary_search(element, base_list))


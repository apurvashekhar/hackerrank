Q- Runner up score
    if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    new_list = []
    for i in arr:
        new_list.append(i)
    sorted_list = sorted(new_list, reverse = True)
    unique_list = []
    for num in sorted_list:
        if num in unique_list:
            continue
        else:
            unique_list.append(num)
    print(unique_list[1])

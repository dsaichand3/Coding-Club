n = 7
lists = []
for i in range(0, n):
    new_list = []
    if i == 0:
        print(1)
        lists.append(1)
    else:
        k = 0
        pivot = lists[k]
        cnt = 0
        while(pivot == lists[k]):
            cnt = cnt + 1
            k+=1
            if k >= len(lists):
                new_list.append(cnt)
                new_list.append(pivot)
                break
            if pivot != lists[k]:
                new_list.append(cnt)
                new_list.append(pivot)
                cnt = 0
                pivot = lists[k]

        for each in new_list:
            print(each, end = " ")
        print(end="\n")
        lists = new_list
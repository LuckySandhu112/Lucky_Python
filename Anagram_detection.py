words=["cat","dog","tac","god","act"]
for i in range(len(words)):
    for j in range(i+1,len(words)):
        list1=[ch for ch in words[i]]
        list2=[ch for ch in words[j]]
        for x in range(len(list1)):
            for y in range(x+1,len(list1)):
                if list1[x] > list1[y]:
                    list1[x],list1[y] = list1[y],list1[x]

        for x in range(len(list1)):
            for y in range(x+1,len(list2)):
                if list2[x] > list2[y]:
                    list2[x],list2[y] = list2[y],list2[x]

        if list1 == list2:
            print(words[i],"<->",words[j])

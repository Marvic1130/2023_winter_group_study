def radix_sort(a, base = 10):
    def list_to_buckets(a, base, iteration):
        buckets = [[] for x in range(base)]  # base만큼 []을 생성(메모리 차이)
        for x in a:     
            digit = (x // (base ** iteration)) % base     
            buckets[digit].append(x)
        return buckets
    
    def buckets_to_list(buckets):
        a = []
        for buckt in buckets:
            for x in buckt:
                a.append(x)
        return a

    maxval = max(a)
    it = 0
    while base ** it <= maxval:
        a = buckets_to_list(list_to_buckets(a, base, it))
        it += 1
    return a

arr = [10,11,23,111,467,234562,972]
print(radix_sort(arr, 7))

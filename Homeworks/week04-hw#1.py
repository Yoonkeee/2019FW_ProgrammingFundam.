def bubblesort(ns):
    for k in range(len(ns)):
        for i in range(0, len(ns) - (k + 1)):
            if ns[i] > ns[i + 1]:
                ns[i], ns[i + 1] = ns[i + 1], ns[i]
    return ns

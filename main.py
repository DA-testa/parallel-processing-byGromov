# python3
# Author: Aleksandrs Pučenkins 17.gr. 221RDB335

ddef parallel_processing(n, m, data):
    output = []

    thread_execution_times = []
    for i in range(n):
        thread_execution_times.append(0)

    output.append((0, 0))
    thread_execution_times[0] = data[0]

    for i in range(m)[1:]:
        n_min = 0
        for k in range(n)[1:]:
            if thread_execution_times[k] < thread_execution_times[n_min]:
                n_min = k
        output.append((n_min, thread_execution_times[n_min]))
        thread_execution_times[n_min] = thread_execution_times[n_min] + data[i]
    return output

def main():
    n = 0
    m = 0
    (n, m) = tuple(map(int, input().split()))

    data = []
    data = list(map(int, input().split()))

    result = parallel_processing(n,m,data)
    
    for pair in result:
        print(str(pair[0]) + " " + str(pair[1]))



if __name__ == "__main__":
    main()
# python3
# Author: Aleksandrs Pučenkins 17.gr. 221RDB335

def parallel_processing(n, m, data):

    output = []
    threads = [(i, 0) for i in range(n)] 
    
    for i in range(m):
        t = data[i]
        thread = min(threads, key=lambda x: x[1])  
        output.append((thread[0], thread[1]))  
        threads[threads.index(thread)] = (thread[0], thread[1] + t)  
    return output

def main():
    n, m = map(int, input().split())
    data = list(map(int, input().split()))
    result = parallel_processing(n, m, data)
    for t in result:
        print(t[0], t[1])
        
if __name__ == "__main__":
    main()
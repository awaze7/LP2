def JobScheduling(arr, t):
    n = len(arr)
    
    # Sorts in descending order 
    for i in range(0, n - 1):
        largest = i
        for j in range(i + 1, n):
            if arr[largest][2] < arr[j][2]:
                largest = j
        arr[i], arr[largest] = arr[largest], arr[i]
    
    #print(arr)  # Print the sorted array after the sorting process is complete
    result=[False]*t #To keep track of free time slots
    jobs=['-1']*t #to store the jobs schedule
    total_profit=0
    
    for i in range(n):
        
        for j in range(min(t-1,arr[i][1]-1),-1,-1):
            if result[j] is False: # Free slot for job closest to deadline
                result[j]=True
                jobs[j]=arr[i][0] # to store job id
                total_profit+=arr[i][2]
                break
                
    print("Job Schedule:", jobs)
    print("Total Profit:", total_profit)

def main():
    arr = [['J1', 2, 20],
           ['J2', 2, 15],
           ['J3', 1, 10],
           ['J4', 3, 5],
           ['J5', 3, 1]]
#     arr = [['J1', 2, 100],
#            ['J2', 1, 19],
#            ['J3', 2, 27],
#            ['J4', 1, 25],
#            ['J5', 3, 15]]
    
    t = max(arr, key=lambda x: x[1])[1]  #max. deadline among the jobs=total time slots processor has
    print("Following is the maximum profit job schedule: ")
    JobScheduling(arr, t)  # 3 is the maximum deadline a job can wait


if __name__ == '__main__':
    main()

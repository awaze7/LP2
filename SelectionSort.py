def Selection_Sort(array):
    for i in range(0,len(array)-1):
        smallest=i
        for j in range(i+1,len(array)):
            if array[j]<array[smallest]:
                smallest=j
                
        array[i],array[smallest]=array[smallest],array[i]
            
            


array=input('Enter the list of Numbers: ').split()
array=[int(x) for x in array]

Selection_Sort(array)

print('\nList after sorting is: ')
#print(array) #works too
for i in range(len(array)):
    print("%d" %array[i],end=" ")
    
#TC:O(N^2) SC:O(1)

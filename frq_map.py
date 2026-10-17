size=int(input("Enter number of elements in array:"))
arr=[]
for i in range(size):
    element=int(input(f"Enter element {i+1}:"))
    arr.append(element)

def freq_elements(arr):
    freq_map={}
    for x in arr:
        if x in freq_map:
            freq_map[x]+=1
        else:
            freq_map[x]=1
    return freq_map

print(freq_elements(arr))
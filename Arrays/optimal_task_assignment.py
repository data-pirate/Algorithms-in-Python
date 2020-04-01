# following the greedy approach
# this will assign task by pairing the sorted array
# pair will be made by choosing a least and a greater number

arr = [4,2,6,1,7,3,9,5]
def optimal_task_assignment(arr):
    arr = sorted(arr)
    for i in range(len(arr)//2):
        print(arr[i], arr[~i]) # Bitwisee complement operator to put negative sign

optimal_task_assignment(arr)

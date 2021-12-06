class Solution:
    #Function to sort a list using quick sort algorithm.
    def quickSort(self,arr,low,high):
        # code here
        if low < high:
            pos = self.partition(arr, low, high)
            
            self.quickSort(arr, low, pos-1)
            self.quickSort(arr, pos+1, high)
    
    def partition(self,arr,low,high):
        # code here
        start = low
        end = high
        pivot = arr[start]
        
        while start < end:
            
            while arr[start] <= pivot and (start < len(arr)):
                start += 1
            
            while arr[end] > pivot:
                end -= 1
            
            if start < end:
                arr[start], arr[end] = arr[end], arr[start]
        
        arr[end], arr[low] = arr[low], arr[end]
        
        return end

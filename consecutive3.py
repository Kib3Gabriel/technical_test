
def three_consecutive(nums):
    
    for i in range(len(nums) - 1):
        
        if nums[i] == 3 and nums[i + 1] == 3:
            return True
    return False

list_nums = [2,4,3,3]
list_nums2 =[3,5,6,3,9,3]
print(three_consecutive(list_nums))   

print(three_consecutive(list_nums2))


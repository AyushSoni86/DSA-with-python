# rearrange elements

# def rearrangeArray(nums):
#     positive = []
#     negative = []
#     answer = []
#     for i in range(0, len(nums)):
#         if nums[i] < 0: negative.append(nums[i])
#         else: positive.append(nums[i])
    
#     for i in range(0, len(positive)):
#         answer.append(positive[i])
#         answer.append(negative[i])
    
#     return answer

def rearrange(nums):
        positive = []
        negative = []
        answer = []
        for i in range(0, len(nums)):
            if nums[i] < 0: negative.append(nums[i])
            else: positive.append(nums[i])
        
        print(positive)
        print(negative)
        pos, neg = 0, 0
        while pos < len(positive) and neg < len(negative):
            answer.append(positive[pos])
            answer.append(negative[neg])
            pos+=1
            neg+=1
        
        while pos < len(positive):
            answer.append(positive[pos])
            pos+=1
          
        while neg < len(negative):
            answer.append(negative[neg])
            neg+=1
        
        return answer

nums = [3,1,-2,-5,2,-4]
nums2 = [9, 4, -2, -1, 5, 0, -5, -3, 2]
nums3 = [-5, -2, 5, 2, 4, 7, 1, 8, 0, -8]
print(rearrange(nums3))





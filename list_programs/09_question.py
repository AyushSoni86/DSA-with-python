# merge two sorted arrays without duplicates

def merge_sorted_array_without_duplicates(nums1, nums2):
    i, j = 0, 0
    nums1_len = len(nums1)
    nums2_len = len(nums2)
    
    ans = []
    count = 0
    ans.append(nums1[0] if nums1[0] < nums2[0] else nums2[0])
    
    while(i < nums1_len and j < nums2_len):
        if(nums1[i] <= nums2[j]):
            if(nums1[i] != ans[count]):
                ans.append(nums1[i])
                count+=1
            i+=1
            
        else:
            if(nums2[j] != ans[count]):
                ans.append(nums2[j])
                count+=1
            j+=1
        
    while(i < nums1_len):
        if(nums1[i] != ans[count]):
            ans.append(nums1[i])
            count+=1
        i+=1      
    while(j < nums2_len):
        if(nums2[j] != ans[count]):
            ans.append(nums2[j])
            count+=1
        j+=1
        
    return ans  

nums1 = [1, 1, 1, 1, 2, 4, 6, 7]
nums2 = [1, 2, 3, 4, 4, 4, 5, 6, 7, 7, 8]
     
ans = merge_sorted_array_without_duplicates(nums1, nums2)
print(ans)
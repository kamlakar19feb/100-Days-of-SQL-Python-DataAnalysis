 Merge two lists without duplicates

Example: [1,2,3] + [2,3,4] → [1,2,3,4]

nums1=list(map(int,input("Enter space separated numbers: ").split()))
nums2=list(map(int,input("Enter space separated numbers: ").split()))
for i in nums2:
  if i not in nums1:
    nums1.append(i)
print("Merged list: ",nums1)

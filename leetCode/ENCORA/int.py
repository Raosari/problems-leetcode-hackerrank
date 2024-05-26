class Solution:
    def productExceptSelf(self, nums) -> list:
        res = []
        for null in range(len(nums)):
            product = 1
            for i,n in enumerate(nums):
                if null == i:
                    if i == len(nums) - 1:
                        res.append(product)
                    continue
                else:
                    product *= n
                    if i == len(nums) - 1:
                        res.append(product)
        return res

sol1 = Solution()
a = sol1.productExceptSelf([1,2,3])
print(a)
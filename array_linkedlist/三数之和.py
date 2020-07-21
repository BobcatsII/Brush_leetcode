#双指针法
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res, k = [], 0
        for k in range(len(nums)-2):
            if nums[k] > 0: break
            if k > 0 and nums[k] == nums[k-1]: continue

            i, j = k+1, len(nums)-1
            while i < j:
                s = nums[i] + nums[j] + nums[k]
                if s < 0:
                    i += 1
                    while i < j and nums[i] == nums[i - 1]: i += 1
                elif s > 0:
                    j -= 1
                    while i < j and nums[j] == nums[j + 1]: j -= 1
                else:
                    res.append([nums[k], nums[i], nums[j]])
                    i += 1
                    j -= 1
                    while i < j and nums[i] == nums[i - 1]: i += 1
                    while i < j and nums[j] == nums[j + 1]: j -= 1
        return res




#//哈希方法
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        neg = defaultdict(int)
        pos = defaultdict(int)
        for x in nums:
            if x>0 :
                pos[x] +=1
            else:
                neg[x] += 1

        ans = set()
        if 0 in neg and neg[0] >= 3:
            ans.add((0,0,0))
        for x in neg:
            for y in pos:
                if -x-y == y and pos[y] <2 or -x-y == x and neg[x] < 2:
                    continue
                if -x-y in pos or -x-y in neg :
                    ans.add(tuple(sorted([x,y,-x-y])))
        return list(ans)

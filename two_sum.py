#/usr/bin/python3

def twoSum():
        nums = [2, 7, 11, 15]
        target = 9
        integer = 0
        new_array = []
        b = 0
        for index, integer in enumerate(nums): # create two vars and list nums
            if nums[b] % target != 0:
                new_array.append(b)
            print(sum(new_array), nums[b])
twoSum()

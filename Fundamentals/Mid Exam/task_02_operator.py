nums = list(map(int,input().split()))
cmd = list(input().split())
while cmd[0]!="Finish":
    if cmd[0] == "Add":
        nums+=[int(cmd[1])]
    elif cmd[0] == "Remove":
        nums.remove(int(cmd[1]))
    elif cmd[0] == "Replace":
        index = nums.index(int(cmd[1]))
        nums[index] = int(cmd[2])
    elif cmd[0] == "Collapse":
        n = int(cmd[1])
        nums = [num for num in nums if num >= n]
    cmd = list(input().split())
print(' '.join(map(str,nums)))

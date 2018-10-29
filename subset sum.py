def subSetSumRecur(mySet, n, goal, lis):
    print(goal)
    if (goal == 0):
        return True
    if goal < 0 or n >= len(mySet):
        return False
    #including the element
    if subSetSumRecur(mySet, n + 1, goal - mySet[n], lis):
        lis.append(mySet[n])
        return True
    #excluding the elemrnt
    if subSetSumRecur(mySet, n + 1, goal, lis):
        return True
    return False


mySet=[]
nums = input("Enter the Elements").strip().split()
for x in nums:
    mySet.append(int(x))

goal = 0
subsum = int(input("Enter the Sum You want"))

for i in range(len(mySet)):
    lis = []
    subSetSumRecur(mySet[i:], 0, subsum, lis)
    if len(lis) > 1:
        print(lis)
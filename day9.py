
def parseFile():
    with open('input/input9.txt') as file:
        return [int(c) for c in file.read().rstrip()]

def part1(nums):
    # remove trailing space
    if len(nums) % 2 == 0:
        nums = nums[:len(nums) - 1]

    index = 0
    fileNumLeading = 0
    fileNumTrailing = len(nums) // 2
    sum = 0
    while len(nums) != 0:
        # process checksum for leading file
        n = nums[0]
        for _ in range(n):
            sum += fileNumLeading * index
            index += 1
        nums = nums[1:]
        fileNumLeading += 1

        if len(nums) == 0:
            break

        # process leading space by moving trailing files and processing checksum
        spaceSize = nums[0]
        while nums[-1] == 0:
            nums = nums[:len(nums) - 2]
            if len(nums == 0):
                break
            fileNumTrailing -= 1

        for _ in range(spaceSize):
            sum += fileNumTrailing * index
            index += 1
            nums[-1] -= 1

            if nums[-1] == 0:
                nums = nums[:len(nums) - 2]
                if len(nums) == 0:
                    break
                fileNumTrailing -= 1

        nums = nums[1:]

    return sum

def part2(nums):
    if len(nums) % 2 == 0:
        nums.pop(-1)

    files = nums[::2]
    spaces = nums[1::2]
    indices = [0]
    for n in nums[:-1]:
        indices.append(indices[-1] + n)
    fileIndices = indices[::2]
    spaceIndices = indices[1::2]

    sum = 0
    fileNum = len(files) - 1
    for file, fileIndex in zip(reversed(files), reversed(fileIndices)):
        if file != 0:
            foundSpace = False
            i = 0
            for space, spaceIndex in zip(spaces, spaceIndices):
                if space >= file:
                    foundSpace = True
                    index = spaceIndex
                    for _ in range(file):
                        sum += index * fileNum
                        index += 1
                    spaces[i] -= file
                    spaceIndices[i] += file
                    break
                i += 1

            if not foundSpace:
                index = fileIndex
                for _ in range(file):
                    sum += index * fileNum
                    index += 1

        fileNum -= 1
        spaces.pop(-1) if spaces else False
        files.pop(-1)
        spaceIndices.pop(-1) if spaceIndices else False
        fileIndices.pop(-1)

    return sum

nums = parseFile()
# print(part1(nums))
print(part2(nums))


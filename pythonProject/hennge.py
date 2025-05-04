import sys

def main():
    input_data = sys.stdin.read().splitlines()
    
    def process(index, acc):
        if index >= len(input_data):
            return acc
        x_line = input_data[index] if index < len(input_data) else ''
        x = int(x_line) if x_line.isdigit() else -1
        nums_line = input_data[index + 1] if index + 1 < len(input_data) else ''
        nums_strs = nums_line.strip().split()
        try:
            expected = int(x)
        except:
            return process(index + 2, acc + ['-1'])

        if len(nums_strs) != expected:
            return process(index + 2, acc + ['-1'])
        try:
            nums = list(map(int, nums_strs))
        except:
            return process(index + 2, acc + ['-1'])
        def calc(i, total):
            if i >= len(nums):
                return total
            val = nums[i]
            if val <= 0:
                return calc(i + 1, total + val ** 4)
            else:
                return calc(i + 1, total)
        result = calc(0, 0)
        return process(index + 2, acc + [str(result)])

    if len(input_data) == 0:
        return
    try:
        n = int(input_data[0])
    except:
        return
    results = process(1, [])
    print('\n'.join(results[:n]))

if __name__ == "__main__":
    main()

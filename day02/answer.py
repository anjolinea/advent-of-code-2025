
ranges = list()
with open("input.txt") as f:
    for line in f:
        ranges_str = line.split(",")
        for range_str in ranges_str:
            ranges.append(tuple(range_str.split("-")))

def part_one():
    ans = 0
    for low, up in ranges:
        range_ans = 0

        len_low = len(low)
        len_up = len(up)

        # did manual checking that len_up - len_low <= 1
        if len_low == len_up and len_low % 2 == 0:
            half_len = len_low // 2
            l_half_low = int(low[:half_len])
            l_half_up = int(up[:half_len])

            for x in list(range(l_half_low, l_half_up + 1)):
                num = int(str(x) + str(x))
                if int(low) <= num <= int(up):
                    range_ans += num
    
        # now len_low + 1 = len_up
        elif len_low % 2 == 0:
            half_len = len_low // 2
            l_half_low = int(low[:half_len])

            for x in range(l_half_low, 10 ** (half_len)):
                num = int(str(x) + str(x))
                if int(low) <= num <= int(up):
                    range_ans += num

        elif len_up % 2 == 0:
            half_len = len_up // 2
            l_half_up = int(up[:half_len])

            for x in range(10 ** (half_len-1), l_half_up+1):
                num = int(str(x) + str(x))
                if int(low) <= num <= int(up):
                    range_ans += num
        ans += range_ans
    print(ans)

def part_two():
    ans = 0

    seen_nums = set()
    max_l_len = max([len(up) // 2 for _, up in ranges])
    for low, up in ranges:
        for l_len in range(1, max_l_len+1):
            print(low, up, l_len)
            range_ans = 0
            len_low = len(low)
            len_up = len(up)

            if len_low == len_up and len_low % l_len == 0 and l_len < len_low:
                l_half_low = int(low[:l_len])
                l_half_up = int(up[:l_len])
                repeated = len_low // l_len

                for x in list(range(l_half_low, l_half_up + 1)):
                    num = int("".join([str(x)] * repeated))
                    if int(low) <= num <= int(up) and not(num in seen_nums):
                        seen_nums.add(num)
                        range_ans += num
            
            elif len_up > len_low:
                if len_low % l_len == 0 and l_len < len_low:
                    l_half_low = int(low[:l_len])
                    repeated = len_low // l_len

                    for x in range(l_half_low, 10 ** (l_len)):
                        num = int("".join([str(x)] * repeated))
                        if int(low) <= num <= int(up) and not(num in seen_nums):
                            seen_nums.add(num)
                            range_ans += num
                
                if len_up % l_len == 0 and l_len < len_up:
                    l_half_up = int(up[:l_len])
                    repeated = len_up // l_len

                    for x in range(10 ** (l_len-1), l_half_up+1):
                        num = int("".join([str(x)] * repeated))
                        if int(low) <= num <= int(up) and not(num in seen_nums):
                            seen_nums.add(num)
                            range_ans += num

            ans += range_ans
    print(ans)
                
part_two()
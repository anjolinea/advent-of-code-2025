
banks = list()
with open("input.txt") as f:
    for line in f:
        banks.append([int(x) for x in list(line) if x.isnumeric()])


def part_one():
    ans = 0
    for bank in banks:
        first_batt_val = max(bank[:-1])
        first_batt_ind = bank.index(first_batt_val)
        second_batt_val = max(bank[first_batt_ind+1:])
        ans += first_batt_val * 10 + second_batt_val

    print(ans)


def part_two():
    ans = 0
    for bank in banks:
        val = 0
        chars_ind_before = 0
        for x in range(12):
            chars_needed_after = 12-x-1
            if chars_needed_after == 0:
                x_batt_val = max(bank[chars_ind_before:])
            else:
                x_batt_val = max(bank[chars_ind_before:-chars_needed_after])
            x_batt_ind = bank.index(x_batt_val, chars_ind_before)
            chars_ind_before = x_batt_ind+1
            val += x_batt_val * (10 ** chars_needed_after)
        ans += val
    
    print(ans)

part_two()
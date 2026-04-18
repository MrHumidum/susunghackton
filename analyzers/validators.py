import re


def validate_snils(snils_str):
    nums = "".join(re.findall(r'\d', snils_str))
    if len(nums) != 11:
        return False

    main_part = nums[:9]
    check_sum = int(nums[9:])

    res = 0
    for i in range(9):
        res += int(main_part[i]) * (9 - i)

    if res < 100:
        calc_sum = res
    elif res == 100 or res == 101:
        calc_sum = 0
    else:
        calc_sum = res % 101
        if calc_sum == 100:
            calc_sum = 0

    return calc_sum == check_sum

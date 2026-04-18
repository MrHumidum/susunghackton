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

def validate_inn(inn):
    nums = re.sub(r"\D", "", inn)

    if len(nums) not in (10, 12):
        return False

    return True  # можно усложнить позже контрольными суммами

def luhn_check(card_number):
    digits = [int(d) for d in re.sub(r"\D", "", card_number)]
    
    if len(digits) < 13 or len(digits) > 19:
        return False

    checksum = 0
    reverse = digits[::-1]

    for i, d in enumerate(reverse):
        if i % 2 == 1:
            d *= 2
            if d > 9:
                d -= 9
        checksum += d

    return checksum % 10 == 0

def validate_results(results):
    validated = {}

    for key, values in results.items():
        valid = []

        for v in values:
            if key == "SNILS" and not validate_snils(v):
                continue
            if key == "CARD" and not luhn_check(v):
                continue
            if key == "INN" and not validate_inn(v):
                continue

            valid.append(v)

        if valid:
            validated[key] = valid

    return validated

def classify_uz(data):
    categories = set(data.keys())

    count = sum(len(v) for v in data.values())

    if "SPECIAL" in categories or "BIOMETRIC" in categories:
        return "УЗ-1"

    if any(c in categories for c in ["CARD", "ACCOUNT", "BIK"]) and count > 10:
        return "УЗ-2"

    if any(c in categories for c in ["PASSPORT", "SNILS", "INN"]):
        if count > 10:
            return "УЗ-2"
        return "УЗ-3"

    if count > 20:
        return "УЗ-3"

    return "УЗ-4"
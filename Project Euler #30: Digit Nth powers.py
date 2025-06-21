def sum_of_digit_powers(power):
    digit_powers = [d ** power for d in range(10)]

    max_digits = 1
    while max_digits * digit_powers[9] >= 10 ** (max_digits - 1):
        max_digits += 1
    upper_limit = max_digits * digit_powers[9]

    total_sum = 0
    for num in range(2, upper_limit + 1):
        s = 0
        n = num
        while n > 0:
            s += digit_powers[n % 10]
            if s > num:
                break
            n //= 10
        if s == num:
            total_sum += num

    return total_sum

power = int(input())
print(sum_of_digit_powers(power))

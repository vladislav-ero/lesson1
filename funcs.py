def get_summ(first, second, delimiter="&"):
    first = str(first).upper()
    second = str(second).upper()
    return f"{first}{delimiter}{second}"


to_print = get_summ("Learn", "python", delimiter='&')
print(to_print)

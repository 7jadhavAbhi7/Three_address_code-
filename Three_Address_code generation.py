def generate_three_address_code():
    code = []
    t_count = 1

    def new_temp():
        nonlocal t_count
        temp = f"t{t_count}"
        t_count += 1
        return temp

    def gen_code(op, arg1, arg2, target):
        code.append((op, arg1, arg2, target))

    u = "u"
    v = "v"
    w = "w"
    t1 = new_temp()
    t2 = new_temp()
    t3 = new_temp()
    t4 = new_temp()
    t5 = new_temp()

    gen_code("*", u, u, t1)
    gen_code("*", u, v, t2)
    gen_code("-", t1, t2, t3)
    gen_code("*", v, v, t4)
    gen_code("+", t3, t4, t5)
    gen_code("=", t5, None, w)

    return code

three_address_code = generate_three_address_code()

# Printing the generated three-address code
for operation in three_address_code:
    op, arg1, arg2, target = operation
    if arg1 is not None and arg2 is not None:
        print(f"{target} = {arg1} {op} {arg2}")
    elif arg1 is not None:
        print(f"{target} = {arg1}")
    else:
        print(f"{target} = {op}")

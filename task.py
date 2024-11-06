def new_sum(*args):
    sum_ = 0
    for num in args:
        sum_ += num
    return sum

print(new_sum(1,5,3,4,5))

def get_personal_data(**kwargs):
    print(type(kwargs))
    print(kwargs)
    print(kwargs['name'])
    print(kwargs['surname'])
    print(kwargs['age'])
    print(kwargs['phone'])

get_personal_data(name = "Дмитрий",surname = 'Таушев', age = 28, phone = +79825657627)
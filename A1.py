from math import *


def is_deletable(s):
    # 用于删去多余的括号，例如(x+1)变为x+1；避免(x+1)*(x+2)变为x+1)*(x+2
    if s[0] != '(':
        return False
    if '(' not in s:
        return False
    if len(s) < 3:
        return False
    count = 0
    t = 0
    for x in s:
        if x == '(':
            count += 1
        if x == ')':
            count -= 1
        if 1 < t < len(s) - 1 and count == 0:
            return False
        t += 1
    return True


def qiudao(f):
    while is_deletable(f):
        f = f[1:-1]
    result = ''
    count = 0
    collect = ''
    chengfa = False
    part_1 = ''
    for x in f:
        if x == '(':
            count += 1
        if x == ')':
            count -= 1
        if x in '+-' and count == 0 and not chengfa:
            result += qiudao(collect) + x
            collect = ''
        elif x == '*' and count == 0 and not chengfa:
            chengfa = True
            part_1 = collect
            collect = ''
        elif x in '+-' and count == 0 and chengfa:
            chengfa = False
            result += '((' + qiudao(part_1) + ')*(' + collect + ')+(' + part_1 + ')*(' + qiudao(collect) + '))' + x
            collect = ''
        else:
            collect += x
    if collect == f:
        try:
            if 'x' not in f:
                return '0'
            raise
        except:
            if f[:3] == 'log' and is_deletable(f[3:]):  # 对数函数
                return '(' + qiudao(f[4:-1]) + ')*(' + f[4:-1] + ')**(-1)'
            elif f == 'x':
                return '1'
            elif f[:3] == 'sin':
                return '(' + qiudao(f[4:-1]) + ')*cos(' + f[4:-1] + ')'
            elif f[:3] == 'cos':
                return '(' + qiudao(f[4:-1]) + ')*sin(' + f[4:-1] + ')*(-1)'
            elif '^' in f:
                m, n = tuple(f.split('^'))
                if 'x' in m and 'x' not in n:
                    return '(' + qiudao(m) + ')*(' + n + ')*(' + m + ')**(' + str(eval(n) - 1) + ')'  # 幂函数
                if 'x' not in m and 'x' in n:
                    return '(' + qiudao(n) + ')*log(' + m + ')*' + f #指数函数
                if 'x' not in m+n:
                    return '0' #常数
            else:
                return "###"
    elif not chengfa:
        result += qiudao(collect)
        return result
    else:
        result += '((' + qiudao(part_1) + ')*(' + collect + ')+(' + part_1 + ')*(' + qiudao(collect) + '))'
        return result


if __name__ == '__main__':
    text = input('y = ').replace('**', '^').lower()
    p = qiudao(text).replace('^', '**')
    print("y' =", p)
    e = 2.718281828459045
    pi = 3.141592653589793
    for x in range(10):
        argument = {'a': 10} #定义函数参数
        for key in argument:
            exec(f'{key} = {str(argument[key])}')
        try:
            print(f"x = {x}, y' =", eval(p))
        except:
            print(f"x = {x}, y' 不存在")

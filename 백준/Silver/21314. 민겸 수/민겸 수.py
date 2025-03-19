# 민겸 수
import sys

def max_num():
    converted = ""
    tmp = ""
    for n in num:
        if n == "K":
            converted += "5" + "0" * tmp.count("M")
            tmp = ""

        else:
            tmp += "M"

    if tmp:
        converted += "1" * tmp.count("M")

    return converted

def min_num():
    converted = ""
    tmp = ""
    for n in num:
        if n == "K":
            if len(tmp) >= 2:
                converted += "1" + "0" * (tmp.count("M") - 1) + "5"

            elif len(tmp) == 1:
                converted += "1" + "5"

            else:
                converted += "5"

            tmp = ""

        else:
            tmp += "M"

    if tmp:
        converted += "1" + "0" * (tmp.count("M") - 1)

    return converted

num = list(sys.stdin.readline().rstrip())

print(max_num())
print(min_num())
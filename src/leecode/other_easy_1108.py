def defangIPaddr(str):
    return str.replace(".", "[.]")


str = "1.1.1.1"

a = defangIPaddr(str)
print(a)

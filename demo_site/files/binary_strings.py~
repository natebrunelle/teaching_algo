def list_strings(n):
    """lists all binary strings of length n"""
    if n == 0:
        return [""]
    else:
        strings = []
        for b in list_strings(n-1):
            strings.append(b+"0")
            strings.append(b+"1")
        return strings

print(list_strings(0))
print(list_strings(1))
print(list_strings(2))
print(list_strings(3))

def string_length(b):
    if b == "":
        return 0
    else:
        return string_length(b[:-1]) + 1
        
print(string_length('111'))

def string_to_nat(b):
    if b == "":
        return 0
    else:
        return 2 * string_to_nat(b[:-1]) + int(b[-1])
        
print(string_to_nat('1101'))

def nat_to_string(x):
    if x == 0:
        return ""
    else:
        return nat_to_string(x//2) + str(x % 2)
        
print(nat_to_string(13))
        

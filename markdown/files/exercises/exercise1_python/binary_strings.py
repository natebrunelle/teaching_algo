
""" This function enumerates all binary strings of a certain length. This will primarily be used for testing purposes."""
def list_strings(n):
    """lists all binary strings of length n, do not modify this function"""
    if n == 0:
        return [""]
    else:
        strings = []
        for b in list_strings(n-1):
            strings.append(b+"0")
            strings.append(b+"1")
        return strings
        


"""The next two functions together implement the procedure for representing natural numbers using binary strings that was presented in class. The first function will "encode" a natural number into a string. The second function will "decode" a string into a natural number."""        

def string_to_nat(b):
    """Given a binary string, converts it into a natural number by the procedure described in lecture.  Do not modify this function."""
    if b == "":
        return 0
    else:
        return 2 * string_to_nat(b[:-1]) + int(b[-1])
        

def nat_to_string(x):
    """Given a natural number, converts it into a binary string by the procedure described in lecture.  Do not modify this function."""
    assert(x >= 0)
    if x == 0:
        return ""
    else:
        return nat_to_string(x//2) + str(x % 2)





"""The next two functions will together define a way of representing integers using binary strings. The first function will "encode" an int into a string. The second function will "decode" a string into an int. There are many ways to do this successfully. I recommend using the nat_to_string and string_to_nat functions I provided to help you out, but that is not required."""


def int_to_string(x):
    """TODO: Implement a procedure to convert a given integer into a binary string. This mapping should be injective, but not necessarily bijective. In other words, come up with the mapping from an int to a string representation for it."""
    return ""

def string_to_int(b):
    """TODO: Implement a procedure to convert a given binary string into an integer. This mapping should be surjective, but not necessarily bijective. Additionally, this function must do the inverse of the previous function. That is, if I represent an int as a string using the previous function, then give the result to this function, I should get the original int back."""
    return 0

# Tests whether string_to_int is defined for all (well, ... many) strings. Do not modify this code (or if you do, restore it to the original).
for i in range(12):
    for b in list_strings(i):
        string_to_int(b)
    

# Tests whether decode undoes the encode. Do not modify this code (or if you do, restore it to the original).
test_ints = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 100, 10000, 123456789]
for i in range(len(test_ints)):
    test_ints.append(-test_ints[i])

for i in test_ints:
    assert(string_to_int(int_to_string(i)) == i)
print("Looks like your integer representation works! HOORAY!!")


"""The next two functions will together define a way of representing integer cartesian coordinates (i.e. ordered pairs of integers) using binary strings. The first function will "encode" a coordinate pair into a string. The second function will "decode" a string into a cordinate pair. There are many ways to do this successfully. I recommend using the int_to_string and string_to_int functions you implemented, but that is not required."""

def coord_to_string(c):
    """TODO: Implement a procedure to convert a given coordinate pair of integers into a binary string. This mapping should be injective, but not necessarily bijective. In other words, come up with the mapping from a coordinate pair to a string representation for it."""
    return ""

def string_to_coord(b):
    """TODO: Implement a procedure to convert a given binary string into a coordinate pair of integers. This mapping should be surjective, but not necessarily bijective. Additionally, this function must do the inverse of the previous function. That is, if I represent a coordinate pair as a string using the previous function, then give the result to this function, I should get the original coordinate pair back. This function must be defined for all strings, i.e. even if your coord_to_string function only ever produces even-length strings, this function must still produce a coordinate pair for odd-length strings."""
    return (0,0)


# Tests whether string_to_int is defined for all (well, ... many) strings. Do not modify this code (or if you do, restore it to the original).
for i in range(12):
    for b in list_strings(i):
        string_to_coord(b)


# Tests whether decode undoes the encode. Do not modify this code (or if you do, restore it to the original).
test_coords = []
for x in test_ints:
    for y in test_ints:
        test_coords.append((x,y))

for i in test_coords:
    assert(string_to_coord(coord_to_string(i)) == i)
print("Looks like your Cartesian representation is working. You're done!!")




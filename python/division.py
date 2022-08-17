# The provided code stub reads two integers,  and , from STDIN.
# Add logic to print two lines. The first line should contain the result of integer division, a // b. The second line should contain the result of float division, a / b.
# No rounding or formatting is necessary.

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    integer_division = a//b
    float_division = a/b
    print(integer_division)
    print(float_division)
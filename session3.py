from fractions import Fraction
def encoded_from_base10(number, base, digit_map):
    '''
    This function returns a string encoding in the "base" for the the "number" using the "digit_map"
    Conditions that this function must satisfy:
    - 2 <= base <= 36 else raise ValueError
    - invalid base ValueError must have relevant information
    - digit_map must have sufficient length to represent the base
    - must return proper encoding for all base ranges between 2 to 36 (including)
    - must return proper encoding for all negative "numbers" (hint: this is equal to encoding for +ve number, but with - sign added)
    - the digit_map must not have any repeated character, else ValueError
    - the repeating character ValueError message must be relevant
    - you cannot use any in-built functions in the MATH module

    '''
    if base<2 or base>36:
        raise ValueError("Invalid base Error!.Please Provide a base between 2 and 36 including both. We can also make the base as the length of the digit_map if that is required ")
    if base != len(digit_map):
        raise ValueError("Invalid Length Error! The Length of the digit map and base are not matching , Please check the input perfectly") 
    digit_map_set = set(digit_map)
    if base != len(digit_map_set):
        raise ValueError("Non Unique Character Error! Your digit_map base is not having all unique characters.Its repeating Please check ") 
    result = ""
    temp_no = number
    if number < 0:
        number = -(number)    
    while number:
        result+=digit_map[number%base]
        number//= base
    if temp_no < 0:
        result+= '-' 
    temp_no = None
    return result[::-1]


def float_equality_testing(a, b):
    '''
        This function emulates the ISCLOSE method from the MATH module, but you can't use this function
        We are going to assume:
        - rel_tol = 1e-12
        - abs_tol = 1e-05
    '''
    if a < 0:
        a = -a
    if b < 0:
        b = -b
    return (a- b) < 1e-05


def manual_truncation_function(f_num):
    '''
    This function emulates python's MATH.TRUNC method. It ignores everything after the decimal point. 
    It must check whether f_num is of correct type before proceed. You can use inbuilt constructors like int, float, etc
    '''

    s=str(f_num)
    sub_str=s[0:s.index(".")]
    f=Fraction(sub_str)
    return f.numerator

def manual_rounding_function(f_num):
    '''
    This function emulates python's inbuild ROUND function. You are not allowed to use ROUND function, but
    expected to write your one manually.
    '''
    s=str(f_num)
    sub_str=s[0:s.index(".")]
    sub_str_dec=s[s.index(".")+1:len(s)]
    num=Fraction(sub_str)
    dec=Fraction(sub_str_dec)
    if dec > 50:
        num = num +1
    else:
        num  = num  
    return num

def rounding_away_from_zero(f_num):
    '''
    This function implements rounding away from zero as covered in the class
    Desperately need to use INT constructor? Well you can't. 
    Hint: use FRACTIONS and extract numerator. 
    '''
    return 3.0
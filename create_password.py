

import string

def long_enough(pw):
    'Password must be at least 6 characters'
    print len(pw)
    return len(pw) >= 6

def short_enough(pw):
    'Password cannot be more than 12 characters'
    return len(pw) <= 12

def has_lowercase(pw):
    'Password must contain a lowercase letter'
    return len(set(string.ascii_lowercase).intersection(pw)) > 0

def has_uppercase(pw):
    'Password must contain an uppercase letter'
    return len(set(string.ascii_uppercase).intersection(pw)) > 0

def has_numeric(pw):
    'Password must contain a digit'
    return len(set(string.digits).intersection(pw)) > 0

def has_special(pw):
    'Password must contain a special character'
    return len(set(string.punctuation).intersection(pw)) > 0

def test_password(pw, tests=[long_enough, short_enough, has_lowercase, has_uppercase, has_numeric, has_special]):
    for test in tests:
        if not test(pw):
            print(test.__doc__)
            return False
    return True

def main():
    pw = input('Please enter a test password:')
    print pw
    if test_password(pw):
        print('That is a good password!')

if __name__=="__main__":
    main()

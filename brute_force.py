import itertools
import string

def brute_force(target):
    chars = string.ascii_letters + string.digits + "!@#$%&*"
    
    for length in range(1, 6):
        for attempt in itertools.product(chars, repeat=length):
            attempt = ''.join(attempt)
            print("Deniyorum:", attempt)
            if attempt == target:
                return attempt

password = "asd"
found = brute_force(password)
print("Şifre bulundu:", found)

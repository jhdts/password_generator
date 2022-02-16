# -----------------------

from random import randint
from urllib.parse import urlparse
from validators import url

# ------------------------
t = input().replace(' ', '')
if url(t):
    t = urlparse(t).netloc
    for s in ['.com', '.net', '.ru']:
        t = t.removesuffix(s)
    t = t.removeprefix('www.')

def add_upper_case(c, i):
    if i % 4 == 2:
        if c.isupper():
            c = c.lower()
        else:
            c = c.upper()
    return c

l = [add_upper_case(t[i], i) for i in range(0, len(t), 2)]

password = ''.join(l)
password = password.replace(password[randint(0, len(password) - 1)], '_+$', 1)
password += str(randint(0, 1000))
print(password)




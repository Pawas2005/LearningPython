import string

def code(s):
    letters = string.ascii_lowercase
    rep_dict = dict(zip(letters, letters[::-1]))
    a = ''.join(map(rep_dict.get, s.replace(" ", "").lower()))
    print(a)
s=input()
code(s)


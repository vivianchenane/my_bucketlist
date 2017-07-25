import urlib.request

v= urlib.request.urlopen('https://api.github.com/users/vivianchenane/')
print(v.read())

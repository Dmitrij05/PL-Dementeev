s = input().lower()
a = len(s) // 2
s = s[:a].replace('п', '*') + s[a:]
print(s)

s = input()
for i in s.split():
    if i.startswith('а') or i.endswith('я'):
        print(i)
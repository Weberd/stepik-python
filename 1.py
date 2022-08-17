#a, b, c = map(int, input().split())
#a = int(input())

i = {}

def search(parent, child):
    print(parent, child)
    if parent == child:
        return True
    if child not in i:
        return False
    if parent in i[child]['parents']:
        return True
    res = False
    for current_parent in i[child]['parents']:
        res = res or search(parent, current_parent)
    return res

n = int(input())
for a in range(n):
    inherit = input().split(' : ')
    child = ''
    parents = ''
    if len(inherit) > 1:
        child = inherit[0]
        parents = inherit[1]
    else:
        child = inherit[0]
    parents = parents.split()
    if not child in i:
        i[child] = {'parents': []}
    for parent in parents:
        if parent not in i:
            i[parent] = {'parents': []}
        i[child]['parents'].append(parent)

print(i)

n = int(input())

for a in range(n):
    parent, child = input().split()
    print('Yes') if search(parent, child) else print('No')

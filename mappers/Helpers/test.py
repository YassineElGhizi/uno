import math

a = [
    1,2,
    3,4,
    5,6,
    7,8,
    9,
]
obe_by_req=2
nb_req = math.ceil(len(a) / obe_by_req)

reqs = []
tmp = []

for num , k in enumerate(a):
    tmp.append(k)
    if (num+1) == len(a):
        reqs.append(tmp)
    if (num+1) % obe_by_req == 0:
        reqs.append(tmp)
        tmp = []
        continue

print(len(reqs))
for N , byreq in enumerate(reqs) :
    print(f"==============={N}================")
    print(byreq)
    print("\n")
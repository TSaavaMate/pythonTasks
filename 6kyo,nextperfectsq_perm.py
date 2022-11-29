import itertools
from math import sqrt, floor


def isPerfect(N):
    if sqrt(N) - floor(sqrt(N)) != 0:
        return False
    return True


def next_perfectsq_perm(lower_limit, k):
    # your code here
    i = 0
    while i < lower_limit:
        lower_limit += 1
        if isPerfect(lower_limit):
            if not str(lower_limit).__contains__("0"):
                n = lower_limit
                results = list(set(("".join(x)) for x in list(itertools.permutations(list(str(n))))))
                squarenumbers = 0
                maxsquarenumber = 0
                for z in results:
                    if isPerfect(int(z)):
                        squarenumbers += 1
                        if maxsquarenumber < int(z):
                            maxsquarenumber = int(z)
                if squarenumbers == k:
                    return maxsquarenumber


print(next_perfectsq_perm(200, 2))

# maximum perfect square of the set of
# permutations generated by the closest
# but higher perfect square than limit_below
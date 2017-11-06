# def factors(n):
#     results = []
#     for k in range(1, n+1):
#         if n % k == 0:
#             results.append(k)
#     return results

# print(factors(10))

# def factors(n):
#     for k in range(1, n+1):
#         if n % k == 0:
#             yield k # yield this factor as next result
#         #yield also indicates to python we are defining a generator, rather than traditional function
#
# for j in (factors(10)):
#     print(j)


def factors(n):
    k = 1
    while k * k < n:
        if n % k == 0:
            yield k
            yield n // k
        k += 1
    if k * k == n:
        yield k

for j in factors(10):
    print(j)

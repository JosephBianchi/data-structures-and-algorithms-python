# if n >= 0:
#     param = n
# else:
#     param = -n
# result = foo(param)
#
# param = n if n >=0 else -n
# result = foo(param)
#  # or
#
#  result = foo(n if n >= 0 else -n)
#
#  [ expression for value in iterable if condition ]
#
# result = []
# for value in iterable:
#     if condition:
#         result.append(expression)
#
# squares = []
# for k in range(1, n+1):
#     squares.append(k*k)

# or
#
# squares = [k*k for k in range(1, 20+1)]
#
# print(squares)
#
#
# factors = [k for k in range(1, 10+1) if 10 % k == 0]
# print(factors)

# print({k: k*k for k in range(1, 10+1)})

# for (x,y) in [(7,2), (5,8), (6,4)]:
#     print(x)
#     print(y)
#     print(x,y)

# for k, v in {"a":1, "b":2}:
#     print(k)


a = {"a":1, "b":2}
a.items()

#Naive recursive algorithm
# def fib(n):
#     if n <= 2:
#         f = 1
#     else:
#         f = fib( n - 1 ) + fib( n - 2 )
#     return f
# print(fib(27))
#Exponential time --> Very bad
# T(n) = T(n-1) + T(n-2) + C
# T(n) >= 2(T(n-2))
# T(n) = theta(2^(n/2))
# ------------------------------------------------------
# Memorized DP algorithm
# memo = {}
# def fib(n):
#     if n in memo:
#         return memo[n]
#     elif n <= 2:
#         f = 1
#     else:
#         f = fib( n - 1 ) + fib( n - 2 )
#     memo[n] = f
#     return f
# print(fib(27))

# Fib(k) only recurses the first time it is called, for every k
# Memorized calls cost constant time --> theta(1)
# No. of non memorized calls is n
# fib(1), fib(2),....,fib(n) will be called at once --> Exactly n calls
# Non recursive work per call is constant
# Therefore the running time is constant
# Time = theta(n)

#In DP
# -------
# memoize (remember)
# & reuse the solutions
# To figure out subproblems
# Designed to help solve the actual problems

#  DP ==> Recursion + Memoization
#  Running time =  number of subproblems we solve * amount of time spent on each subproblems

#  Don't count memoize recursions!!
# --------------------------------------------------------------------------------------------------------------
# Bottom-up DP algorithm
# -----------------------
# fib = {}
# for k in range(n+1):
#     if k <= 2:
#         f= 1
#     else:
#         f = fib[k-1] +fib[k-2]
#     fib[k] = f
# return fib[n]

# Exactly same computation
# Topological sort of subproblem dependency DAG (Directed Acyclic Graphs)
# Can often save space

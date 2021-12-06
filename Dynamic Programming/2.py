# Shortest Paths
# ------------------------------
# Shortest pathway from S-->V for all V
# Tool : Guessing =: Dont know the answer? Guess!
# Try all guesses!! (& take the best one)
# DP ==> Recursion + Memoizing + Guessing

# S --> () --> () --> () --> () --> V
# 1.Guess first edge approach --> Guessing the edges from the first point (S) and then guessing the 
# shortest path from the first best landing point ..--> Where S changes to the landing point

# S --> () --> () --> () --> (u) --> V
# 2. Delta(s,u) = Finding the last edge leading to V from u and then finding and adding the best shortest path from S to u.
# Delta(S,V) = min(delta(S,u)) + w(u,V) for all (u,V) in Edges
# This is a recursive call and hence it is a recursive algorithm ::--> Very bad and Terrible

# Delta of V is stored in Memoizing table (since S is not changing)

# Infinite time on graphs with cycles!!!
# For DAGs --> O(V+E)
# Time for subproblem delta(S,V) = indegree(V) ;Number of edges coming to V

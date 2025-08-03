s1 = {1, 45, 6, 78}
s2 = {7, 8, 1, 78}

print(s1.union(s2))
print(s2.union(s1))
union_equality = s1.union(s2) == s2.union(s1)
print(union_equality)

print(s1.intersection(s2))
print(s2.intersection(s1))
intersection_equality = s1.intersection(s2) == s2.intersection(s1)
print(intersection_equality)
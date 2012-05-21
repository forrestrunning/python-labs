even_numbers=(x for x in range(11) if x%2==0)
print even_numbers #See that just the object reference is ready, needs iteration to compute

for x in even_numbers:
    print x
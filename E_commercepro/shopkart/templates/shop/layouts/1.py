def generate_sequence(n):
    sequence = []
    value = 2
    for i in range(n):
        sequence.append(value)
        value *= 2
    return sequence

# Number of terms to generate
n = 30

# Generate the sequence
sequence = generate_sequence(n)

print(sequence)


    


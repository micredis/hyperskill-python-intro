synthesis_index = float(input())
if synthesis_index < 2:
    print("Analytic")
elif 2 <= synthesis_index <= 3:
    print("Synthetic")
else:
    print("Polysynthetic")
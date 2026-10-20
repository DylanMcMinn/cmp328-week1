scores = [42, 61, 75, 58, 90]
for i, s in enumerate(scores, start=1):
    print (f"{i}: {s}")
avg = sum(scores) / len(scores)
print("Average:", round(avg, 2))
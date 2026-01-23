from itertools import combinations

weights = [7,3,4,5]
values = [42,12,40,25]
capacity = 10
n = len(weights)

best_value = 0
best_subset = None

print("Subset\t\tTotal Weight\tTotal Value")
print("-"*45)

for r in range(n+1):
    for subset in combinations(range(n),r):
        total_weight = sum(weights[i] for i in subset)
        total_value = sum(values[i] for i in subset)
        subset_display = "{"+",".join(str(i+1) for i in subset)+"}"\
        
        if total_weight <= capacity:
            print(f"{subset_display:<15}{total_weight<15} ${total_value}")
            if total_value > best_value:
                best_value = total_value
                best_subset = subset
        else:
            print(f"{subset_display:<15}{total_weight<15} Not feasible")

print("\nOptimal Soulution")
print("Item Selected:",{i+1 for i in best_subset})
print("Maximum Value: $",best_value)

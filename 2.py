# Create the two sets of two guest lists
guest_set1 = {'A', 'B', 'C', 'D', 'E'}
guest_set2 = {'B', 'D', 'V', 'X', 'Y', 'Z'}

# Find union of two sets
combined_guests = guest_set1.union(guest_set2)

# Converting set into list
# to find total guests to be invited in party
guest_list = list(combined_guests)

print("Total guests to be invited in party are :", len(guest_list))
print("Guest List :", guest_list)

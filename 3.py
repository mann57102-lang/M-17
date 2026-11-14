# Create the two sets of two guest lists
guest_set1 = {'A', 'B', 'C', 'D', 'E'}
guest_set2 = {'B', 'D', 'V', 'X', 'Y', 'Z'}

# Find intersection of two sets
common_guests = guest_set1.intersection(guest_set2)

# Converting set into list
# to find total guests to be invited in party
guest_list = list(common_guests)

print("Total guests to be invited in party are :", len(guest_list))
print("Guest List :", guest_list)

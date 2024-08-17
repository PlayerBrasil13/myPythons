blocks = int(input("Enter the number of blocks: "))
blocks_in_layer = 1
height = 0

while blocks >= blocks_in_layer:
    blocks -= blocks_in_layer
    blocks_in_layer += 1
    height += 1

print("The height of the pyramid:", height)

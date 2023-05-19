number_of_lines = int(input())
tank_capacity = 255
water_counter = 0

for current_line in range(number_of_lines):
    litters_of_water = int(input())
    if (tank_capacity - litters_of_water) < 0:
        print("Insufficient capacity!")
        continue
    tank_capacity -= litters_of_water
    water_counter += litters_of_water

print(water_counter)
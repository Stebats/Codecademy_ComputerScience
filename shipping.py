weight = 41.5
cost_ground_premium = 125

#Ground Shipping
if weight <= 2:
  cost_ground = weight * 1.5 + 20
elif weight <= 6:
  cost_ground = weight * 3 + 20
elif weight <= 10:
  cost_ground = weight * 4 + 20
else:
  cost_ground = weight * 4.75 + 20
print(cost_ground + cost_ground_premium)

#Drone shipping
if weight <= 2:
  cost_drone = weight * 4.5 + 0
elif weight <= 6:
  cost_drone = weight * 9 + 0
elif weight <= 10:
  cost_drone = weight * 12 + 0
else:
  cost_drone = weight * 14.25 + 0
print(cost_drone)

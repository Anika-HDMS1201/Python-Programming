distance_km = 185
bike_mileage = 45.5 #km per liter
petrol_price = 106.50
budget_str = "Total Budget: Rs. 500"

budget=float(budget_str[18:])
total_litres_fuel_req=(distance_km/bike_mileage)
total_cost_trip=(total_litres_fuel_req*petrol_price)

approval="Trip Approved" if budget>=total_cost_trip else "Need More Cash"
print(approval) 



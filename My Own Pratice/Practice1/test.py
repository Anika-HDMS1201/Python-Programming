attendance = [1, 0, 1, 1, 0, 1, 1]
#Write a program to:
#Count the number of days present (1).
#Count the number of days absent (0).
#Calculate attendance percentage.
#Print "Eligible" if attendance ≥ 75%, otherwise "Not Eligible"

# Count days present and absent
days_present = attendance.count(1)
days_absent = attendance.count(0)
total_days = len(attendance)

# Calculate attendance percentage
attendance_percentage = (days_present / total_days) * 100

# Print results
print(f"Days Present: {days_present}")
print(f"Days Absent: {days_absent}")
print(f"Attendance Percentage: {attendance_percentage:.2f}%")

# Check eligibility
if attendance_percentage >= 75:
    print("Eligible")
else:
    print("Not Eligible")





"""
Q2
prices = (450, 1200, 750, 3000, 1800)
Using a loop:

Count products costing more than ₹1000.
Find the most expensive product price.
Find the cheapest product price.
Calculate the average price.
Do not use any in-built function.
"""

prices = (450, 1200, 750, 3000, 1800)

# Count products costing more than ₹1000
count_above_1000 = 0
for price in prices:
    if price > 1000:
        count_above_1000 += 1

# Find most expensive product using a loop
most_expensive = prices[0]
for price in prices:
    if price > most_expensive:
        most_expensive = price

# Find cheapest product using a loop
cheapest = prices[0]
for price in prices:
    if price < cheapest:
        cheapest = price

# Calculate average price using a loop
total = 0
for price in prices:
    total += price
average_price = total / len(prices)

# Print results
print(f"Products costing more than ₹1000: {count_above_1000}")
print(f"Most Expensive Price: ₹{most_expensive}")
print(f"Cheapest Price: ₹{cheapest}")
print(f"Average Price: ₹{average_price:.2f}")
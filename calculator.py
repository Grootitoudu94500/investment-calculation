start = int(input("Starting number : "))
percentage = float(input("Percentage number : "))
years = int(input("Number of years : "))
def calculation(initial_amount, rate, duration):
  total = initial_amount
  for i in range(duration):
    total = total + (total * rate / 100)
  pure_gain = total - initial_amount
  return pure_gain
final_result = calculation(start, percentage, years)
print(f"The gain is {final_result:.2f} or {final_result + start:.2f}")

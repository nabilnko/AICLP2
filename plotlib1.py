import matplotlib.pyplot as plt
days = ["SAT", "SUN", "MON", "TUE", "WED", "THU", "FRI"]
temperatures = [20, 22, 23, 21, 19, 18, 17]
plt.plot(days, temperatures, marker='o', linestyle='-', color='b')
plt.xlabel("Day")
plt.ylabel("Temperature in '°C'")
plt.title("Temperature Over a Week")
plt.show()
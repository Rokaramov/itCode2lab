import datetime

day = datetime.datetime.now().strftime("%d")
month = datetime.datetime.now().strftime("%B")
temperature = -16

print("Сегодня", day, month, "На улице", temperature, "градусов.")

if temperature < 0:
    print("Холодно, лучше остаться дома.")

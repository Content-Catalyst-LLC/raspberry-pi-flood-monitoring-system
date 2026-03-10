import statistics

water_series = [122, 125, 127, 130, 161]

mean = statistics.mean(water_series)
stdev = statistics.pstdev(water_series)

latest = water_series[-1]

if latest > mean + 2 * stdev:
    print("Possible flood anomaly detected.")
else:
    print("No anomaly detected.")

import csv
import datetime

def log_data(water_level_cm, rainfall_mm, pressure_hpa):
    with open("flood_log.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([
            datetime.datetime.now().isoformat(),
            water_level_cm,
            rainfall_mm,
            pressure_hpa
        ])

if __name__ == "__main__":
    log_data(142.5, 12.4, 1003.2)
    print("Sample flood monitoring record written.")

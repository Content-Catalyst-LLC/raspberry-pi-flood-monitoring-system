def check_alerts(water_level_cm, rainfall_mm):
    if water_level_cm > 180:
        print("Flood warning: river level exceeded threshold")

    if rainfall_mm > 50:
        print("Heavy rainfall warning")

if __name__ == "__main__":
    check_alerts(192, 61)

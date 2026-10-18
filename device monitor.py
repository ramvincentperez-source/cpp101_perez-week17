readings = [28, 31, 35, 37, 29] 
"""
Simulated Device Monitoring and Alert System
Name: Perez Ram Vincent B
Section: 1CPE-B
Course: CPP102 - Programming Logic and Design
Program: Bachelor of Science in Computer Engineering
Pamantasan ng Cabuyao
"""

def is_whole_number(text):
    """Return True if text is a valid non-negative whole number representation."""
    if len(text) == 0:
        return False
    start = 0
    if text[0] == "-":
        start = 1
    if start == len(text):
        return False
    for index in range(start, len(text)):
        if text[index] not in "0123456789":
            return False
    return True

def get_initial_readings():
    """Return the initial simulated device temperature readings list."""
    return [28, 31, 35, 37, 29]

def display_readings(readings):
    """Display every reading currently in the list with its position number."""
    print("\nCURRENT READINGS")
    for index in range(len(readings)):
        print(f"Reading {index + 1}: {readings[index]}°C")

def add_reading(readings):
    """Ask the user for a new reading, validate it, and append if valid."""
    text = input("Enter new reading: ")
    if len(text) == 0:
        print("Invalid input. The reading cannot be empty.")
        return
    
    if not is_whole_number(text):
        print("Invalid input. Enter a whole number only.")
        return
    
    value = int(text)
    if value < 0 or value > 100:
        print("Invalid reading. Enter a value from 0 to 100.")
        return
    
    readings.append(value)
    print("Reading added successfully.")

def classify_reading(value):
    """Return NORMAL, WARNING, or CRITICAL for a single temperature value."""
    if value < 30:
        return "NORMAL"
    elif value <= 35:
        return "WARNING"
    else:
        return "CRITICAL"

def display_classifications(readings): 
    """Classify and display every reading in the list."""
    print("\nREADING CLASSIFICATION")
    for value in readings:
        print(f"{value}°C -> {classify_reading(value)}")

def compute_total(readings):
    """Return the total sum of all temperature readings using a loop."""
    total = 0
    for value in readings:
        total += value
    return total

def compute_average(readings):
    """Return the average temperature computed from the list."""
    if len(readings) == 0:
        return 0.0
    return compute_total(readings) / len(readings)

def find_minimum(readings):
    """Return the minimum temperature using a loop (no min() function)."""
    if len(readings) == 0:
        return None
    minimum = readings[0]
    for value in readings:
        if value < minimum:
            minimum = value
    return minimum

def find_maximum(readings):
    """Return the maximum temperature using a loop (no max() function)."""
    if len(readings) == 0:
        return None
    maximum = readings[0]
    for value in readings:
        if value > maximum:
            maximum = value
    return maximum

def count_category(readings, category_name):
    """Count how many readings fall into a specific category."""
    count = 0
    for value in readings:
        if classify_reading(value) == category_name:
            count += 1
    return count

def determine_overall_status(warning_count, critical_count):
    """Determine the overall monitoring status based on category counts."""
    if critical_count >= 1:
        return "ATTENTION REQUIRED"
    elif warning_count >= 1:
        return "MONITOR"
    else:
        return "NORMAL"

def display_summary(readings):
    """Compute and display numerical summary and overall status."""
    num_readings = len(readings)
    total = compute_total(readings)
    average = compute_average(readings)
    minimum = find_minimum(readings)
    maximum = find_maximum(readings)
    
    normal_count = count_category(readings, "NORMAL")
    warning_count = count_category(readings, "WARNING")
    critical_count = count_category(readings, "CRITICAL")
    
    if num_readings > 0:
        normal_pct = (normal_count / num_readings) * 100
        warning_pct = (warning_count / num_readings) * 100
        critical_pct = (critical_count / num_readings) * 100
    else:
        normal_pct = warning_pct = critical_pct = 0.0

    status = determine_overall_status(warning_count, critical_count)

    print("\nMONITORING SUMMARY")
    print(f"Number of readings: {num_readings}")
    print(f"Total of readings : {total}")
    print(f"Average temperature: {average:.2f}°C")
    print(f"Minimum temperature: {minimum}°C")
    print(f"Maximum temperature: {maximum}°C")
    print(f"NORMAL   : {normal_count} ({normal_pct:.2f}%)")
    print(f"WARNING  : {warning_count} ({warning_pct:.2f}%)")
    print(f"CRITICAL : {critical_count} ({critical_pct:.2f}%)")
    print(f"Overall Status: {status}")

def display_menu():
    """Display the main menu options."""
    print("\nSIMULATED DEVICE MONITORING SYSTEM")
    print("[1] View Readings")
    print("[2] Add Reading")
    print("[3] Classify Readings")
    print("[4] Generate Summary")
    print("[5] Exit")

def main():
    """Control the main program flow and menu loop."""
    readings = get_initial_readings()
    
    while True:
        display_menu()
        choice_text = input("Enter choice: ").strip()
        
        if len(choice_text) == 0:
            print("Invalid choice. Please enter a number from 1 to 5.")
            continue
            
        if not is_whole_number(choice_text):
            print("Invalid choice. Please enter a number from 1 to 5.")
            continue
            
        choice = int(choice_text)
        
        if choice == 1:
            display_readings(readings)
        elif choice == 2:
            add_reading(readings)
        elif choice == 3:
            display_classifications(readings)
        elif choice == 4:
            display_summary(readings)
        elif choice == 5:
            print("Thank you for using the Device Monitoring System.")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")

if __name__ == "__main__":
    main()
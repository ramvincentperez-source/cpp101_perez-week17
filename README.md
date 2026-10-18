# Simulated Device Monitoring and Alert System

**Student Name:** Ram Vincent B Perez\
**Student Number:** 2601285\
**Section:** 1CpE-B

## Project Description

This project is a Python program designed to simulate the monitoring of device temperatures in a Computer Engineering laboratory. It keeps a list of temperature readings, allows users to add new values after checking their validity, and categorizes each reading as NORMAL, WARNING, or CRITICAL. It also provides a statistical summary showing the total, average, lowest and highest temperatures, category counts, percentages, and the overall monitoring status.

## Features

- Displays all recorded temperature readings along with their corresponding numbers.
- Allows users to add new temperature readings while checking that inputs are whole numbers between 0 and 100.
- Identifies the category of each temperature according to the program's defined conditions.
- Calculates the total, average, minimum, and maximum readings, as well as the number and percentage of readings in each category.
- Determines the overall system status based on the number of WARNING and CRITICAL readings.
- Handles invalid menu choices and incorrect inputs by displaying appropriate error messages without stopping the program unexpectedly.

## Requirements

- Python 3
- No additional libraries or external packages required

## How to Run

1. Open a terminal in the Week17 folder.
2. Execute the following command to start the program:

   `python device_monitor.py`

## Sample Output

```
SIMULATED DEVICE MONITORING SYSTEM
[1] View Readings
[2] Add Reading
[3] Classify Readings
[4] Generate Summary
[5] Exit
Enter choice: 1

CURRENT READINGS
Reading 1: 28°C
Reading 2: 31°C
Reading 3: 35°C
Reading 4: 37°C
Reading 5: 29°C
```

## Test Cases

I conducted a total of 10 test cases to check whether the program functions correctly. All 10 tests passed, and none failed. The complete test results are documented in `test_cases.md`.

## Known Limitations

- The temperature readings are stored temporarily and will return to their initial values when the program is restarted.
- The program accepts whole numbers only. Decimal values and other invalid formats are not accepted.

## Reflection

There are times when I question why I chose Computer Engineering because I find the course challenging. As a first-year CpE student, I hope to continue learning, improve my abilities, and become more confident. It has only been one semester, but I still find it difficult to keep up with the lessons. i always find questioning my self if i can do this, if i can continiue, do i have what it takes to be a computer engineer.

Despite these difficulties, working on this project helped me. I learned how to use loops, conditional statements, functions, and input validation to create a working program. 

Overall, this project was challenging, especially when I had to combine several concepts and make sure that each part worked correctly. As a first-year student completing this task during finals week, I sometimes felt overwhelmed while working with loops, validation, and boundary conditions. However, reviewing the lesson modules and solving the problems step by step helped me understand the program better. I did my best to complete this project, and I hope to practice more, strengthen my coding skills, and eventually create future programs independently without always relying on assistance.

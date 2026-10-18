# test_cases.md -- Simulated Device Monitoring and Alert System

Tested by: Ram Vincent B Perez\
Date: October 18, 2026

| Test Case | Input or Action         | Expected Result                                                 | Actual Result                                                                         | Pass/Fail |
| --------- | ----------------------- | --------------------------------------------------------------- | ------------------------------------------------------------------------------------- | --------- |
| TC01      | Choose 1                | Five readings displayed: 28, 31, 35, 37, 29                     | All five readings appeared correctly on the screen                                    | Pass      |
| TC02      | Choose 2, enter 33      | "Reading added successfully."                                   | The system confirmed that the reading was added successfully                          | Pass      |
| TC03      | Choose 2, enter abc     | Rejected; list unchanged                                        | The input was rejected, and the system requested a whole number                       | Pass      |
| TC04      | Choose 2, enter -5      | Rejected; list unchanged                                        | The system rejected the input and requested a value from 0 to 100                     | Pass      |
| TC05      | Choose 2, enter 120     | Rejected; list unchanged                                        | The system rejected the input and requested a value from 0 to 100                     | Pass      |
| TC06      | Add 30, then choose 3   | 30°C classified as WARNING                                      | The 30°C reading was identified as WARNING                                            | Pass      |
| TC07      | Choose 3                | 35°C classified as WARNING                                      | The 35°C reading was identified as WARNING                                            | Pass      |
| TC08      | Choose 4 (initial data) | Total 160, Avg 32.00, Min 28, Max 37, Status ATTENTION REQUIRED | The total, average, minimum, maximum, and overall status matched the expected results | Pass      |
| TC09      | Enter 9                 | Error message; menu shown again                                 | The system displayed an invalid-choice message and returned to the menu               | Pass      |
| TC10      | Choose 5                | Exit message; program ends                                      | The system displayed a closing message and terminated properly                        | Pass      |

## Bugs Found and Fixed

- During initial testing of boundary condition evaluation (30 and 35), value comparisons initially used strict inequalities (< instead of <=), which incorrectly classified 30 as "NORMAL" and 35 as "NORMAL" or "CRITICAL". This was resolved by updating "classify_reading()" to include inclusive comparison operators (<= 35), ensuring that both 30°C and 35°C correctly evaluate to "WARNING".

Clarify the test-case numbering and inputsAdd a concise overall test summary
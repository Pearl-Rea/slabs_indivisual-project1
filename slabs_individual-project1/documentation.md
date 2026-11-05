# Documentation - Grade Evaluation System

## How it Works
1. User enters Practical Assessment mark (0-100)
2. User enters Theory Examination mark (0-100)
3. Program calculates: final = (practical * 0.40) + (theory * 0.60)
4. If final >= 50, student PASSES, else FAILS

## Edge Cases and Error Handling

### 1. Non-numeric input
- Example: user types "abc" or "eighty" or "80 60"
- Handling: Python raises ValueError, caught with try/except
- Output: "Error: Please enter a numeric value only."

### 2. Out-of-range input
- Example: -5 or 150
- Handling: Check if 0 <= mark <= 100, if not, stop and show error
- Output: "Error: Practical mark must be between 0 and 100."
- Output: "Error: Theory mark must be between 0 and 100."

### 3. Boundary values
- 0 and 100 are valid and accepted
- 50 is PASS, 49.99 is FAIL
- Tested: 80 and 60 -> 68.00% -> PASS

### 4. Empty input
- Example: user just presses Enter
- Handling: Treated as non-numeric, shows numeric error

## Test Cases
| Practical | Theory | Final | Status |
| --- | --- | --- | --- |
| 80 | 60 | 68.00% | PASS |
| 100 | 100 | 100.00% | PASS |
| 0 | 0 | 0.00% | FAIL |
| 50 | 50 | 50.00% | PASS |
| 101 | 50 | Error | Out of range |
| abc | 50 | Error | Non-numeric |

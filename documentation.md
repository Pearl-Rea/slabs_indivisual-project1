# Edge Case & Error Analysis - Grade Checker

## 1. Invalid Input: Text like "abc"

**what happens:**
User types "abc" when asked for a mark.

**Error Type: Runtime Errors**
Specifically a ValueError in Python. The program complies fine (no Syntax error), but crashes at runtime because int("abc") cannot convert text to a number.

**How we prevent it:**
We use try / except ValueError around the input.
If conversation fails, we display a friendly error message instead of crashing.
This is called type casting with exception hamdling.

## 2. Invalid Input: Out-of-range number like 150

**What happens:**
User types 150. Python accepts it as a number, so no crash occurs.


**Error Type: Semantic / Logic Error**
The program runs, but the result is meaningless. A mark cannot be > 100.
If we did not check, the final mark would be wrong and a student could PASS incorrectly.


**How we prevent it:**
We use explicit range validation:
if not (0 <= mark <=100):
If out of range, we stop and show an error. This prevents incorrect logic.


## Conclusion

Type casting with int() combined with explicit range validation prevents system crashes (Runtime errors) and incorrect logic (Semantic errors).
The program fails safely with a clear message instead of crashing or producing a wrong PASS/FAIL result.

# Python Function Error: Handling Empty Lists and Non-Numeric Input

This repository demonstrates a common error in Python: forgetting to handle potential exceptions or invalid input when working with functions.  Specifically, the `calculate_average` function in `bug.py` fails if provided an empty list or a list containing non-numeric elements. The solution in `bugSolution.py` addresses these issues with robust error handling and input validation.

**Error:** A `TypeError` occurs when attempting to calculate the average of a list containing a mix of numbers and strings.

**Solution:**  The solution incorporates a `try-except` block to handle the `TypeError` and input validation to ensure that only numeric values are processed.
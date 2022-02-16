# <COE 332 Homework 3>

Luke Wilson
lew2547
2/17/2022

# Contents

- analyze_water.py
- test_analyze_water.py

# analyzt_water.py

This script contains the functions necessary to calculate turbidity levels of the water, assess water safety and compute time needed for water to return to safe levels. 
The two functions are:
	- compute_turbidity
	- check_turbidity_safety

# test_analyze_water.py

This script is build to operate with pytest. It tests the functions declared in analyze_water.py, by feeding them dummy arguments. we also test for exceptions and argument errors.
The four functions used are:
	- test_compute_turbidity
	- test_compute_turbidity_exceptions
	- test_check_turbidity_safety
	- test_check_turbidity_safety_exceptions


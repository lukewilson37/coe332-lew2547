# Water Turbidity Analysis and Pytest

## COE 332 Homework 3

Luke Wilson
lew2547
2/17/2022

## Description

For this homework, we seek to apply our newfound pytest skills to a water turbidity analysis script. Pytest is a python/terminal package that allows us to test and debug a script. For any analysis, the script may run, but is it producing true results? We can check this with pytest. With Pytest we will feed teh script dummy data and ensure the script produces the correct data, does not throw unexpected errors and throws errors when data input is invalid.

## Contents

- analyze_water.py
- test_analyze_water.py

### analyzt_water.py

This script contains the functions necessary to calculate turbidity levels of the water, assess water safety and compute time needed for water to return to safe levels. 
The two functions are:
	- compute_turbidity
	- check_turbidity_safety

### test_analyze_water.py

This script is build to operate with pytest. It tests the functions declared in analyze_water.py, by feeding them dummy arguments. we also test for exceptions and argument errors.
The four functions used are:
	- test_compute_turbidity
	- test_compute_turbidity_exceptions
	- test_check_turbidity_safety
	- test_check_turbidity_safety_exceptions

## Running the Code




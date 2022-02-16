import json
import math
import logging

d = 0.02		# decay factor
Ts = 1 			# Turbidity Threshold


def compute_turbidity(list_data: list) -> float:
	"""	Computes Turbidity level from a list of dictionaries
	
	This function calculated the turbidity level of water. The equation used for turbidity is
		T = a0 * I90
	where a0 is the calibration constant and I90 i the ninety degree detector current. T is 
	is NTI units (0-40). a0 and I90 are variable for each sample and are key elements passed through
	the argument. The function will return the average turbidity of the last 5 samples as an indication 
	of water quality.

	Args:
		list_data: list of dictionaries. Each dictionary must have 'calibration_constant' and 
			'detector_current' key key paired with a number (integeer or float)

	Returns:
		A float which represents the average 5 turbidity values in the dictionary

	Raises:
		KeyError: if 'calibration_canstant' or 'detector_current' kays are not present in dictionary
		TypeError: if 'calibration_constant' or 'detector_current' are not paired with floats
		IndexError: if list contains less than 5 dictionaries		

	"""

	current_turbidity = 0

	for i in range(-5,0):
		current_turbidity += list_data[i]['calibration_constant'] * list_data[i]['detector_current']


	current_turbidity = current_turbidity / 5

	return current_turbidity

def turbidity_safety_check(list_data: list) -> float:
	""" Checks the current turbidity level to assess safety as well as computing minimum time to safe turbidity levels

	This function accepts a list of dictionaries with same constaints as in calculate_turbidity. 
	It checks if turbidity is above or below threshold and calculates minimum time needed to return to safe levels.
	As it does this, it prints info regarding the turbidity level, turbidity safety and time to safe turbidity levels.
	The function also relies on global vaviables Ts, turbidity threshold, and d, decay factor.
	
	Args:
		list_data: list of dictionaries. Each dictionary must have 'calibration_constant' and 
			'detector_current' key key paired with a number (integeer or float)

	Returns:
		A float which represents the minimum time needed to return to safe turbidity levels

	Raises:
		KeyError: if 'calibration_canstant' or 'detector_current' kays are not present in dictionary
		TypeError: if 'calibration_constant' or 'detector_current' are not paired with floats
		IndexError: if list contains less than 5 dictionaries		

	"""
	
	T0 = compute_turbidity(list_data)

	logging.info('Average turbidity based on most recent five measurments = '+ str(round(T0,4)) + ' NTU')


	if (T0 < 1):
		logging.info('Info: Turbidity is below threshold for safe use')
		logging.info('Minimum time required to return below a safe threshold = '+str(round(0,2))+' hours')
		b = 0
	else:
		logging.warning('Warning: Turbidity is above threshold for safe use')	
		b = math.log(Ts/T0) / math.log( 1-d )
		logging.warning('Minimum time required to return below a safe threshold = '+str(round(b,2))+' hours')
		

	return b

def main():

	with open('turbidity_data.json', 'r') as f:
		water_json = json.load(f)

	water_data = water_json['turbidity_data']

	compute_turbidity(water_data)

	turbidity_safety_check(water_data)
		
	
if (__name__ == '__main__'):
	main()



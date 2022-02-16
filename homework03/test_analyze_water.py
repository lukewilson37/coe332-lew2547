import pytest
import math

from analyze_water import compute_turbidity
from analyze_water import turbidity_safety_check

def test_compute_turbidity():

	list = [{
				'calibration_constant':1,
				'detector_current':1
			},{
				'calibration_constant':1,
				'detector_current':1
			},{
				'calibration_constant':1,
				'detector_current':1
			},{
				'calibration_constant':1,
				'detector_current':1
			},{
				'calibration_constant':1,
				'detector_current':1
			},{
				'calibration_constant':1,
				'detector_current':1
			}
			]

	assert(compute_turbidity(list) == 1)

	list.append({'calibration_constant':1,'detector_current':21})

	assert(compute_turbidity(list) == 5)

	list.append({'calibration_constant':0,'detector_current':10})

	assert(compute_turbidity(list) != 5)

	list. append({'calibration_constant':-1,'detector_current':23})

	assert(compute_turbidity(list) == 0)

def test_compute_turbidity_exceptions():

	list = [{
				'calibration_constant':1,
				'detector_current':1
			},{
				'calibration_constant':1,
				'detector_current':1
			},{
				'calibration_constant':1,
				'detector_current':1
			},{
				'calibration_constant':1,
				'detector_current':1
			},{
				'calibration_constant':1,
				'detector_current':1
			},{
				'calibration_constant':1,
				'detector_current':1
			}
			]

	list.append({'turbidity':100})

	with pytest.raises(KeyError):
		compute_turbidity(list)

	list.remove({'turbidity':100})

	list.append({'calibration_constant':'zero','detector_current':'one'})

	with pytest.raises(TypeError):
		compute_turbidity(list)

	list = [{
				'calibration_constant':1,
				'detector_current':1
			}]

	with pytest.raises(IndexError):
		compute_turbidity(list)

 

def test_turbidity_safety_check():

	list = [{
				'calibration_constant':1,
				'detector_current':1
			},{
				'calibration_constant':1,
				'detector_current':1
			},{
				'calibration_constant':1,
				'detector_current':1
			},{
				'calibration_constant':1,
				'detector_current':1
			},{
				'calibration_constant':1,
				'detector_current':1
			},{
				'calibration_constant':1,
				'detector_current':1
			}
			]

	assert(turbidity_safety_check(list) == 0)

	list.append({'calibration_constant':1,'detector_current':21})

	assert(turbidity_safety_check(list) != 0)

	assert(round(turbidity_safety_check(list),2) == round(math.log(1/5)/math.log(1-.02),2))

	list. append({'calibration_constant':-1,'detector_current':30})

	assert(turbidity_safety_check(list) == 0)


def test_turbidity_safety_check_exceptions():

	list = [{
				'calibration_constant':1,
				'detector_current':1
			},{
				'calibration_constant':1,
				'detector_current':1
			},{
				'calibration_constant':1,
				'detector_current':1
			},{
				'calibration_constant':1,
				'detector_current':1
			},{
				'calibration_constant':1,
				'detector_current':1
			},{
				'calibration_constant':1,
				'detector_current':1
			}
			]

	list.append({'turbidity':100})

	with pytest.raises(KeyError):
		turbidity_safety_check(list)

	list.remove({'turbidity':100})

	list.append({'calibration_constant':'zero','detector_current':'one'})

	with pytest.raises(TypeError):
		turbidity_safety_check(list)

	list = [{
				'calibration_constant':1,
				'detector_current':1
			}]

	with pytest.raises(IndexError):
		turbidity_safety_check(list)



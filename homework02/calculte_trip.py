import json
import math

mars_radius = 3389.5 

def main():

	file = "sites.json"

	with open(file,'r') as f:
		sites_dict = json.load(f)
	sites_list = sites_dict['sites']

	time_elapsed = 0.0

	robot_lat = 16
	robot_lon = 82
	robot_kph = 10

	for i in range(len(sites_list)):
		
		travel_time = calc_gcd(sites_list[i]['latitude'],sites_list[i]['longitude'],robot_lat,robot_lon) / robot_kph
		robot_lat = sites_list[i]['latitude']
		robot_lon = sites_list[i]['longitude']

		if sites_list[i]['composition'] == 'stony':
			sample_time = 1
		elif sites_list[i]['composition'] == 'iron':
			sample_time = 2
		elif sites_list[i]['composition'] == 'stony-iron':
			sample_time = 3

		time_elapsed += (travel_time + sample_time)

		print("leg = ",i,", time to travel =",travel_time," hr, time to sample = ",sample_time," hr")
		
	print("number of legs = ",i,", total time elapsed = ",round(time_elapsed,2)," hr")


def calc_gcd(latitude_1: float, longitude_1: float, latitude_2: float, longitude_2: float) -> float:
    lat1, lon1, lat2, lon2 = map( math.radians, [latitude_1, longitude_1, latitude_2, longitude_2] )
    d_sigma = math.acos( math.sin(lat1) * math.sin(lat2) + math.cos(lat1) * math.cos(lat2) * math.cos(abs(lon1-lon2)))
    return ( mars_radius * d_sigma )

if __name__ == "__main__":
	main()

import json
import random

def main():

	types = ["iron","stony","stony-iron"]

	n = 5

	lat0 = 16.0
	lat1 = 18.0

	lon0 = 82.0
	lon1 = 84.0

	site_dict = {"sites":generate_sites(n,lat0,lat1,lon0,lon1,types)}

	with open('sites.json','w') as out:
		json.dump(site_dict,out,indent=2)



def generate_sites(n,lat0,lat1,lon0,lon1,comps):

	site_list = []

	for i in range(n):

		site = {
				"side_id": i, 
				"latitude": lat0 + random.random()*(lat1-lat0),
				"longitude":lon0 + random.random()*(lon1-lon0),
				"composition": random.choice(comps)
				}

		site_list.append(site)


	return site_list


if __name__ == "__main__":
	main()


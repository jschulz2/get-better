import json
import requests
import pandas as pd

def call_data():
	url = "https://datausa.io/api/data?drilldowns=Nation&measures=Population"
	response = requests.get(url)
	data = response.json()
	print(response.status_code)
	print(data)
	return data

#def place_data_in_dataframe()

def main():
	one = call_data()

if __name__ == "__main__":
	main()
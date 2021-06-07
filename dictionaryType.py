gojek_driver_data = {
    'date': '2021-06-08',
    'driver_nearby': [
        {'name': 'eko', 'distance': 10}, {'name': 'michael', 'distance': 40}, {'name': 'gerald', 'distance': 100}
    ]
}

print('\nData from gojek server :')
print(gojek_driver_data)

print('\nNearest driver')
print(f"name : {gojek_driver_data['driver_nearby'][0]['name']} dengan jarak {gojek_driver_data['driver_nearby'][0]['distance']} meters")

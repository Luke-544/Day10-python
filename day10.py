#sets in python - collection of things which are unordered,unindexed. No duplicate values\

cars = {"BMW","Mazda","Audi"}
Bikes = {"Yamaha","RTR","Kawasaki","BMW"}

cars.add("Lamborghini")
cars.remove("BMW")
cars.clear()
cars.update(Bikes)
motors = cars.union(Bikes)

for x in cars:
    print(x)

print(Bikes.difference(cars)) #what one set has that's not in another set
print(cars.intersection(Bikes)) #what is common between the two sets

#Dictionary
capitals = {'USA': 'Washington DC',
            'India': 'New Delhi'}
print(capitals['India'])
print(capitals.get('Kenya'))
print(capitals.keys())
print(capitals.values())
print(capitals.items())
capitals.update({'Kenya':'Nairobi'}) #you can use it add a new key and value
capitals.update({'USA':'Nairobi'}) #you can use it to alter an existing key and value
capitals.pop('India')
capitals.clear

for key,value in capitals.items():
    print(key,value)
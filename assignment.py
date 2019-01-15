import json

#Part 1
# station code for Seattle is GHCND:US1WAKG0038
#creating a new dictionary with the Seattle date using the station code

Seattle = []
with open('precipitation.json', 'r') as file:
    station_dictionary = json.load(file)
    for line in station_dictionary:
        if line['station']=='GHCND:US1WAKG0038':
            Seattle.append(line)
    
# Clean the Dictionary from the datatype and station
for line in Seattle:
    del[line['datatype']],
    del[line['station']]


#get just months and values in the Seattle dictionary

for line in Seattle:
    line['year'], line['month'], line['day'] = line['date'].split("-")
    del[line['year']],
    del[line['date']],
    del[line['day']]
# create a new list that is going to have values averages and months as indexes
final_list = [0,0,0,0,0,0,0,0,0,0,0,0]
for line in Seattle:
    month = int(line['month']) 
    final_list[month-1] = line['value'] +  final_list[month-1]
print(final_list)











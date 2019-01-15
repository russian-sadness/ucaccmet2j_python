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
final_list = [0]*12
for line in Seattle:
    month = int(line['month']) 
    final_list[month-1] = line['value'] +  final_list[month-1]
#print(final_list)

import json
with open('Seattle_months.json', 'w') as file: 
    json.dump(final_list, file , indent=4 , sort_keys = True ) 

#Part 2
#Calculate the sum of the precipitation over the whole year., we use the final_list which has the precipations per month 
total_precipitation = int(sum(final_list))
print('The total precipation is: ' + str(total_precipitation))

# Calculate the relative precipitation per month (percentage compared to the precipitation over the whole year)
# We have to devide each value in the final_list by the total and multiply by 100 (and we loop it around the final_list)
relative_precipitation= [100*i/total_precipitation for i in final_list]
print(relative_precipitation)

import json
with open('total_precipitation.json', 'w') as file: 
    json.dump(total_precipitation, file , indent=4 , sort_keys = True ) 
import json
with open('relative_precipitation.json', 'w') as file: 
    json.dump(relative_precipitation, file , indent=4 , sort_keys = True ) 
#Part 3
#Rewrite your code so that it calculates all the above for each location














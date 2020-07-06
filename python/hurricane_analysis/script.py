# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day',
         'New England','Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen',
         'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix',
         'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September',
          'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August',
          'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September',
          'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979,
         1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175,
                       190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'],
                  ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'],
                  ['The Bahamas', 'Northeastern United States'],
                  ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'],
                  ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'],
                  ['Jamaica', 'Yucatn Peninsula'],
                  ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'],
                  ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'],
                  ['Bermuda', 'New England', 'Atlantic Canada'],
                  ['Lesser Antilles', 'Central America'],
                  ['Texas', 'Louisiana', 'Midwestern United States'],
                  ['Central America'],
                  ['The Caribbean', 'Mexico', 'Texas'],
                  ['Cuba', 'United States Gulf Coast'],
                  ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'],
                  ['Mexico'],
                  ['The Caribbean', 'United States East coast'],
                  ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'],
                  ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'],
                  ['The Caribbean', 'United States East Coast'],
                  ['The Bahamas', 'Florida', 'United States Gulf Coast'],
                  ['Central America', 'Yucatn Peninsula', 'South Florida'],
                  ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'],
                  ['The Caribbean', 'Venezuela', 'United States Gulf Coast'],
                  ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'],
                  ['Bahamas', 'United States Gulf Coast'],
                  ['Cuba', 'United States Gulf Coast'],
                  ['Greater Antilles', 'Central America', 'Florida'],
                  ['The Caribbean', 'Central America'],
                  ['Nicaragua', 'Honduras'],
                  ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'],
                  ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'],
                  ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'],
                  ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M',
           '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B',
           '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

# write your update damages function here:
def update_damages(list_damages):
    new_damages = []

    for damage in list_damages:
        if damage == "Damages not recorded":
            new_damages.append(damage)
        elif damage[-1] == "M":
            new_damage = float(damage[:len(damage)-1]) * 1000000.0
            new_damages.append(new_damage)
        else:
            new_damage = float(damage[:len(damage)-1]) * 1000000000.0
            new_damages.append(new_damage)

    return new_damages

new_damages = update_damages(damages)
print()
print(new_damages)
print()

# write your construct hurricane dictionary function here:
def hurricane_dictionary(names, months, years, max_sustained_winds, areas_affected, damages, deaths):
    dictionary = {}
    i = 0

    for name in names:
        dictionary[name] = {
            'Name':names[i],
            'Month':months[i],
            'Year':years[i],
            'Max Sustained Wind':max_sustained_winds[i],
            'Areas Affected':areas_affected[i],
            'Damage':damages[i],
            'Deaths':deaths[i]
        }
        i+=1

    return dictionary

main_dict = hurricane_dictionary(names, months, years, max_sustained_winds, areas_affected, new_damages, deaths)
print(main_dict['Cuba I'])
print()

# write your construct hurricane by year dictionary function here:
def years_dictionary(main_dict):
    new_dict = {}
    for hurricane in main_dict:
        current_year = main_dict[hurricane]['Year']
        if current_year in new_dict:
            new_dict[current_year].append(main_dict[hurricane])
        else:
            new_dict[current_year] = [main_dict[hurricane]]

    return new_dict

years_dict = years_dictionary(main_dict)
print(years_dict[1932])
print()

# write your count affected areas function here:
def areas_dictionary(main_dict):
    new_dict = {}

    for hurricane in main_dict:
        current_area = main_dict[hurricane]['Areas Affected']
        for area in current_area:
            if area in new_dict:
                new_dict[area] += 1
            else:
                new_dict[area] = 1

    return new_dict

areas_dict = areas_dictionary(main_dict)
print(areas_dict)
print()

# write your find most affected area function here:
def most_affected_area(areas_dict):
    max_times = 0
    affected_area = ""

    for area in areas_dict:
        if max_times < areas_dict[area]:
            max_times = areas_dict[area]
            affected_area = area

    return affected_area, max_times

most_affect_area = most_affected_area(areas_dict)
print('The most affected area is: ' + str(most_affect_area[0] + ', with ' + str(most_affect_area[1]) + ' huricanes attacks.'))
print()

# write your greatest number of deaths function here:
def most_deaths(main_dict):
    max_deaths = 0
    hurricane_name = ""

    for hurricane in main_dict:
        if max_deaths < main_dict[hurricane]['Deaths']:
            max_deaths = main_dict[hurricane]['Deaths']
            hurricane_name = main_dict[hurricane]['Name']

    return hurricane_name, max_deaths

most_deaths_hurricane = most_deaths(main_dict)
print('The greatest number of deaths was on ' + str(most_deaths_hurricane[0]) + ', with ' + str(most_deaths_hurricane[1]) + ' deaths.')
print()

# write your categorize by mortality function here:
mortality_scale = {0: 0,
                   1: 100,
                   2: 500,
                   3: 1000,
                   4: 10000}

def mortality_scale_dictionary(main_dict):
    new_dict = {0:[], 1:[], 2:[], 3:[], 4:[], 5:[]}

    for hurricane in main_dict:
        if main_dict[hurricane]['Deaths'] > 10000:
            new_dict[5].append(main_dict[hurricane])
        elif main_dict[hurricane]['Deaths'] > 1000:
            new_dict[4].append(main_dict[hurricane])
        elif main_dict[hurricane]['Deaths'] > 500:
            new_dict[3].append(main_dict[hurricane])
        elif main_dict[hurricane]['Deaths'] > 100:
            new_dict[2].append(main_dict[hurricane])
        elif main_dict[hurricane]['Deaths'] > 0:
            new_dict[1].append(main_dict[hurricane])
        else:
            new_dict[0].append(main_dict[hurricane])

    return new_dict

mortality_scale_dict = mortality_scale_dictionary(main_dict)
print('### MORTALITY SCALE ###')
for scale in mortality_scale_dict:
    print(str(scale) + ':')
    for dict in mortality_scale_dict[scale]:
        print(dict)
print()

# write your greatest damage function here:
def greatest_damage(main_dict):
    max_damage = 0
    hurricane_name = ""

    for hurricane in main_dict:
        if type(main_dict[hurricane]['Damage']) == str:
            continue
        else:
            if max_damage < main_dict[hurricane]['Damage']:
                max_damage = main_dict[hurricane]['Damage']
                hurricane_name = main_dict[hurricane]['Name']

    return hurricane_name, max_damage

max_damage_hurricane = greatest_damage(main_dict)
print('The greatest damage was on ' + str(max_damage_hurricane[0]) + ', with $' + str(max_damage_hurricane[1]))
print()

# write your catgeorize by damage function here:
damage_scale = {0: 0,
                1: 100000000,
                2: 1000000000,
                3: 10000000000,
                4: 50000000000}

def damage_scale_dictionary(main_dict):
    new_dict = {0:[], 1:[], 2:[], 3:[], 4:[], 5:[]}

    for hurricane in main_dict:
        if type(main_dict[hurricane]['Damage']) == str:
            continue
        elif main_dict[hurricane]['Damage'] > 50000000000:
            new_dict[5].append(main_dict[hurricane])
        elif main_dict[hurricane]['Damage'] > 10000000000:
            new_dict[4].append(main_dict[hurricane])
        elif main_dict[hurricane]['Damage'] > 1000000000:
            new_dict[3].append(main_dict[hurricane])
        elif main_dict[hurricane]['Damage'] > 100000000:
            new_dict[2].append(main_dict[hurricane])
        elif main_dict[hurricane]['Damage'] > 0:
            new_dict[1].append(main_dict[hurricane])
        else:
            new_dict[0].append(main_dict[hurricane])

    return new_dict

damage_scale_dict = damage_scale_dictionary(main_dict)
print('### DAMAGE SCALE ###')
for scale in damage_scale_dict:
    print(str(scale) + ':')
    for dict in damage_scale_dict[scale]:
        print(dict)
print()
from datetime import datetime
import colours
import add_spaces_to_nb as astn

ages = {
'Florence': datetime(1943, 9, 8),
'Jean Pierre': datetime(1943, 11, 23),
'Oivia': datetime(1979, 4, 24),
'Olivier': datetime(1980, 5, 30),
'Timothee': datetime(2011, 5, 16),
'Gautier': datetime(2016, 10, 12),
'Coralie': datetime(1973, 5, 21),
'Nicolas': datetime(1973, 10, 7),
'Meldan': datetime(2004, 10, 13),
'Elana': datetime(2007, 4, 11),
'Anaia': datetime(2011, 2, 24),
'Sebastien': datetime(1975, 3, 22),
'Nelly': datetime(1979, 1, 12),
'Eliot': datetime(2014, 1, 18),
'Aelys': datetime(2017, 6, 28),
'Odile': datetime(1953, 2, 2),
'Valerie': datetime(1987, 5, 6),
}


names = {
'flo': 'Florence',
'ba': 'Jean Pierre',
'ma': 'Oivia',
'pa': 'Olivier',
'tim': 'Timothee',
'gau': 'Gautier',
'coc': 'Coralie',
'nic': 'Nicolas',
'mel': 'Meldan',
'ela': 'Elana',
'ana': 'Anaia',
'seb': 'Sebastien',
'nel': 'Nelly',
'eli': 'Eliot',
'ael': 'Aelys',
'odi': 'Odile',
'val': 'Valerie',
}

groups = {
'all': ['Florence', 'Jean Pierre', 'Oivia', 'Olivier', 'Timothee', 'Gautier', 'Coralie', 'Nicolas', 'Meldan', 'Elana', 'Anaia', 'Sebastien', 'Nelly', 'Eliot', 'Aelys', 'Odile', 'Valerie',], 
'pfranses': ['Oivia', 'Olivier', 'Timothee', 'Gautier'],
'gfranses': ['Oivia', 'Olivier', 'Timothee', 'Gautier', 'Odile', 'Valerie'],
'gpg': ['Florence', 'Jean Pierre'],
'gpf': ['Odile', 'Valerie'],
'recorbets': ['Coralie', 'Nicolas', 'Meldan', 'Elana', 'Anaia'],
'gravelles': ['Sebastien', 'Nelly', 'Eliot', 'Aelys'],
'goutails': ['Florence', 'Jean Pierre', 'Oivia', 'Olivier', 'Timothee', 'Gautier', 'Coralie', 'Nicolas', 'Meldan', 'Elana', 'Anaia', 'Sebastien', 'Nelly', 'Eliot', 'Aelys'],
'cousins': ['Timothee', 'Gautier', 'Meldan', 'Elana', 'Anaia', 'Eliot', 'Aelys'],
}


# Step 1: Get the current date
current_date = datetime.now()

# Step 2: Define the given date (format: YYYY, MM, DD)
given_date = datetime(2011, 5, 16)

# Step 3: Calculate the difference between dates
date_difference = current_date - given_date

# Step 4: Get the number of days
days_difference = date_difference.days

#print(f"Current Date: {current_date.strftime('%Y-%m-%d')}")
#print(f"Given Date: {given_date.strftime('%Y-%m-%d')}")
#print(f"Days between: {days_difference} days")




# set up ages
now = datetime.now()
for x, y in ages.items():
    y = now - y
    y = y.days
    ages.update({x: y})

for group in groups:
    print(colours.dark.CYAN + group + colours.END)

while True:
    # ask people
    people = input('Quelle personnes/groupes? ').lower()
        
    # retrieve each person
    if ',' in people:
        people = people.split(',')
    else:
        people = [people]

    totalpeople = []
    for person in people:
        if person in names:
            totalpeople.append(names[person])
        elif person in groups:
            for pp in groups[person]:
                totalpeople.append(pp)
        else:
            print(f"ERROR: '{person}' introuvable")
            break

    # get everyone's age
    totalages = []
    for person in totalpeople:
        totalages.append(ages[person])

    # get total age
    totalage = 0
    for age in totalages:
        totalage += age

    # print total age
    totalpeoplestring = ", ".join(totalpeople)
    print(totalpeoplestring + colours.BOLD + ' ont ' + colours.dark.RED + astn.run(totalage) + colours.END + colours.BOLD + ' jours' + colours.END)

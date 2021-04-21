contact_file = open ("contacts.txt", "r")

liam = contact_file.readline().split()

people = {}
people[1] = {}

people[1]['Name'] = liam[0]
people[1]['Phone'] = liam[1]
people[1]['Email'] = liam[2]


noah = contact_file.readline().split()   

people[2] = {}

people[2]['Name'] = noah[0]
people[2]['Phone'] = noah[1]
people[2]['Email'] = noah[2]

tony = contact_file.readline().split()   

people[3] = {}

people[3]['Name'] = tony[0]
people[3]['Phone'] = tony[1]
people[3]['Email'] = tony[2]


bert = contact_file.readline().split()   

people[4] = {}

people[4]['Name'] = bert[0]
people[4]['Phone'] = bert[1]
people[4]['Email'] = bert[2]


contact_file.close()


names = input ("Enter Name: ")


if names == people[1]['Name']:
    print (people[1])
elif names == people[2]['Name']:
    print (people[2])
elif names == people[3]['Name']:
    print (people[3])
elif names == people[4]['Name']:
    print (people[4])
else:
    print("No contact with that name")
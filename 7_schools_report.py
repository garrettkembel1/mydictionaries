"""
Process the JSON file named school_data.json. Display only those schools 
that are part of the ACC, Big 12, Big Ten, and SEC divisons.

Copy that info here:

"NCAA/NAIA conference number football (IC2020)","372","American Athletic Conference"
"NCAA/NAIA conference number football (IC2020)","108","Big Twelve Conference"
"NCAA/NAIA conference number football (IC2020)","107","Big Ten Conference"
"NCAA/NAIA conference number football (IC2020)","130","Southeastern Conference"


Display report for all universities that have a graduation rate for Women over 75%
Display report for all universities that have a total price for in-state students living off campus over $50,000



"""
#list_of_schools = json.load(infile)

#print(type(list_of_schools))

#list_of_conferences = [372,108,107,130]

#import json


#infile = open('school_data.json', 'r')

import json

infile = open('school_data.json', 'r')

school_data = json.load(infile)

list_of_conferences = [372, 108, 107, 130]

print("Universities with a graduation rate for Women over 75%:")
for school in school_data:
    if school.get("NCAA", {}).get("NAIA conference number football (IC2020)") in list_of_conferences and school.get("Graduation rate  women (DRVGR2020)") is not None and school.get("Graduation rate  women (DRVGR2020)") > 75:
        print('\n')
        print(f'University: {school["instnm"]}')
        print(f'Graduation Rate for Women: {school["Graduation rate  women (DRVGR2020)"]}%')

print("\nUniversities with a total price for in-state students living off campus over $50,000:")
for school in school_data:
    if school.get("NCAA", {}).get("NAIA conference number football (IC2020)") in list_of_conferences and school.get("Total price for in-state students living off campus (not with family)  2020-21 (DRVIC2020)") is not None and school.get("Total price for in-state students living off campus (not with family)  2020-21 (DRVIC2020)") > 50000:
        print('\n')
        print(f'University: {school["instnm"]}')
        print(f'Total price for in-state students living off campus: ${school["Total price for in-state students living off campus (not with family)  2020-21 (DRVIC2020)"]}')


infile.close()

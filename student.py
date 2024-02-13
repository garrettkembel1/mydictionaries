student = {}
student["name"] =  "Garrett Kembel"
student ["age"]=  22
student ["major 1"]=  "Supply Chain Management"
student ["major 2"]= "Management Information Systems"
student ["hobbies"]= ["Music", "Lego", "Sports", "Gym"]
student ["state"]=  "Texas"

student ["age"] += 1

for i in student ['hobbies']:
    print(i)

for k, v in student.items():
    print (f" {k}: {v}")

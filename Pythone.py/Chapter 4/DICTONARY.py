info = {
    "Name" : "Faheem",
    "cgpa" : 3.43,
    "Department" : "Electrical",
    "SUbjects" : ["DSA", "EDC", "DLD", "AI", "MVC"] 
}
#print(info)
#info["Name"] = "ALi"
#print(info)
#info["Surname"] = "Sajid Hussain Shah"
#print(info)
#print(info.keys())
#print(list(info.keys()))
#print(len(info))
#print(list(info.values()))
#list1 =list(info.items())
#print(list1[0])
#print(info.get("Department"))
#info.update({"City" : "Sargodha"})
#print(info)
new_Dict = {"City" : "Sargodha"}
info.update(new_Dict)
print(info)
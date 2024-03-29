import json
    
website = "Website"
username = "Username"
password = "Password"
# Note! json format. 
new_data = {
    website:{
        "email": username,
        "password": password,
    },
}
newer_data = {
    "website2": {
        "email": "username2",
        "password": "password2",
    },
}


with open("json_file.json", "w") as data_file:
    json.dump(new_data, data_file, indent=4)
    
with open("json_file.json", "r") as data_file:
    #Reading old data
    
    data = dict(json.load(data_file))
    print(type(data))
    print(data)
    #Update old data
    data.update(newer_data)
with open("json_file.json", "w") as data_file:
    # Save updated data
    json.dump(data, data_file, indent=4)

   

    
        
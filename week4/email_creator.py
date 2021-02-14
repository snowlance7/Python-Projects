print("Email Creator\n")

with open("email_creator_contacts.txt") as f1:
    for line in f1:
        print("==========================================================")
        contact = line.split(",")
        contact[2] = contact[2].rstrip("\n").lower()
        contact[0] = contact[0].title()
        
        with open("email_creator_template.txt") as f2:
            template = f2.read()
            template = template.replace("{email}",contact[2]).replace("{first_name}",contact[0])
            print(template)
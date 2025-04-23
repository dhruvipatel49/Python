def create_vcard():
    name = input("Full Name: ")
    phone = input("Phone Number: ")
    email = input("Email Address: ")
    org = input("Organization (optional): ")
    title = input("Job Title (optional): ")
    website = input("Website (optional): ")
    address = input("Address (optional): ")

    vcard = "BEGIN:VCARD\n"
    vcard += "VERSION:3.0\n"
    vcard += f"N:{name}\n"
    vcard += f"FN:{name}\n"
    if title:
        vcard += f"TITLE:{title}\n"
    if org:
        vcard += f"ORG:{org}\n"
    vcard += f"TEL;TYPE=CELL:{phone}\n"
    vcard += f"EMAIL;TYPE=INTERNET:{email}\n"
    if website:
        vcard += f"URL:{website}\n"
    if address:
        vcard += f"ADR;TYPE=HOME:;;{address}\n"
    vcard += "END:VCARD\n"

    with open("contact.vcf", "w") as file:
        file.write(vcard)
    print("vCard saved as contact.vcf")

create_vcard()
 
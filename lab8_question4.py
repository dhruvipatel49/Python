names_set={"Alice","Adam","Brian","Bob","Andrew","Bella","Alex"}
a_names={name for name in names_set if name.startswith("A")}
b_names={name for name in names_set if name.startswith("B")}
print("Names starting with A:",a_names)
print("Names starting with B:",b_names)


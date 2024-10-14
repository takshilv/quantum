import uuid
import datetime

# Input strings
string1 = "user1234"
string2 = str(datetime.datetime.now().strftime("%H:%M:%S"))
print(string2)
# Create a unique ID
unique_id = str(uuid.uuid5(uuid.NAMESPACE_DNS, string1 + string2))

# Output the unique ID
print(unique_id)
# f9fc09e1-6058-5717-bb90-d5859c54242a
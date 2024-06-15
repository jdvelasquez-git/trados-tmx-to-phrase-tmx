import re
import pandas as pd
i = 0

# Get list of Phrase username mappings
userList = pd.read_excel('tmx_replace_list.xlsx',sheet_name='Sheet1')

# Create lists for columns A and B
old_user = userList['username'].tolist()
new_user = userList['username_phrase'].tolist()

# Open TMX file in read-only mode
with open(r'sample.tmx','r',errors="ignore") as file:
    tmx_contents = file.read()

# Find old users and replace them with new users
for users in old_user:
    tmx_contents = re.sub(old_user[i],new_user[i],tmx_contents)
    i += 1

# Write TMX file
with open(r'sample.tmx','w',errors="ignore") as file:
    file.write(tmx_contents)

print("The operation has completed successfully.")
import csv
import json
compromised_users = []

# Open 'passwords.csv', read its contents, and append usernames to 'compromised_users' list
# Ensure 'passwords.csv' is in the directory
try:
  with open('passwords.csv') as password_file:
    password_csv = csv.DictReader(password_file)
    for password_row in password_csv:
      #compromised_users.append(password_row['Username'])
      compromised_users = [password_row['Username'] for password_row in password_csv]
except:
   print('File not found.')
#Open compromised user file and the user names in the file 
with open('compromised_users.txt', 'w') as compromised_user_file:
  for user in compromised_users:
    compromised_user_file.write(user + "\n")
# Open 'boss_message.json' to send a message to the boss
with open('boss_message.json', 'w') as boss_message:
  boss_message_dict = {"recipient": "The Boss", "message": "Mission Success"}
  json.dump(boss_message_dict, boss_message)

#Create new "password file" and write signature message 
with open('new_passwords.csv', 'w') as new_passwords_obj:
  slash_null_sig = """ _  _     ___   __  ____             
/ )( \   / __) /  \(_  _)            
) \/ (  ( (_ \(  O ) )(              
\____/   \___/ \__/ (__)             
 _  _   __    ___  __ _  ____  ____  
/ )( \ / _\  / __)(  / )(  __)(    \ 
) __ (/    \( (__  )  (  ) _)  ) D ( 
\_)(_/\_/\_/ \___)(__\_)(____)(____/ 
        ____  __     __   ____  _  _ 
 ___   / ___)(  )   / _\ / ___)/ )( \
(___)  \___ \/ (_/\/    \\___ \) __ (
       (____/\____/\_/\_/(____/\_)(_/
 __ _  _  _  __    __                
(  ( \/ )( \(  )  (  )               
/    /) \/ (/ (_/\/ (_/\             
\_)__)\____/\____/\____/
"""
  new_passwords_obj.write(slash_null_sig)



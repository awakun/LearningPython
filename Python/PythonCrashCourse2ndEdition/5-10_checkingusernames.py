current_users = ['user1', 'user2', 'User3', 'User4', 'user5', 'admin']
new_users = ['user4', 'user5', 'user6', 'Julia', 'Cassandra' 'Elizabeth']

lower_current_users = [user.lower() for user in current_users]
for user in new_users:
    if user.lower() in lower_current_users:
        print(f'User {user} already exists.')
    else:
        print(f"{user} is available!")

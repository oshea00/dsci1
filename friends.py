from __future__ import division
from collections import defaultdict, Counter
# import random

users = [
    {"id": 0, "name": "Hero"},
    {"id": 1, "name": "Dunn"},
    {"id": 2, "name": "Sue"},
    {"id": 3, "name": "Chi"},
    {"id": 4, "name": "Thor"},
    {"id": 5, "name": "Clive"},
    {"id": 6, "name": "Hicks"},
    {"id": 7, "name": "Devon"},
    {"id": 8, "name": "Kate"},
    {"id": 9, "name": "Klein"}
]

friendships = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4),
               (4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)]

for user in users:
    user["friends"] = []

for i, j in friendships:
    users[i]["friends"].append(users[j])
    users[j]["friends"].append(users[i])

def number_of_friends(user):
    return len(user["friends"])

total_connections = sum(number_of_friends(user) for user in users)

num_users = len(users)

avg_connections = total_connections / num_users

num_friends_by_id =  [(user["id"], number_of_friends(user)) for user in users]

top_friend_holders =  sorted(num_friends_by_id, key=lambda (id, numf): numf, reverse=True)

def not_the_same(user1, user2):
    return user1["id"] != user2["id"]

def not_friends(user1, user2):
    return all([not_the_same(user2, u) for u in user1["friends"]])

print (not_friends(users[0],users[1]))

def friends_of_friends_ids(user1):
    return [foaf["id"]
              for friend in user1["friends"]
              for foaf in friend["friends"]
              if not_friends(user1, foaf) and
              not_the_same(user1, foaf)
              ]

print(Counter(friends_of_friends_ids(users[3])))

print()






#print("hello world")

#voting_data = []

# {key1:value1, key2:value2}
# counties_dict = {'Arapahoe': 422829,
#                  'Denver': 463353,
#                  'Jefferson': 432438}

# print(counties_dict)
# print(counties_dict.get("Arapahoe"))
# print(counties_dict['Arapahoe'])

# voting_data.append({"county":"Arapahoe", "registered_voters": 422829})
# voting_data.append({"county":"Denver", "registered_voters": 463353})
# voting_data.append({"county":"Jefferson", "registered_voters": 432438})

# print(voting_data)

# What is the score?
score = int(input("What is your test score? "))

# Determine the grade.
if score >= 90:
    print('Your grade is an A.')
elif score >= 80:
    print('Your grade is a B.')
elif score >= 70:
    print('Your grade is a C.')
elif score >= 60:
    print('Your grade is a D.')
else:
    print('Your grade is an F.')

# How many votes did you get?
my_votes = int(input("How many votes did you get in the election? "))
#  Total votes in the election
total_votes = int(input("What is the total votes in the election? "))
# Calculate the percentage of votes you received.
percentage_votes = (my_votes / total_votes) * 100
print("I received " + str(percentage_votes)+"% of the total votes.")
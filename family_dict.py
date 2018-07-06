my_family = {
    'badsister': {
        'name': 'Courtney',
        'age': 32
    },
    'sister': {
        'name': 'Susanna',
        'age': 27
    },
    'mother': {
        'name': 'Jeanne',
        'age': 'Umpteen'
    },
    'father': {
        'name': 'Dennis',
        'age': 'Whatever'
    }
}


# my solution
my_peeps = {f'my {relation} is {data["name"]} and is {data["age"]} years old'
            for (relation, data) in my_family.items()
            }
print(my_peeps)

#  joe's solution

family_stuff = {
    f'{member_values["name"]} is my {family_member} and is {str(member_values["age"])} years old.'
    for (family_member, member_values) in my_family.items()
}

print("My family!", family_stuff)

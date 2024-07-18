import random

def get_data(data):
    return random.choice(data)

def reshape_data(data):
    name = data['name']
    description = data['description']
    country = data['country']
    follower = data['follower_count']
    return f"{name}, a {description}, from {country}", follower

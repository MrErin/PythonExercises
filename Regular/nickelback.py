# Example set
songs = {
    ('Nickelback', 'How You Remind Me'),
    ('Will.i.am', 'That Power'),
    ('Miles Davis', 'Stella by Starlight'),
    ('Nickelback', 'Animals')
}

# Using a set comprehension, create a new set that contains all songs that were not performed by Nickelback.

print(list(
    f'The song is {song[1]} and the artist is {song[0]}' for song in songs if not song[0] == 'Nickelback'))

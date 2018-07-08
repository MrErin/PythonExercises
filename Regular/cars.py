# Create an empty set named `showroom`.
showroom = set()
print(len(showroom))
print(f'When it\'s empty the showroom contains: {showroom}')

# Add four of your favorite car model names to the set.
# Print the length of your set.
showroom.add('Nimbus 2000')
showroom.add('Cleansweep Five')
showroom.add('Firebolt')
showroom.add('Nimbus 2001')
print(len(showroom))
print(f'Now the showroom contains: {showroom}')

# Pick one of the items in your show room and add it to the set again.
# Print your showroom. Notice how there's still only one instance of that model in there.
showroom.add('Comet 140')
print(len(showroom))
print(f'Now the showroom contains: {showroom}')

# Using `update()`, add two more car models to your showroom with another set.
new_models = set()
new_models.add('Silver Arrow')
new_models.add('Air Wave Gold')
print(len(new_models))
print(f'Yay! New Models! {new_models}')
showroom.update(new_models)
print(len(showroom))
print(f'Now the showroom contains: {showroom}')

# You've sold one of your cars. Remove it from the set with the `discard()` method.
showroom.discard('Comet 140')
print(f'after discard, the showroom contains: {showroom}')

# Now create another set of cars in a variable `junkyard`. Someone who owns a junkyard full of old cars has approached you about buying the entire inventory. In the new set, add some different cars, but also add a few that are the same as in the `showroom` set.
junkyard = set()
junkyard.add('Comet 140')
junkyard.add('Silver Arrow')
junkyard.add('Twigger 90')
junkyard.add('Moontrimmer')
junkyard.add('Cleansweep Eleven')
junkyard.add('Nimbus 1000')
junkyard.add('Nimbus 2000')
print(len(junkyard))
print(f'Junkyard contains: {junkyard}')
print(f'Showroom contains: {showroom}')

# Use the `intersection` method to see which cars exist in both the showroom and that junkyard.
print(
    f'These brooms are in both the junkyard and the showroom: {set.intersection(junkyard, showroom)}')

# Now you're ready to buy the cars in the junkyard. Use the `union` method to combine the junkyard into your showroom.
print(
    f'These are the brooms in the showroom after the junkyard purchase: {showroom.union(junkyard)}')

# Use the `discard()` method to remove any cars that you acquired from the junkyard that you want in your showroom.
junkyard.discard('Twigger 90')
junkyard.discard('Moontrimmer')
junkyard.discard('Cleansweep Eleven')
junkyard.discard('Nimbus 1000')
print(f'Now the junkyard still has: {junkyard}')
print(f'The showroom contains: {showroom}')

#  ? The Comet 140 is the one discarded from the showroom. There was one in the junkyard, and it should have been added to the showroom during the purchase, but it wasn't It just disappears. Why?
print(f'WHAT HAPPENED TO THE COMET 140???')

# Create a tuple named zoo that contains your favorite animals.
pokedex = ("Pikachu", "Froakie", "Treecko", "Cubone", "Machop", "Magby", "Charizard")

# Find one of your animals using the .index(value) method on the tuple.
print(pokedex.index("Pikachu"))
# print(pokedex[0])

# Determine if an animal is in your tuple by using value in tuple.

# for pokemon in pokedex:
#   if pokemon == "Pikachu":
#     print(pokemon)
#   else:
#     print("You dont own that pokemon")

if "Pikachu" in pokedex:
  print("Amazing you have a pikachu")
else:
  print("oops")

# for pokemon in pokedex:
#  if pokemon in pokedex:
#   print("{0}".format(pokemon))

# Create a variable for each of the animals in your tuple with this cool feature of Python.

# pikachu = pokedex[0]
# print(pikachu)

(pokemon1, pokemon2, pokemon3, pokemon4, pokemon5, pkemon6, pokemon7) = pokedex
# print(pokemon1)
# Convert your tuple into a list.

pokedex_list = list(pokedex)
# print(pokedex_list)

# Use extend() to add three more animals to your zoo.

pokedex_list.extend({"Greninja", "Ursaring", "Mewtwo"})
# print(pokedex_list)

# Convert the list back into a tuple.

new_pokedex_tuple = tuple(pokedex_list)
print(new_pokedex_tuple)





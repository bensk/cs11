class Pet(object):
    """Represents a pet"""

my_pet_1 = Pet()
my_pet_1.type = 'direwolf'
my_pet_1.noise = 'howl'
my_pet_1.full_name = 'Ghost'

my_pet_2 = Pet()
my_pet_2.type = 'direwolf'
my_pet_2.noise = 'howl'
my_pet_2.full_name = 'Nymeria'

my_pet_3 = Pet()
my_pet_3.type = 'direwolf'
my_pet_3.noise = 'howl'
my_pet_3.full_name = 'Summer'

my_pets = [my_pet_1, my_pet_2, my_pet_3]
print type(my_pets)
print type(my_pet_1)
print type('Summer')
for pet in my_pets:
    print pet.full_name

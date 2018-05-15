# main module for MapGenerator

from dungeon import Generator
import printer

params = {
    'transitions_type' : 'both', # corridors/portals/both
    'each_room_transitions': True, # bool. Generate a corridor for each room
    'must_conected': False, # bool. Generate additional corridors, if needed, to connect the dungeon
    'room_size': (3, 5), # min, max
    'rooms_count': 20,
    'base_connecting': 'farest', # closest, farest, random
    'width': 120,
    'height': 80
}

# map generation
dung = Generator(params)
dung.generate() # array[][] of dungeon

# map printing
printer.draw(dung.result)
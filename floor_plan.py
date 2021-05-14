def floor_cost():
        floor_area = int(input('enterthe floor area in squer feet:'))
        tile_size = int(input('enterthe size of tile : '))
        tile_cost = int(input('enterthe cost of tile Rupees:')) 
        cost_of_floor = floor_area / tile_size * tile_cost
        print (cost_of_floor)

floor_cost()
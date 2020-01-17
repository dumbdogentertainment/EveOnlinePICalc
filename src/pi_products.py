from pi_recipe import PI_Recipe, list_to_dict
from pi_p4 import *

mha_recipe = PI_Recipe('moon harvesting array',
                       1,
                       [('broadcast node', 4, broadcast_node_recipe),
                        ('nano-factory', 2, nanofactory_recipe),
                        ('recursive computing module', 2, recursive_computing_module_recipe),
                        ('self-harmonizing power core', 2, selfharmonizing_power_core_recipe)],
                       'structure')

large_tower_recipe = PI_Recipe('amarr control tower',
                               1,
                               [('broadcast node', 18, broadcast_node_recipe),
                                ('integrity response drones', 32, integrity_response_drones_recipe),
                                ('nano-factory', 26, nanofactory_recipe),
                                ('organic mortar applicators', 28, organic_mortar_applicators_recipe),
                                ('recursive computing module', 18, recursive_computing_module_recipe),
                                ('self-harmonizing power core', 18, selfharmonizing_power_core_recipe),
                                ('sterile conduits', 28, sterile_conduits_recipe),
                                ('wetware mainframe', 12, wetware_mainframe_recipe)],
                               'structure')

gallente_large_tower = large_tower_recipe
gallente_large_tower._name = 'Gallente Control Tower'

amarr_large_tower = large_tower_recipe
amarr_large_tower._name = 'Amarr Control Tower'

if __name__ == '__main__':
    d = list_to_dict(integrity_response_drones_recipe.Mat_List(60, 'P1'))
    for k,v in d.items():
        print '%d %s' % (v[1], v[0])
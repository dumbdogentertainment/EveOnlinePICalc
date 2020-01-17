from pi_p3 import *

""" P4 RECIPES """
broadcast_node_recipe = PI_Recipe('broadcast node',
                                  1,
                                  [('neocoms', 6, neocoms_recipe),
                                   ('data chips', 6, data_chips_recipe),
                                   ('high-tech transmitters', 6, hightech_transmitters_recipe)],
                                  'P4')

integrity_response_drones_recipe = PI_Recipe('integrity response drones', 1, [('gel-matrix biopaste', 6, gelmatrix_biopaste_recipe),
                                                                              ('hazmat detection systems', 6, hazmat_detection_systems_recipe),
                                                                              ('planetary vehicles', 6, planetary_vehicles_recipe)], 'P4')
nanofactory_recipe = PI_Recipe('nano-factory', 1, [('ukomi super conductors', 6, ukomi_super_conductors_recipe),
                                                   ('industrial explosives', 6, industrial_explosives_recipe),
                                                   ('reactive metals', 40, reactive_metals_recipe)], 'P4')
organic_mortar_applicators_recipe = PI_Recipe('organic mortar applicators', 1, [('condensates', 6, condensates_recipe),
                                                                                ('robotics', 6, robotics_recipe),
                                                                                ('bacteria', 40, bacteria_recipe)], 'P4')
recursive_computing_module_recipe = PI_Recipe('recursive computing module', 1, [('synthetic synapses', 6, synthetic_synapses_recipe),
                                                                                ('guidance systems', 6, guidance_systems_recipe),
                                                                                ('transcranial microcontrollers', 6, transcranial_microcontrollers_recipe)], 'P4')
selfharmonizing_power_core_recipe = PI_Recipe('self-harmonizing power core', 1, [('camera drones', 6, camera_drones_recipe),
                                                                                 ('nuclear reactors', 6, nuclear_reactors_recipe),
                                                                                 ('hermetic membranes', 6, hermetic_membranes_recipe)], 'P4')
sterile_conduits_recipe = PI_Recipe('sterile conduits', 1, [('vaccines', 6, vaccines_recipe),
                                                            ('smartfab units', 6, smartfab_units_recipe),
                                                            ('water', 40, water_recipe)], 'P4')
wetware_mainframe_recipe = PI_Recipe('wetware mainframe', 1, [('supercomputers', 6, supercomputers_recipe),
                                                              ('biotech research reports', 6, biotech_research_reports_recipe),
                                                              ('cryoprotectant solution', 6, cryoprotectant_solution_recipe)], 'P4')

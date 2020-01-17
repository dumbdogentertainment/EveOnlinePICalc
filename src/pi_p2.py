#from pi_recipe import PI_Recipe
from pi_p1 import *

""" P2 RECIPES """
biocells_recipe = PI_Recipe('biocells', 5, [('biofuels', 40, biofuels_recipe),
                                            ('precious metals', 40, precious_metals_recipe)], 'P2')
construction_blocks_recipe = PI_Recipe('construction blocks', 5, [('reactive metals', 40, reactive_metals_recipe),
                                                                  ('toxic metals', 40, toxic_metals_recipe)], 'P2')
consumer_electronics_recipe = PI_Recipe('consumer electronics', 5, [('toxic metals', 40, toxic_metals_recipe),
                                                                    ('chiral structures', 40, chiral_structures_recipe)], 'P2')
coolant_recipe = PI_Recipe('coolant', 5, [('water', 40, water_recipe),
                                          ('electrolytes', 40, electrolytes_recipe)], 'P2')
enriched_uranium_recipe = PI_Recipe('enriched uranium', 5, [('precious metals', 40, precious_metals_recipe),
                                                            ('toxic metals', 40, toxic_metals_recipe)], 'P2')
fertilizer_recipe = PI_Recipe('fertilizer', 5, [('proteins', 40, proteins_recipe),
                                                ('bacteria', 40, bacteria_recipe)], 'P2')
genetic_enhanced_livestock_recipe = PI_Recipe('genetic enhanced livestock', 5, [('proteins', 40, proteins_recipe),
                                                                                ('biomass', 40, biomass_recipe)], 'P2')
livestock_recipe = PI_Recipe('livestock', 5, [('biofuels', 40, biofuels_recipe),
                                              ('proteins', 40, proteins_recipe)], 'P2')
mechanical_parts_recipe = PI_Recipe('mechanical parts', 5, [('precious metals', 40, precious_metals_recipe),
                                                            ('reactive metals', 40, reactive_metals_recipe)], 'P2')
miniature_electronics_recipe = PI_Recipe('miniature electronics', 5, [('silicon', 40, silicon_recipe),
                                                                      ('chiral structures', 40, chiral_structures_recipe)], 'P2')
microfiber_shielding_recipe = PI_Recipe('microfiber shielding', 5, [('silicon', 40, silicon_recipe),
                                                                    ('industrial fibers', 40, industrial_fibers_recipe)], 'P2')
nanites_recipe = PI_Recipe('nanites', 5, [('reactive metals', 40, reactive_metals_recipe),
                                          ('bacteria', 40, bacteria_recipe)], 'P2')
oxides_recipe = PI_Recipe('oxides', 5, [('oxygen', 40, oxygen_recipe),
                                        ('oxidizing compound', 40, oxidizing_compound_recipe)], 'P2')
polyamarids_recipe = PI_Recipe('polyamarids', 5, [('industrial fibers', 40, industrial_fibers_recipe),
                                                  ('oxidizing compound', 40, oxidizing_compound_recipe)], 'P2')
polytextiles_recipe = PI_Recipe('polytextiles', 5, [('biofuels', 40, biofuels_recipe),
                                                    ('industrial fibers', 40, industrial_fibers_recipe)], 'P2')
rocket_fuel_recipe = PI_Recipe('rocket fuel', 5, [('electrolytes', 40, electrolytes_recipe),
                                                  ('plasmoids', 40, plasmoids_recipe)], 'P2')
silicate_glass_recipe = PI_Recipe('silicate glass', 5, [('oxidizing compound', 40, oxidizing_compound_recipe),
                                                        ('silicon', 40, silicon_recipe)], 'P2')
supertensile_plastics_recipe = PI_Recipe('supertensile plastics', 5, [('biomass', 40, biomass_recipe),
                                                                      ('oxygen', 40, oxygen_recipe)], 'P2')
super_conductors_recipe = PI_Recipe('super conductors', 5, [('plasmoids', 40, plasmoids_recipe),
                                                            ('water', 40, water_recipe)], 'P2')
synthetic_oil_recipe = PI_Recipe('synthetic oil', 5, [('electrolytes', 40, electrolytes_recipe),
                                                      ('oxygen', 40, oxygen_recipe)], 'P2')
test_cultures_recipe = PI_Recipe('test cultures', 5, [('water', 40, water_recipe),
                                                      ('bacteria', 40, bacteria_recipe)], 'P2')
transmitter_recipe = PI_Recipe('transmitter', 5, [('chiral structures', 40, chiral_structures_recipe),
                                                  ('plasmoids', 40, plasmoids_recipe)], 'P2')
viral_agent_recipe = PI_Recipe('viral agent', 5, [('bacteria', 40, bacteria_recipe),
                                                  ('biomass', 40, biomass_recipe)], 'P2')
watercooled_cpu_recipe = PI_Recipe('water-cooled cpu', 5, [('water', 40, water_recipe),
                                                           ('reactive metals', 40, reactive_metals_recipe)], 'P2')

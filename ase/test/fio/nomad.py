# Stripped (minimal) version of nomad entry with 3 images.
# The images are actually identical for some reason, but we want to be sure
# that they are extracted correctly.

nomad_data = """{"uri": "nmd://N9Jqc1y-Bzf7sI1R9qhyyyoIosJDs/C74RJltyQeM9_WFuJYO49AR4gKuJ2", "section_run": [{"name": "section_run", "uri": "nmd://N9Jqc1y-Bzf7sI1R9qhyyyoIosJDs/C74RJltyQeM9_WFuJYO49AR4gKuJ2/section_run/0c", "gIndex": 0, "section_system": [{"configuration_periodic_dimensions": [{"flatData": [true, true, true]}], "uri": "nmd://N9Jqc1y-Bzf7sI1R9qhyyyoIosJDs/C74RJltyQeM9_WFuJYO49AR4gKuJ2/section_run/0c/section_system/0c", "gIndex": 0, "lattice_vectors": {"flatData": [1.289082e-09, 0.0, 0.0, 0.0, 1.2238921e-09, 0.0, 0.0, 0.0, 1.103065e-09]}, "name": "section_system", "atom_positions": {"flatData": [1.8369957336276003e-10, 1.6999517355319901e-10, 0.0, 8.282405733627601e-10, 4.41950876446801e-10, 0.0, 4.6084142663724006e-10, 7.81941223553199e-10, 0.0, 1.1053824266372401e-09, 1.053896926446801e-09, 0.0, 6.44541e-10, 0.0, 1.2892214482885e-10, 0.0, 6.1194605e-10, 1.2892214482885e-10, 1.0605776359825801e-09, 1.98497527706708e-10, 2.5802171766295004e-10, 4.1603663598258003e-10, 4.13448522293292e-10, 2.5802171766295004e-10, 8.730453640174201e-10, 8.10443577706708e-10, 2.5802171766295004e-10, 2.2850436401742e-10, 1.025394572293292e-09, 2.5802171766295004e-10, 5.2517352791676e-10, 4.6602249641989005e-11, 5.515325e-10, 1.4685300778002002e-10, 1.66342369669381e-10, 5.515325e-10, 7.9139400778002e-10, 4.45603680330619e-10, 5.515325e-10, 1.1697145279167601e-09, 5.65343800358011e-10, 5.515325e-10, 1.1936747208324e-10, 6.58548299641989e-10, 5.515325e-10, 4.976879922199801e-10, 7.78288419669381e-10, 5.515325e-10, 1.14222899221998e-09, 1.057549730330619e-09, 5.515325e-10, 7.6390847208324e-10, 1.177289850358011e-09, 5.515325e-10, 1.0605776359825801e-09, 1.98497527706708e-10, 8.450432823370501e-10, 4.1603663598258003e-10, 4.13448522293292e-10, 8.450432823370501e-10, 8.730453640174201e-10, 8.10443577706708e-10, 8.450432823370501e-10, 2.2850436401742e-10, 1.025394572293292e-09, 8.450432823370501e-10, 6.44541e-10, 0.0, 9.7414285517115e-10, 0.0, 6.1194605e-10, 9.7414285517115e-10, 9.1056464993268e-10, 1.25465107864641e-10, 0.0, 5.4589940120358e-10, 2.7689366691594603e-10, 0.0, 1.19044040120358e-09, 3.35052383084054e-10, 0.0, 2.6602364993268e-10, 4.86480942135359e-10, 0.0, 1.0230583500673202e-09, 7.37411157864641e-10, 0.0, 9.864159879642e-11, 8.88839716915946e-10, 0.0, 7.431825987964201e-10, 9.469984330840542e-10, 0.0, 3.7851735006732003e-10, 1.098426992135359e-09, 0.0, 0.0, 0.0, 2.0246975378805e-10, 6.44541e-10, 6.1194605e-10, 2.0246975378805e-10, 3.4046283730566e-10, 1.17495575349518e-10, 3.040167815311e-10, 9.8500383730566e-10, 4.944504746504821e-10, 3.040167815311e-10, 3.0407816269434e-10, 7.29441625349518e-10, 3.040167815311e-10, 9.486191626943402e-10, 1.106396524650482e-09, 3.040167815311e-10, 7.3089033824148e-10, 2.12568186818173e-10, 3.5617527624000004e-10, 8.634933824148001e-11, 3.9937786318182705e-10, 3.5617527624000004e-10, 1.2027326617585201e-09, 8.24514236818173e-10, 3.5617527624000004e-10, 5.581916617585201e-10, 1.011323913181827e-09, 3.5617527624000004e-10, 1.11810587223036e-09, 1.51565512577295e-10, 5.515325e-10, 4.7356487223036e-10, 4.60380537422705e-10, 5.515325e-10, 8.155171277696401e-10, 7.63511562577295e-10, 5.515325e-10, 1.7097612776964e-10, 1.072326587422705e-09, 5.515325e-10, 7.3089033824148e-10, 2.12568186818173e-10, 7.468897237600001e-10, 8.634933824148001e-11, 3.9937786318182705e-10, 7.468897237600001e-10, 1.2027326617585201e-09, 8.24514236818173e-10, 7.468897237600001e-10, 5.581916617585201e-10, 1.011323913181827e-09, 7.468897237600001e-10, 3.4046283730566e-10, 1.17495575349518e-10, 7.990482184689e-10, 9.8500383730566e-10, 4.944504746504821e-10, 7.990482184689e-10, 3.0407816269434e-10, 7.29441625349518e-10, 7.990482184689e-10, 9.486191626943402e-10, 1.106396524650482e-09, 7.990482184689e-10, 0.0, 0.0, 9.005952462119501e-10, 6.44541e-10, 6.1194605e-10, 9.005952462119501e-10]}, "atom_species": [33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 38, 38, 38, 38, 38, 38, 38, 38, 38, 38, 38, 38, 38, 38, 38, 38, 38, 38, 38, 38, 38, 38, 38, 38, 38, 38, 38, 38, 38, 38, 38, 38]}, {"configuration_periodic_dimensions": [{"flatData": [true, true, true]}], "uri": "nmd://N9Jqc1y-Bzf7sI1R9qhyyyoIosJDs/C74RJltyQeM9_WFuJYO49AR4gKuJ2/section_run/0c/section_system/1c", "lattice_vectors": {"flatData": [1.289082e-09, 0.0, 0.0, 0.0, 1.2238921e-09, 0.0, 0.0, 0.0, 1.103065e-09]}, "gIndex": 1, "name": "section_system", "atom_positions": {"flatData": [1.8369957336276003e-10, 1.6999517355319901e-10, 0.0, 8.282405733627601e-10, 4.41950876446801e-10, 0.0, 4.6084142663724006e-10, 7.81941223553199e-10, 0.0, 1.1053824266372401e-09, 1.053896926446801e-09, 0.0, 6.44541e-10, 0.0, 1.2892214482885e-10, 0.0, 6.1194605e-10, 1.2892214482885e-10, 1.0605776359825801e-09, 1.98497527706708e-10, 2.5802171766295004e-10, 4.1603663598258003e-10, 4.13448522293292e-10, 2.5802171766295004e-10, 8.730453640174201e-10, 8.10443577706708e-10, 2.5802171766295004e-10, 2.2850436401742e-10, 1.025394572293292e-09, 2.5802171766295004e-10, 5.2517352791676e-10, 4.6602249641989005e-11, 5.515325e-10, 1.4685300778002002e-10, 1.66342369669381e-10, 5.515325e-10, 7.9139400778002e-10, 4.45603680330619e-10, 5.515325e-10, 1.1697145279167601e-09, 5.65343800358011e-10, 5.515325e-10, 1.1936747208324e-10, 6.58548299641989e-10, 5.515325e-10, 4.976879922199801e-10, 7.78288419669381e-10, 5.515325e-10, 1.14222899221998e-09, 1.057549730330619e-09, 5.515325e-10, 7.6390847208324e-10, 1.177289850358011e-09, 5.515325e-10, 1.0605776359825801e-09, 1.98497527706708e-10, 8.450432823370501e-10, 4.1603663598258003e-10, 4.13448522293292e-10, 8.450432823370501e-10, 8.730453640174201e-10, 8.10443577706708e-10, 8.450432823370501e-10, 2.2850436401742e-10, 1.025394572293292e-09, 8.450432823370501e-10, 6.44541e-10, 0.0, 9.7414285517115e-10, 0.0, 6.1194605e-10, 9.7414285517115e-10, 9.1056464993268e-10, 1.25465107864641e-10, 0.0, 5.4589940120358e-10, 2.7689366691594603e-10, 0.0, 1.19044040120358e-09, 3.35052383084054e-10, 0.0, 2.6602364993268e-10, 4.86480942135359e-10, 0.0, 1.0230583500673202e-09, 7.37411157864641e-10, 0.0, 9.864159879642e-11, 8.88839716915946e-10, 0.0, 7.431825987964201e-10, 9.469984330840542e-10, 0.0, 3.7851735006732003e-10, 1.098426992135359e-09, 0.0, 0.0, 0.0, 2.0246975378805e-10, 6.44541e-10, 6.1194605e-10, 2.0246975378805e-10, 3.4046283730566e-10, 1.17495575349518e-10, 3.040167815311e-10, 9.8500383730566e-10, 4.944504746504821e-10, 3.040167815311e-10, 3.0407816269434e-10, 7.29441625349518e-10, 3.040167815311e-10, 9.486191626943402e-10, 1.106396524650482e-09, 3.040167815311e-10, 7.3089033824148e-10, 2.12568186818173e-10, 3.5617527624000004e-10, 8.634933824148001e-11, 3.9937786318182705e-10, 3.5617527624000004e-10, 1.2027326617585201e-09, 8.24514236818173e-10, 3.5617527624000004e-10, 5.581916617585201e-10, 1.011323913181827e-09, 3.5617527624000004e-10, 1.11810587223036e-09, 1.51565512577295e-10, 5.515325e-10, 4.7356487223036e-10, 4.60380537422705e-10, 5.515325e-10, 8.155171277696401e-10, 7.63511562577295e-10, 5.515325e-10, 1.7097612776964e-10, 1.072326587422705e-09, 5.515325e-10, 7.3089033824148e-10, 2.12568186818173e-10, 7.468897237600001e-10, 8.634933824148001e-11, 3.9937786318182705e-10, 7.468897237600001e-10, 1.2027326617585201e-09, 8.24514236818173e-10, 7.468897237600001e-10, 5.581916617585201e-10, 1.011323913181827e-09, 7.468897237600001e-10, 3.4046283730566e-10, 1.17495575349518e-10, 7.990482184689e-10, 9.8500383730566e-10, 4.944504746504821e-10, 7.990482184689e-10, 3.0407816269434e-10, 7.29441625349518e-10, 7.990482184689e-10, 9.486191626943402e-10, 1.106396524650482e-09, 7.990482184689e-10, 0.0, 0.0, 9.005952462119501e-10, 6.44541e-10, 6.1194605e-10, 9.005952462119501e-10]}, "atom_species": [33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 38, 38, 38, 38, 38, 38, 38, 38, 38, 38, 38, 38, 38, 38, 38, 38, 38, 38, 38, 38, 38, 38, 38, 38, 38, 38, 38, 38, 38, 38, 38, 38]}, {"configuration_periodic_dimensions": [{"flatData": [true, true, true]}], "uri": "nmd://N9Jqc1y-Bzf7sI1R9qhyyyoIosJDs/C74RJltyQeM9_WFuJYO49AR4gKuJ2/section_run/0c/section_system/2c", "gIndex": 2, "lattice_vectors": {"flatData": [1.289082e-09, 0.0, 0.0, 0.0, 1.2238921e-09, 0.0, 0.0, 0.0, 1.103065e-09]}, "name": "section_system", "atom_positions": {"flatData": [1.8369957336276003e-10, 1.6999517355319901e-10, 0.0, 8.282405733627601e-10, 4.41950876446801e-10, 0.0, 4.6084142663724006e-10, 7.81941223553199e-10, 0.0, 1.1053824266372401e-09, 1.053896926446801e-09, 0.0, 6.44541e-10, 0.0, 1.2892214482885e-10, 0.0, 6.1194605e-10, 1.2892214482885e-10, 1.0605776359825801e-09, 1.98497527706708e-10, 2.5802171766295004e-10, 4.1603663598258003e-10, 4.13448522293292e-10, 2.5802171766295004e-10, 8.730453640174201e-10, 8.10443577706708e-10, 2.5802171766295004e-10, 2.2850436401742e-10, 1.025394572293292e-09, 2.5802171766295004e-10, 5.2517352791676e-10, 4.6602249641989005e-11, 5.515325e-10, 1.4685300778002002e-10, 1.66342369669381e-10, 5.515325e-10, 7.9139400778002e-10, 4.45603680330619e-10, 5.515325e-10, 1.1697145279167601e-09, 5.65343800358011e-10, 5.515325e-10, 1.1936747208324e-10, 6.58548299641989e-10, 5.515325e-10, 4.976879922199801e-10, 7.78288419669381e-10, 5.515325e-10, 1.14222899221998e-09, 1.057549730330619e-09, 5.515325e-10, 7.6390847208324e-10, 1.177289850358011e-09, 5.515325e-10, 1.0605776359825801e-09, 1.98497527706708e-10, 8.450432823370501e-10, 4.1603663598258003e-10, 4.13448522293292e-10, 8.450432823370501e-10, 8.730453640174201e-10, 8.10443577706708e-10, 8.450432823370501e-10, 2.2850436401742e-10, 1.025394572293292e-09, 8.450432823370501e-10, 6.44541e-10, 0.0, 9.7414285517115e-10, 0.0, 6.1194605e-10, 9.7414285517115e-10, 9.1056464993268e-10, 1.25465107864641e-10, 0.0, 5.4589940120358e-10, 2.7689366691594603e-10, 0.0, 1.19044040120358e-09, 3.35052383084054e-10, 0.0, 2.6602364993268e-10, 4.86480942135359e-10, 0.0, 1.0230583500673202e-09, 7.37411157864641e-10, 0.0, 9.864159879642e-11, 8.88839716915946e-10, 0.0, 7.431825987964201e-10, 9.469984330840542e-10, 0.0, 3.7851735006732003e-10, 1.098426992135359e-09, 0.0, 0.0, 0.0, 2.0246975378805e-10, 6.44541e-10, 6.1194605e-10, 2.0246975378805e-10, 3.4046283730566e-10, 1.17495575349518e-10, 3.040167815311e-10, 9.8500383730566e-10, 4.944504746504821e-10, 3.040167815311e-10, 3.0407816269434e-10, 7.29441625349518e-10, 3.040167815311e-10, 9.486191626943402e-10, 1.106396524650482e-09, 3.040167815311e-10, 7.3089033824148e-10, 2.12568186818173e-10, 3.5617527624000004e-10, 8.634933824148001e-11, 3.9937786318182705e-10, 3.5617527624000004e-10, 1.2027326617585201e-09, 8.24514236818173e-10, 3.5617527624000004e-10, 5.581916617585201e-10, 1.011323913181827e-09, 3.5617527624000004e-10, 1.11810587223036e-09, 1.51565512577295e-10, 5.515325e-10, 4.7356487223036e-10, 4.60380537422705e-10, 5.515325e-10, 8.155171277696401e-10, 7.63511562577295e-10, 5.515325e-10, 1.7097612776964e-10, 1.072326587422705e-09, 5.515325e-10, 7.3089033824148e-10, 2.12568186818173e-10, 7.468897237600001e-10, 8.634933824148001e-11, 3.9937786318182705e-10, 7.468897237600001e-10, 1.2027326617585201e-09, 8.24514236818173e-10, 7.468897237600001e-10, 5.581916617585201e-10, 1.011323913181827e-09, 7.468897237600001e-10, 3.4046283730566e-10, 1.17495575349518e-10, 7.990482184689e-10, 9.8500383730566e-10, 4.944504746504821e-10, 7.990482184689e-10, 3.0407816269434e-10, 7.29441625349518e-10, 7.990482184689e-10, 9.486191626943402e-10, 1.106396524650482e-09, 7.990482184689e-10, 0.0, 0.0, 9.005952462119501e-10, 6.44541e-10, 6.1194605e-10, 9.005952462119501e-10]}, "atom_species": [33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 38, 38, 38, 38, 38, 38, 38, 38, 38, 38, 38, 38, 38, 38, 38, 38, 38, 38, 38, 38, 38, 38, 38, 38, 38, 38, 38, 38, 38, 38, 38, 38]}]}], "name": "calculation_context"}"""

fname = 'nmd.test.nomad.json'
with open(fname, 'w') as fd:
    fd.write(nomad_data)

from ase.io import iread

images = list(iread(fname))
assert len(images) == 3

for atoms in images:
    assert all(atoms.pbc)
    assert (atoms.cell > 0).sum() == 3
    assert atoms.get_chemical_formula() == 'As24Sr32'


# Code for cleaning up nomad files so their size is reasonable for inclusion
# in test suite:
"""
ourkeys = {'section_run', 'section_system', 'name', 'atom_species',
           'atom_positions', 'flatData', 'uri', 'gIndex',
           'configuration_periodic_dimensions', 'lattice_vectors'}

includekeys = lambda k: k in ourkeys

fname = ...
with open(fname) as fd:
    d = read(fd, includekeys=includekeys)
print(json.dumps(d))
"""

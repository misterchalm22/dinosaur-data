

potions = {}
potions.['potion ingredients'] = {}
potions.['cooking instructions'] = {}
potions.['dangers'] = {}

ing = potions['potion ingredients']
cook = potions['cooking instructions']
dangers = potions['dangers']

ing['fire potion'] = {
	'fire dragon head': 1,
	'boiling water (mL)': 800,
	'cockatrice claws (just the nail)': 3,
	'frog saliva (mL)': 5,
	'desert lizard, alive, 10g': 1,
	'night fury scale': 1,
}

cook['fire potion'] = {
	'cook time (mins)': 30,
	'cook method': 'suspended over a volcano',
	'special instructions': [
		'Take a vial fill it with the potion liquid after it is cooked.',
		'Quickly cap the vial, or drink it to give yourself fire breath and fire immunity.']
}

dangers['fire potion'] = {
	'A': {
		'name': 'fire dragon',
		'death': 'A fire dragon made from fire will kill you.',
		'trigger': 'Anything from the potion falls into the volcano.'},
	'B': {
		'name': 'Falling into the volcano',
		'trigger': 'You fall into the volcano.',
		'death': 'Lava.'
	},
	'C': {
		'name': 'eruption',
		'trigger': 'Geothermal events and tectonic shifts. And magic.'
		'death': 'Lava, heat, smoke, or ash.'
	},
}

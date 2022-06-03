import re

def dna_is_actg(dna):
	return bool(re.match('^[actgACTG]+$', dna))


def reverse_complement(dna):
	return dna.translate(str.maketrans('ACTGactg', 'TGACtgac'))


# Functions to use in our project.
import itertools

def parser(parents):
	"""
	This function separates a given input of Blood Group into it's constituent Alleles and Rh-factor.
	
	Input: List of blood groups.
	
	Output: Separate lists of Rh-factor and Allele type.
	"""
	rh = []
	bt = []
	for i in parents:
		if '+' in i:
			bt.append(i.replace('+',""))
			rh.append('+')
		
		elif '-' in i:
			bt.append(i.replace('-', ""))
			rh.append('-')

	return bt, rh


def dealer(type_1, type_2):
	pool = list(itertools.product(type_1, type_2))
	for i in range(len(pool)):
		if pool[i] == ('O', 'A'):
			pool[i] = ('A', 'O')
		elif pool[i] == ('O', 'B'):
			pool[i] = ('B', 'O')
		pool[i] = "".join(pool[i])
	return pool

def unique_pools(pool):
	gene_set = list(set(pool))
	blood_types = [("".join(i)) for i in gene_set]
	return blood_types

def percent_proba(blood_types, pool):
	proba_dict = {}
	for i in blood_types:
		proba_dict[i] = 100 * ((pool.count(i))/len(pool))
	return (proba_dict)

def punnett(type_1, type_2):
	"""
	This function allows the user to output a dictionary of possible combinations formed by two given blood group.

	Input:
	type_1 : Blood group 1
	type_2 : Blood group 2

	Output: Dictionary of possible derived blood types
	"""
	pool = dealer(type_1, type_2)
	blood_types = unique_pools(pool)
	answer = percent_proba(blood_types, pool)
	return answer


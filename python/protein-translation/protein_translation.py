translator = {
	'AUG' : 'Methionine',
	'UUU' : 'Phenylalanine',
	'UUC' : 'Phenylalanine',
	'UUA' : 'Leucine',
	'UUG' : 'Leucine',
	'UCU' : 'Serine',
	'UCC' : 'Serine',
	'UCA' : 'Serine',
	'UCG' : 'Serine',
	'UAU' : 'Tyrosine',
	'UAC' : 'Tyrosine',
	'UGU' : 'Cysteine',
	'UGC' : 'Cysteine',
	'UGG' : 'Tryptophan',
	'UAA' : False,
	'UAG' : False,
	'UGA' : False,
}

def codon_translate(codon):
	return translator[codon]

def rna_to_codon_list(strand):
	codons = []
	while strand:
		codons.append(codon_translate(strand[:3]))
		strand = strand[3:]
	return codons

def proteins(strand):
	protein = []
	codon_list =  rna_to_codon_list(strand)
	for codon in codon_list:
		if not codon:
			break
		protein.append(codon)

	return(protein)
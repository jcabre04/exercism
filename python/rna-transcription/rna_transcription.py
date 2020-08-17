dna_to_rna_translator = {
	'G' : 'C',
	'C' : 'G',
	'T' : 'A',
	'A' : 'U'
}

def to_rna(dna_strand):
	rna = ''
	for nucleotide in dna_strand:
		rna += dna_to_rna_translator[nucleotide]
	return rna

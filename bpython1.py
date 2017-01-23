from Bio.PDB.PDBParser import PDBParser
from Bio.PDB.parse_pdb_header import parse_pdb_header
from Bio.PDB.MMCIFParser import MMCIFParser

path = r'C:\Users\clint\Desktop\Classes\Python\temp\pymodeler\Antigens\4tvp.pdb'
path2 = r'C:\Users\clint\Desktop\Classes\Python\temp\pymodeler\Particles\1mva.pdb'
pdbParser = PDBParser()
# Creates Dictionary of molecule names pointing to a dictionary of attributes
mva = pdbParser.get_structure('1mva', path2)
print mva


quit()
fat_dict = parse_pdb_header(path)
print fat_dict
dict = fat_dict['compound']
# Output ->
# {'fragment': 'unp residues 30-505', 'molecule': 'envelope glycoprotein gp160', 'misc': '', 'engineered': 'yes', 'chain': 'g'}
# {'molecule': 'pgt122 light chain', 'misc': '', 'engineered': 'yes', 'chain': 'l'}
# {'fragment': 'unp residues 509-661', 'molecule': 'envelope glycoprotein gp160', 'misc': '', 'engineered': 'yes', 'chain': 'b'}
# {'molecule': '35o22 heavy chain', 'misc': '', 'engineered': 'yes', 'chain': 'd'}
# {'molecule': 'pgt122 heavy chain', 'misc': '', 'engineered': 'yes', 'chain': 'h'}
# {'molecule': '35o22 light chain', 'misc': '', 'engineered': 'yes', 'chain': 'e'}

ab_chains = []
for key in dict.keys():
    if 'chain' in dict[key]['molecule']:
        ab_chains.append(dict[key]['chain'])

print ab_chains
quit()

cifParser = MMCIFParser()
structure = cifParser.get_structure('1fat', '1fat.cif')

first_model = structure[0]
chain_A = first_model['A']
# res100 = chain_A[('', 100, '')]
res_100 = chain_A[100]
n = res_100['N'].get_vector()

print chain_A
# print res100
print first_model
print res_100
print n

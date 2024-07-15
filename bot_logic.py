
import random






def gen_pass(pass_length):
    elements = "+-/*!&$#?=@<>"
    password = ""
    for i in range(pass_length):
        password += random.choice(elements)
    return password
    
def gen_pass_smile():
    smiles = [":)", ":(", ">:(", ">:)", "<3", "(==3"]
    smiles_choosed = ""

    number = random.randint(0, len(smiles)-1)

    smiles_choosed += smiles[number]
    return smiles_choosed



realPasword = gen_pass(50)
realSmiles = gen_pass_smile()

print(realPasword)  
print(realSmiles)
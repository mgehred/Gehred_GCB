def read_fasta(x):
    """
    Read in a file in FASTA format    
    """
    x = input("Which .fasta file? ")
    seq = ''
    f = open(x)
    for line in f:
        line = line.strip()
        seq = seq + line
    f.close()
    return print(seq)
read_fasta('x')


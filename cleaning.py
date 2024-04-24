from random import shuffle
from Bio import SeqIO
import re 

##############################################
#####         CLEANING DATASET           #####
##############################################


def clean_dFAM(dFAM, removed_seq):
    """
    Extract sequence superfamily from dFAM.
    
    Keyword arguments:
    file -- TE dFAM sequence
    """
    family = None
    try:
        family = dFAM.split("#")[1].split("/")[1]
    except: 
        removed_seq += 1
    
    # vocabulary = ["DNA", "RC", "MITE", "LINE", "Retroposon"]
    # if any(TE in dFAM for TE in vocabulary) and "/" in dFAM:
    #     print(dFAM)
    
    return family, removed_seq
                    


def clean_plantDB(plantDB):
    """
    Extract sequence superfamily from plantDB.
    
    Keyword arguments:
    file -- TE plantDB sequence
    """
    return plantDB.split("|")[3].split(":")[1] ### for superfamily



def classification(file_seq, n_missing, minimum):
    """
    Classify all TE by their superfamily, new ID and sequence

    Keyword arguments:
    file_seq -- TE fasta file input with all db
    n_missing -- percent allowed for nucleotide missing 
    """
    seen = set()
    targets = {}
    removed_seq = 0 ### number of sequences that will be removed
    records = []
    rm_list = []
    ids = 0 ### new ID for each transposable element 
    specific_excluded_family = ["Caulimovirus", "tandem", "rice", "Evirus", "Centro", "tRNA"]   ### not Transposable element
    specific_retained_family = ["L1", "ERTBV", "MITE", "hAT", "MULE", "TcMar"]

    for dna_sequence in SeqIO.parse(f'{file_seq}', format='fasta'):
        percent_missing = (str(dna_sequence.seq).upper().count("N") / len(dna_sequence.seq))*100
        name_seq = dna_sequence.id
        if dna_sequence.seq.upper() not in seen: 
            if "unknown" not in str(name_seq).lower() and percent_missing < n_missing:    ### threshold to s% of missing nucleotide and if unknown class/ order or superfamily 
                if '|' in name_seq:  ### select PlantDB ID 
                    ids += 1
                    family = clean_plantDB(name_seq)

                elif '#' in name_seq :  ### select dFAM ID 
                    ids += 1
                    family, removed_seq = clean_dFAM(name_seq, removed_seq)

                else :
                    removed_seq += 1        ### no family identified so the sequence is deleted
                    continue 
                 
                if family is None :
                    continue
                
                try: ### same superfamily so we regroup the sequences together                
                    selection = str(family.split("-")[0])
                    
                    if family in specific_excluded_family or selection in specific_excluded_family:
                        removed_seq += 1  ### no TE superfamily
                        continue 
                    
                    if selection in '\t'.join(specific_retained_family):
                        family = family.split("-")[0]  
                        
                except:
                    pass

                seen.add(dna_sequence.seq)
                records.append([f"Seq_{ids}", str(dna_sequence.seq).upper(), family])
            else : 
                removed_seq += 1
                      
        else : 
            removed_seq += 1
        
    for seq in records :
        family = seq[2]
        if family in targets.keys(): 
            targets[family] = targets[family] + 1
        # Else we add the target to the dictionary with an initial value of 1 
        else: 
            targets[family] = 1

    print("Data information after cleaning:")
    print(f"{len(records)} sequences has been keep for the training")
    print(f"{removed_seq} sequences has been removed") 

    print("\nData summary:")

    for key, value in targets.items():
        if value >= minimum:
            print("Target = ", key, "| Number of sequences = ", value)
        else : 
            rm_list.append(key)
            records = [x for x in records if not key in x]
            
    for target in rm_list: 
        del targets[target]
        
            
    return targets, records


##############################################
##### GENERATION OF THE TRAIN/TEST SPLIT #####
##############################################


def training_split(targets, records, k):
    """
    Split training / testing sequences based on their total values by family

    Keyword arguments:
    targets -- dictionary of family and values
    records -- list with all ID, DNA sequences and superfamily from training model
    k -- size of kmer selected by user
    """
    # Initialize train/test split tables that will contain the data
    train_data, test_data = [], []
    # Initialize train/test split dictionaries that will contain the number of instances for each target
    test_split, train_split, kmers = {}, {}, {}
    test_split = test_split.fromkeys(targets.keys(), 0)
    train_split = train_split.fromkeys(targets.keys(), 0)
    
    shuffle(records) ## mix all dataset

    for seq in records:
        family = seq[2]
        threshold = int(targets[family] * (0.8))
        
        if train_split[family] < threshold: ###  inferior to 80%
            train_split[family] += 1
            train_data.append(seq)
                
        else :                             #### superior to 80%
            test_split[family] += 1 
            test_data.append(seq)

    print("\nTrain/Test split summary:\n")
    for train_key, test_key in zip(train_split.keys(), test_split.keys()):
        print("Target =", train_key, "| Train instances = ", train_split[train_key], "| Test instances = ", test_split[test_key])
    print("\nTotal number of training instances =", len(train_data))
    print("Total number of testing instances =", len(test_data))

    for seq in train_data:
    # Get the sequence
        sequence = seq[1]
        # Go through the sequence 
        for i in range(0, len(sequence) - k + 1, 1):
            # Get the current k-mer
            kmer = sequence[i:i + k]
            # If it contains only the characters "A", "C", "G" or "T", it will be saved.
            if bool(re.match('^[ACGT]+$', kmer)) == True: 
                kmers[kmer] = 0


    return train_split, test_split, train_data, test_data, kmers



##################################################
#########        MAKE THE MATRIX         #########
##################################################

def make_matrix(records, k, kmers):
    """
    Create the matrix based on kmer possibilities
    
    Keyword arguments:
    records -- list with all sequences, id and superfamily
    k -- number of kmers selected by user
    kmers -- kmer dictionary
    """
    kmer_possible = []
    ### initialization of feature and target matrices
    X = []
    y = []
    
    for seq in records : 
        x = {}  ### c'est mon vecteur pour les diff kmers
        x = x.fromkeys(kmers.keys(), 0)
        sequence = seq[1]
        family = seq[2]
        
        for i in range(len(sequence) - k +1):
            kmer = sequence[i:i + k]
            if "N" not in kmer:
                if kmer not in kmer_possible : 
                    x[kmer] = 0
                    kmer_possible.append(str(kmer))
                try :
                    x[kmer] += 1
                except:
                    continue
        X.append(list(x.values()))
        y.append(family)

    return X, y


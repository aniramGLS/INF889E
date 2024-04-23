import argparse
from cleaning import classification, training_split, make_matrix
from features import normalization, run_pca
from SVM import run_SVM
from MLP import run_MLP


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Add informations and files",
                                 formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("-f", "--fasta_file", help="add the fasta file ")
    parser.add_argument("-k", "--kmer", help="add number of kmer needed for the analysis")
    parser.add_argument("-n", "--n_missing", help="percent of missing nucleotide by sequence")
    parser.add_argument("-min", "--minimum", help="minimum of sequences")
    parser.add_argument("-pca", "--pca_plot", dest='flag_exists', help="plot PCA graph", action='store_true')
    parser.add_argument("-svm", dest='flag_exists', help="run SVM model", action='store_true')
    parser.add_argument("-mlp", dest='flag_exists', help="run MLP model", action='store_true')

    args = parser.parse_args()
    # if parser.parse_args(['-pca']) : 
    #     print("run pca")
    targets, records = classification(args.fasta_file, int(args.n_missing), int(args.minimum))
    train_split, test_split, train_data, test_data, kmers = training_split(targets, records, int(args.kmer))
    X_train, y_train = make_matrix(records = train_data, kmers = kmers, k = int(args.kmer))
    X_test, y_test = make_matrix(records = test_data, kmers= kmers, k = int(args.kmer))
    
    X_train = normalization(X_train)
    X_test = normalization(X_test)
    print("heheh")
    run_pca(X_train, y_train, train_data)
    # if parser.parse_args(['-pca']) : 
    #     print("run pca")
    #     run_pca(X_train, y_train, train_data)
    # if parser.parse_args(['-svm']) : 
    #     print("run smv")
    #     run_SVM(X_train, y_train, X_test, y_test)
    # if parser.parse_args(['-mlp']) : 
    #     print("run mlp")
    #     run_MLP(X_train, y_train, X_test, y_test)

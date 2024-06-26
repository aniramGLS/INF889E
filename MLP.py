from sklearn.metrics import confusion_matrix, classification_report
import matplotlib.pyplot as plt
from sklearn.neural_network import MLPClassifier
import numpy as np
import seaborn as sns


def run_MLP(X_train, y_train, X_test, y_test):
    """
    Training MLP model on training set and evaluation of the model
    
    Keyword arguments:
    X_train, y_train, X_test, y_test -- dataset 
    """

    model = MLPClassifier(solver='lbfgs', hidden_layer_sizes=(10, 10), activation='identity', max_iter=3000,
                            early_stopping = True, alpha= 1e-7, random_state=26)  # mlp creation model, activation function : identity, optimiser : lbfgs
                                                                        
    model.fit(X_train, y_train)     ### training model of training set
    y_prediction = model.predict(X_test)    ## prediction for testing set 
    print(model.score(X_train, y_train))
    print(classification_report(y_test, y_prediction, digits = 3))      ### classification evaluation for accurary, recall and f1 score
    c_matrix = confusion_matrix(y_test, y_prediction, labels=model.classes_)        ### confusion matrix for testing set vs prediction set 
    classification_report_dict_keys = list(classification_report(y_test, y_prediction, output_dict= True).keys())[:-3]


    fig, ax = plt.subplots(figsize=(15, 13))
    sns.heatmap(c_matrix, 
                cmap = 'viridis', 
                annot = True, 
                fmt = ".0f", 
                linewidth = 0.1, 
                xticklabels = classification_report_dict_keys, 
                yticklabels = classification_report_dict_keys)
    plt.title("Confusion matrix")
    plt.xlabel("Predicted label")
    plt.ylabel("True label")
    plt.savefig("confusion_matrix_MLP.png")

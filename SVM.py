import numpy as np
from sklearn import svm
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from sklearn.feature_selection import RFE
from sklearn.metrics import  accuracy_score, confusion_matrix, ConfusionMatrixDisplay, classification_report
from sklearn.model_selection import cross_val_score


#################################
#####    MODEL TRAINING     #####
#################################

def run_SVM(X_train, y_train, X_test, y_test, kmer):
    """
    Training SVM model on training set and evaluation of the model

    Keyword arguments:
    X_train, y_train -- training dataset
    X_test, y_test -- testing dataset
    """
    model = svm.SVC(C=7.0, kernel='linear', class_weight = None, random_state=26) ### model initialization
    model.fit(X_train, y_train)
    y_prediction = model.predict(X_test)        ### model prediction
    print(classification_report(y_test, y_prediction, digits = 3))   ### classification evaluation for all superfamily 
    c_matrix = confusion_matrix(y_test, y_prediction, labels=model.classes_)
    
    classification_report_dict_keys = list(classification_report(y_test, y_prediction, output_dict= True).keys())[:-3]

    fig, ax = plt.subplots(figsize=(15, 14))
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

    plt.savefig(f"confusion_matrix_SVM.png")         ### save confusion matrix figure

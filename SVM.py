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
    model = svm.SVC(C=7.0, kernel='linear', class_weight = None) ### model initialization
    #rfe = RFE(model, n_features_to_select = 50, step = 2)  ### feature selection initialization to keep only 200 features
    #X_train = rfe.fit_transform(X_train, y_train)       #### feature selection on training dataset
    #X_test = rfe.transform(X_test)              #### feature selection on testing dataset
    model.fit(X_train, y_train)
    y_prediction = model.predict(X_test)        ### model prediction
    print(classification_report(y_test, y_prediction, digits = 3))   ### classification evaluation for all superfamily 
    c_matrix = confusion_matrix(y_test, y_prediction, labels=model.classes_)
    figure = ConfusionMatrixDisplay(confusion_matrix=c_matrix, display_labels=model.classes_) ### plot confusion matrix graph
    
    figure.plot()   
    plt.subplots()
    plt.savefig(f"confusion_matrix_SVM_{kmer}.png")         ### save matrix figure

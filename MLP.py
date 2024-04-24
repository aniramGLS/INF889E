from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay, classification_report
import matplotlib.pyplot as plt
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import cross_val_score
from yellowbrick.model_selection import learning_curve
import numpy as np


def run_MLP(X_train, y_train, X_test, y_test): ### INITIALISATION DU MODELE
    """
    Training MLP model on training set and evaluation of the model
    """

    model = MLPClassifier(solver='lbfgs', hidden_layer_sizes=(10, 10), activation='identity', max_iter=3000,
                            early_stopping = True, alpha= 1e-7, random_state=26)  # CREATION DU MODELE MLP
                                                                        # FONCTION D'ACTIVATION : RELU
                                                                        # ALGORITHME D'OPTIMISATION : DESCENTE DE GRADIENT STOCHASTIQUE (SGD)
    model.fit(X_train, y_train)     ### training model of training set
    y_prediction = model.predict(X_test)    ## prediction for testing set 
    print(model.score(X_train, y_train))
    print(classification_report(y_test, y_prediction, digits = 3))      ### classification evaluation for accurary, recall and f1 score
    c_matrix = confusion_matrix(y_test, y_prediction, labels=model.classes_)	    ### confusion matrix for testing set vs prediction set 
    figure = ConfusionMatrixDisplay(confusion_matrix=c_matrix, display_labels=model.classes_)  
    figure.plot()   
    # plt.subplots(figsize=(15, 10))

    plt.savefig("confusion_matrix_MLP.png")

    # cross_validate = cross_val_score(model, X_train, y_test, cv=10) ### cross validatioon
    # print(cross_validate)

    #print(classification_report(y_test, y_prediction))
    #train_sizes, train_scores, test_scores, fit_times, _ = learning_curve(model, X_train, y_train, cv=10) #### learning curve visualizarion
    #plt.plot(train_sizes, np.mean(train_scores, axis=1))
    #plt.savefig("Learning_curve.png")

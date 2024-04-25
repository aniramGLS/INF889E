# INF889E PROJECT 2024

Script python développé pour le cours INF88E.
Le projet consiste à la comparaison de deux modèles de machine learning dans la détection de superfamille d'éléments transposable. Il a pour but de détecter les patterns spécifiques aux séquences des éléments transposables pour prédire et classifier la superfamille


Présentation:
| Program                       |                                       Description                                        |
|-------------------------------|:----------------------------------------------------------------------------------------:|
| Principal component analysis  |            Exploration des variations entre les différents éléments transposables        |
| Support vector machine        |                         Lance l'entraînement du modèle SVM                               |
| Multi layer perceptron        |                         Lance l'entraînement du modèle MLP                               |
 

# Table of contents
* [Prerequisites](#Prerequisites)
* [How to download the dataset](#How-to-download-the-dataset)
* [Technologies use](#Technologies-use)
* [Authors](#Authors)
* [License](#License)

## Prerequisites <a name="Prerequisites"></a>

Pour pouvoir lancer correctement ce script, il est important d'avoir ces packages suivants : 

biopython                    
matplotlib                   
numpy                        
pandas                      
scikit_learn                 
seaborn
sklearn  
h5py

## How to download dataset <a name="How-to-download-the-dataset"></a>

Les séquences d'éléments transposables ont été extraites à partir de ces différentes bases de données :  

riceTElib : https://github.com/oushujun/riceTElib  
dFAM : https://github.com/Dfam-consortium/FamDB/  
PlantLTRDB


## How to run the program <a name="How-to-run-the-program"></a>
Pour en savoir plus sur le script :
python main.py -h  

Exemple de lancement :  
python  main_mlp.py -f ../TE_total.fa -n 3 -k 5 -min 15  
-k : longueur de k-mer sélectionnée  
-n : pourcentage nucléotide manquants accepté  
-min : nombre de séquences minimum accepté par superfamille  

## Technologies use <a name="Technologies-use"></a>
Use python python/3.10.13 version or more

## Authors <a name="Authors"></a>
Autrice : Marina GOLIASSE 

## License <a name="License"></a>
Open source project.

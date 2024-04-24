# INF889E PROJECT 2024

Python script developed for the course INF889E. 
The project consist of a comparison between two machine learning models for transposable elements (TE) classification. It has as goal to detecting patterns behind DNA sequence of TE for classifying superfamily.


Présentation:
| Program                       |                                       Description                                        |
|-------------------------------|:----------------------------------------------------------------------------------------:|
| Principal component analysis  |                   Méthode de réorganisation de données : triage et regroupement          |
| Support vector machine        |          Reprends la séquence transformée et reproduit la séquence initiale              |
| Multi layer perceptron        |            Méthode de compression des séquences d'ADN en binaire puis ascii              |
 

# Table of contents
* [Prerequisites](#Prerequisites)
* [How to run the program](#How-to-run-the-program)
* [Technologies use](#Technologies-use)
* [Authors](#Authors)
* [License](#License)

## Prerequisites <a name="Prerequisites"></a>

For correctly use this script you need to install or update that library:

- tkinterdnd2
- bitarray

For correctly use this script you need to download TE dna sequences from multiple public databases
  riceTElib : https://github.com/oushujun/riceTElib
  dFAM : 
  PlantDB

# Tape in console

pip install tkinterdnd2      #Install tkinterdnd2 librairy
pip install bitarray      #Install bitarray librairy

    or

pip install tkinterdnd2 --upgrade     #Upgrade tkinterdnd2 library
pip install bitarray --upgrade         #Upgrade bitarray library
## How to run the program <a name="How-to-run-the-program"></a>
For launch program tape in console:

python3 .\main.py
## Technologies use <a name="Technologies-use"></a>
Use python 3.9.10 version and compatible with python 3.9.*

## Authors <a name="Authors"></a>
Autrice : Marina GOLIASSE 

## License <a name="License"></a>
Open source project.

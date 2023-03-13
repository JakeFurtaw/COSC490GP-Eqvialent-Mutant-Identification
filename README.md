# Automatic Equivalent Mutant Identification
We will be creating an AST based neural network model that will automatically detect equivalent mutants in a dataset.
The program and model will have the following functionality:
- ✓ Process dataset to sort java and c programs
- Parse dataset with java parser to prepare it for the AST
- Feed 70%-80% parsed data into ASTNN to train it on the dataset
- Use remaining data to test the ASTNN after training is complete
- Compute Accuracy, F1 Score, and other necessary data results using numpy
- Provide analysis to detemine success of the model

# Dataset used 
- https://b2share.eudat.eu/records/fd8e674385214fe9a327941525c31f53

# Libraries
```
https://pytorch.org/
https://code2vec.org/
https://pandas.pydata.org/
https://pypi.org/project/javalang/
https://pypi.org/project/gensim/
https://scikit-learn.org/stable/
```

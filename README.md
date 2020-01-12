# Awt M4 Evaluation
This is a simple evaluation framework used to compare the results achieved by different groups working on TU Berlin AWT (Advanced Web Technologies) project. The aim of the project is to come up with models to predict the hourly dataset provided by [M4 competition](https://github.com/M4Competition/M4-methods) organizers.

# How to use
- Add a folder under [results](https://github.com/yamen23ali/awt-m4-evaluation/tree/master/results) indicating your group name.

- Inside your group folder create a folder indicating the model name (e.g. skynet).

- Inside the created model folder create 2 folders with these exact names (Test, Holdout).

- In the created Test folder put the results of the model predictions for [Test Data](https://github.com/yamen23ali/awt-m4-evaluation/blob/master/Dataset/Test/Hourly-train.csv). In the created Holdout folder put the results of the model predictions for [Holdout Data](https://github.com/yamen23ali/awt-m4-evaluation/blob/master/Dataset/Holdout/Hourly-train.csv). 3 files with the following names should be placed in Test and Holdout folders:
  * point.csv: the points predictions.
  * lower.csv: the lower bounds predictions.
  * upper.csv: the upper bounds predictions.

- Finally run the python script:
```
python evaluate.py
```

After running the script, results of all models from all the groups will be printed. Also results of the naive model and the Smyl ( the best ahcieving model in the M4 competition) will be reported.

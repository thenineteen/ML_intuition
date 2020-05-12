# imports
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn import svm

from imports_and_functions import visualise_decision_boundary
from Data_synthesis import data_synthesis

# get data
X1, X0, X, Xdf, y1, y0, y, colours = data_synthesis()

# VISUALISE DECISION BOUNDARIES
# linear SVC
visualise_decision_boundary(svm.SVC(kernel='linear'), 'Decision boundary of SVC')

# LR C=1 (regularisation)
visualise_decision_boundary(LogisticRegression(C=1), 'Decision surface of LR C=1')

# Compare LR C=1 to the below LR C=10000 model where the decision boundary conincides with that of SVC:
visualise_decision_boundary(LogisticRegression(C=10000), 'Decision surface of LR C=10000')

import copy
import time
import re
import numpy as np
import pandas as pd
import seaborn as sns
import missingno as msn
from scipy import stats
import matplotlib.pyplot as plt
from sklearn import metrics
from sklearn.svm import SVC, SVR
from IPython.display import display
from sklearn.decomposition import PCA, KernelPCA
from scipy.stats.stats import pearsonr
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import Imputer, StandardScaler, LabelEncoder
from sklearn.neural_network import MLPRegressor, MLPClassifier
from sklearn.linear_model import LogisticRegression, LogisticRegressionCV
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.feature_selection import VarianceThreshold, chi2, RFE, SelectKBest, f_classif
from sklearn.model_selection import train_test_split, KFold, cross_val_score, cross_val_predict, GridSearchCV

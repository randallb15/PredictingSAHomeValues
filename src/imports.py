import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import glob
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
import re

from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split, KFold, StratifiedKFold, cross_val_score, GridSearchCV
from sklearn.datasets import make_classification
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier, KNeighborsRegressor
from sklearn.linear_model import LogisticRegression, LinearRegression, ElasticNet, Ridge, Lasso
from sklearn.pipeline import Pipeline
import statsmodels.api as sm
import statsmodels.formula.api as smf

from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn.ensemble import GradientBoostingClassifier, GradientBoostingRegressor
from sklearn.tree import DecisionTreeRegressor, DecisionTreeClassifier

from sklearn.metrics import mean_squared_error, r2_score, SCORERS
from sklearn.metrics import precision_recall_curve, roc_curve, confusion_matrix, classification_report,precision_score,recall_score,accuracy_score,roc_auc_score, f1_score
from sklearn.utils import resample
from sklearn.utils.class_weight import compute_class_weight
from sklearn.inspection import permutation_importance

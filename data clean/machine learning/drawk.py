import pandas as pd  #for data manipulation operations
import numpy as np  #for numeric operations on data
import seaborn as sns  #for data visualization operations
import matplotlib.pyplot as plt  #for data visualization operations
from sklearn.preprocessing import LabelEncoder # for encoding
from sklearn.preprocessing import MinMaxScaler, RobustScaler, StandardScaler #for standardization

import scipy.stats as st

from sklearn.model_selection import train_test_split, GridSearchCV, cross_val_score
from sklearn.metrics import confusion_matrix, accuracy_score, classification_report
from sklearn.metrics import accuracy_score
from sklearn.metrics import roc_auc_score, roc_curve
from sklearn.metrics import plot_confusion_matrix
from sklearn import model_selection
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import GradientBoostingClassifier

#ignore warnings
import warnings
warnings.filterwarnings("ignore")

#to see model parametres
from sklearn import set_config
set_config(print_changed_only = False)

df = pd.read_csv('processed.csv', encoding = 'gbk')
sns.set_theme(style = "whitegrid")

fig, axes = plt.subplots(1, 3, figsize=(40, 10))
sns.histplot(ax = axes[0], x = df["abv"],
             bins = 10,
             kde = True,
             color = "g").set(title = "Distribution of 'abv'");
sns.histplot(ax = axes[1], x = df["degree"],
             bins = 10,
             kde = True,
             color = "r").set(title = "Distribution of 'degree'");
sns.histplot(ax = axes[2], x = df["price"],
             bins = 10,
             kde = True,
             color = "g").set(title = "Distribution of 'price'");
plt.savefig('img1.png', dpi = 300, format = 'png')

fig, axes = plt.subplots(1, 4, figsize=(50, 10))
sns.histplot(ax = axes[0], x = df["sweet"],
             bins = 10,
             kde = True,
             color = "g").set(title = "Distribution of 'sweet'");
sns.histplot(ax = axes[1], x = df["acidity"],
             bins = 10,
             kde = True,
             color = "r").set(title = "Distribution of 'acidity'");
sns.histplot(ax = axes[2], x = df["body"],
             bins = 10,
             kde = True,
             color = "g").set(title = "Distribution of 'body'");
sns.histplot(ax = axes[3], x = df["tannin"],
             bins = 10,
             kde = True,
             color = "g").set(title = "Distribution of 'tannin'");
plt.savefig('img2.png', dpi = 300, format = 'png')

sns.pairplot(df, diag_kind = "hist", corner = True);
plt.savefig('img3.png', dpi = 500, format = 'png')

sns.set_theme(style = "whitegrid")
g = sns.JointGrid(data = df, size = 5, x = "abv", y = "price", space = 0.2)
g.plot_joint(sns.kdeplot, fill = True, thresh = 0, cmap = "seismic")
g.plot_marginals(sns.histplot, color = "#808080", alpha = 1, bins = 25);
plt.savefig('img4.png', dpi = 300, format = 'png')

sns.set_theme(style = "whitegrid")
g = sns.JointGrid(data = df, size = 5, x = "degree", y = "price", space = 0.2)
g.plot_joint(sns.kdeplot, fill = True, thresh = 0, cmap = "seismic")
g.plot_marginals(sns.histplot, color = "#808080", alpha = 1, bins = 25);
plt.savefig('img5.png', dpi = 300, format = 'png')

sns.set_theme(style = "whitegrid")
g = sns.JointGrid(data = df, size = 5, x = "sweet", y = "price", space = 0.2)
g.plot_joint(sns.kdeplot, fill = True, thresh = 0, cmap = "seismic")
g.plot_marginals(sns.histplot, color = "#808080", alpha = 1, bins = 25);
plt.savefig('img6.png', dpi = 300, format = 'png')

sns.set_theme(style = "whitegrid")
g = sns.JointGrid(data = df, size = 5, x = "acidity", y = "price", space = 0.2)
g.plot_joint(sns.kdeplot, fill = True, thresh = 0, cmap = "seismic")
g.plot_marginals(sns.histplot, color = "#808080", alpha = 1, bins = 25);
plt.savefig('img7.png', dpi = 300, format = 'png')

sns.set_theme(style = "whitegrid")
g = sns.JointGrid(data = df, size = 5, x = "body", y = "price", space = 0.2)
g.plot_joint(sns.kdeplot, fill = True, thresh = 0, cmap = "seismic")
g.plot_marginals(sns.histplot, color = "#808080", alpha = 1, bins = 25);
plt.savefig('img8.png', dpi = 300, format = 'png')

sns.set_theme(style = "whitegrid")
g = sns.JointGrid(data = df, size = 5, x = "tannin", y = "price", space = 0.2)
g.plot_joint(sns.kdeplot, fill = True, thresh = 0, cmap = "seismic")
g.plot_marginals(sns.histplot, color = "#808080", alpha = 1, bins = 25);
plt.savefig('img9.png', dpi = 300, format = 'png')

sns.set_theme(style = "whitegrid")
g = sns.JointGrid(data = df, size = 5, x = "year", y = "price", space = 0.2)
g.plot_joint(sns.kdeplot, fill = True, thresh = 0, cmap = "seismic")
g.plot_marginals(sns.histplot, color = "#808080", alpha = 1, bins = 25);
plt.savefig('img10.png', dpi = 300, format = 'png')

fig, axes = plt.subplots(1, 2, figsize=(12, 5))
axes = axes.flatten()
sns.regplot(ax = axes[0], x = "abv", y = "price", data = df);
sns.regplot(ax = axes[1], x = "degree", y = "price", data = df);
plt.savefig('img11.png', dpi = 300, format = 'png')

fig, (ax0, ax1) = plt.subplots(nrows = 1, ncols = 2, figsize = (17, 5))

hb = ax0.hexbin(df["abv"], df["price"], gridsize = 30, cmap = 'spring')
ax0.set_title("Hexagon binning")
cb = fig.colorbar(hb, ax = ax0, label = 'counts')


hb = ax1.hexbin(df["degree"], df["price"], gridsize = 30, bins = 'log', cmap = 'inferno')
ax1.set_title("With a log color scale")
cb = fig.colorbar(hb, ax = ax1, label = 'log10(N)')
plt.savefig('img12.png', dpi = 300, format = 'png')

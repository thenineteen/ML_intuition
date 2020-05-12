import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn import svm

def make_meshgrid(x, y, h=.02):
    x_min, x_max = x.min() - 1, x.max() + 1
    y_min, y_max = y.min() - 1, y.max() + 1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
                         np.arange(y_min, y_max, h))
    return xx, yy

def plot_contours(ax, clf, xx, yy, **params):
    Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)
    out = ax.contourf(xx, yy, Z, **params)
    return out

def visualise_decision_boundary(classifier,
     title):
    
    clf = classifier.fit(X, y)
    fig, ax = plt.subplots()
    # title for the plots
    title = title
    # Set-up grid for plotting.
    # X0, X1 as above
    xx, yy = make_meshgrid(X0, X1)
    ax.set_ylim(-0.01, 1.01)
    ax.set_xlim(-0.01, 1.01)
    ax.set_xticks(minor=True, ticks=[0, 0.5, 1])
    ax.set_yticks(minor=True, ticks=[0, 0.5, 1])
    ax.scatter(Xdf[0], Xdf[1],
               c=colours, cmap='RdBu',
               alpha=0.3)
    ax.set_ylabel('y = AUTOMOTOR')
    ax.set_xlabel('x = HS')
    plot_contours(ax, clf, xx, yy, cmap=plt.cm.coolwarm, alpha=0.8)
    ax.set_title(title)
    # ax.legend()
    plt.show()

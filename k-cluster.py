import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs

dataset = make_blobs(n_samples=200,centers=4,n_feature=2,cluster_std=1.6,random_state=50)
print(dataset[0])

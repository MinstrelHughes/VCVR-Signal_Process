import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
from sklearn.decomposition import FastICA, PCA

class decompose():
	def __init__(self, source):
		self.source = source
	def ICA(self, components_count):
		# ICA模型
		ica = FastICA(n_components=components_count)
		S_ = ica.fit_transform(self.source)  # 重构信号
		A_ = ica.mixing_  # 获得估计混合后的矩阵
		return S_
	def plot(self,signals,title='decomposition plot'):
		plt.figure()
		plt.title(title)
		for sig in siganls:
        	plt.plot(sig)
        plt.show()

	def low_rank():
		return "rinidie"
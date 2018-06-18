import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
from sklearn.decomposition import FastICA, PCA
from signal_filter import Filter
class decompose():
	def __init__(self, source_path):
		self.signal_filter = Filter(source_path)
		self.signal_source = (self.signal_filter.filter())
	def ICA(self, components_count):
		# ICA模型
		ica = FastICA(n_components=components_count)
		source = np.array((self.signal_source[0]))
		source = source.reshape(1,-1)
		print("source shape",source.shape)
		print(source)
		# source = np.nan_to_num(source)
		print(np.isinf(source).any())
		print(np.isnan(source).any())
		# # source = source.reshape(1,-1)
		threshold_for_bug = 0.0001
		print(threshold_for_bug)
		for i in range(len(source[0])):
			print("worinidie",source[0][i])
			if (abs(source[0][i])) < threshold_for_bug:
				source[0][i] = threshold_for_bug
		# source[source < threshold_for_bug] = threshold_for_bug
		# print(source)

		S_ = ica.fit_transform(source)  # 重构信号
		A_ = ica.mixing_  # 获得估计混合后的矩阵
		return S_
	def plot(self,signals,title='decomposition plot'):
		print("signals aa ",signals[0])
		# plt.title(title)
		# print(signals)
		# print(signals[0][0].shape)
		# plt.plot(len(sig),)
		# plt.figure()
		# for sig in signals:
		# 	plt.scatter(np.arange(len(sig)),sig)
		# 	plt.show()
	def helper(self,x):
		print("x shape is ",np.array(x).shape)
		plt.figure()
		plt.plot(np.arange(len(x)),x)
		plt.show()

	def low_rank():
		return "rinidie"

path = "/Users/luzhuoran/VCVR-Signal_Process/DATA/DataCollection2_ProfSowers_12March2018/demo_2.vhdr"
decomposition = decompose(path)
# print(decomposition.ICA(2))
decomposition.ICA(2)
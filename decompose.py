import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
from sklearn.decomposition import FastICA, PCA
from signal_filter import Filter
import copy
class decompose():
	def __init__(self, source_path):
		self.signal_filter = Filter(source_path)
		self.signal_source = (self.signal_filter.filtered_signal())
	def sk_learn_ICA(self, components_count):
		# ICA模型
		ica = FastICA(n_components=components_count)
		source = np.array((self.signal_source))
		source = source.reshape(1,-1)
		print("source shape",source.shape)
		print(source)
		# source = np.nan_to_num(source)
		print(np.isinf(source).any())
		print(np.isnan(source).any())
		# # source = source.reshape(1,-1)
		threshold_for_bug = 10
		# print(threshold_for_bug)
		# for i in range(len(source[0])):
		# 	print("worinidie",source[0][i])
		# 	if (abs(source[0][i])) < threshold_for_bug:
		# 		source[0][i] = threshold_for_bug
		source[source < threshold_for_bug] = threshold_for_bug
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
	def Fast_ICA(self,signal,iteration_max=10000,epsilon=0.01):
		max_count = iteration_max
		cirtical = epsilon
		input_signal = signal

		#demean the signal
		mean = np.mean(input_signal,axis=1)
		demean_signal = np.array([elem-i for elem,i in zip(input_signal,mean)])
		# new_mean = np.mean(demean_signal,axis=1)

		#white the signal

		Cx=np.cov(mix)    

		value,eigvector = np.linalg.eig(Cx)#计算协方差阵的特征值  
		val=value**(-1/2)*np.eye(R, dtype=float)   
		White=np.dot(val ,eigvector.T)  #白化矩阵  
  
		Z=np.dot(White,mix) #混合矩阵的主成分Z，Z为正交阵




		return demean_signal


path = "/Users/luzhuoran/VCVR-Signal_Process/DATA/DataCollection2_ProfSowers_12March2018/demo_2.vhdr"
# decomposition = decompose(path)
# # print(decomposition.ICA(2))
# decomposition.ICA(2)

alpha_filter = Filter(path)
filtered_signal = alpha_filter.filtered_signal()
# plt.figure()
# plt.plot(np.arange(len(filtered_signal[0])),filtered_signal[0])
# plt.show()
decomposition = decompose(path)
decomposition.Fast_ICA(filtered_signal)
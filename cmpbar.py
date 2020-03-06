import numpy as np
import matplotlib.pyplot as plt

# data to plot
n_groups = 4
means_haar = (90, 55, 40, 65)
means_hog = (85, 62, 54, 20)
means_cnn = (85, 45, 92, 20)
# create plot
fig, ax = plt.subplots()
index = np.arange(n_groups)
bar_width = 0.27
opacity = 1

rects1 = plt.bar(index, means_haar, bar_width,
alpha=opacity,
color='b',
label='Haarcascades')

rects2 = plt.bar(index + bar_width, means_hog, bar_width,
alpha=opacity,
color='g',
label='Hog')

rects3 = plt.bar(index + bar_width+ bar_width, means_cnn, bar_width,
alpha=opacity,
color='y',
label='CNN')

plt.xlabel('Images')
plt.ylabel('Time')

plt.xticks(index + bar_width, ('A', 'B', 'C', 'D'))
plt.legend()

plt.tight_layout()
plt.show()

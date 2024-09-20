# https://www.naftaliharris.com/blog/visualizing-k-means-clustering/
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
data = pd.read_csv('Techniques of ML/Countryclusters.csv', encoding = 'latin1')
# plt.scatter(data['longitude'],data['latitude'])
# plt.xlim(-180,180)
# plt.ylim(-90,90)
# plt.show()

x = data.iloc[:,1:3] 
# kmeans = KMeans(4)
# kmeans.fit(x)
# identified_clusters = kmeans.fit_predict(x)
# # print(identified_clusters)
# data_with_clusters = data.copy()
# data_with_clusters['Clusters'] = identified_clusters 
# plt.scatter(data_with_clusters['longitude'],data_with_clusters['latitude'],c=data_with_clusters['Clusters'],cmap='rainbow')
# plt.show()


# ----------Within-sum-of-squares---------
# wcss=[]
# for i in range(1,7):
#     kmeans = KMeans(i)
#     kmeans.fit(x)
#     wcss_iter = kmeans.inertia_
#     wcss.append(wcss_iter)

# number_clusters = range(1,7)
# plt.plot(number_clusters,wcss)
# plt.title('The Elbow title')
# plt.xlabel('Number of clusters')
# plt.ylabel('WCSS')
# plt.show()
# [p1[R,G,B] p2 p3
# p4 p5 p6
# p7 p8 p9]
#Sample 1[p1[R,G,B] p2 p3 p4 p5 p6 p7 p8 p9 ]

# -----------------------------
import numpy as np
import cv2
import matplotlib.pyplot as plt
original_image = cv2.imread("CommonStepsML/CountingObject(Task).jpg")
img=cv2.cvtColor(original_image,cv2.COLOR_BGR2RGB)
vectorized = img.reshape((-1,3)) #converts the MxNx3 image into a Kx3 matrix where K=MxN and each row is now a vector in the 3-D space of RGB.
vectorized = np.float32(vectorized) #We convert the unit8 values to float as it is a requirement of the k-means method of OpenCV.
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
# cv2.TERM_CRITERIA_EPS: This indicates that the algorithm will stop if the desired accuracy or precision is reached. 
# Specifically, if the movement of cluster 
# centroids between iterations becomes smaller than a specified threshold, the algorithm terminates.
# cv2.TERM_CRITERIA_MAX_ITER: This indicates that the algorithm will stop after a certain number of iterations 
# (even if the accuracy condition isn't met).
# 10: This value represents the maximum number of iterations the algorithm will perform. In this case, it will iterate at most 10 times.
# 1.0: This value is the accuracy threshold for the movement of the centroids 
# (when combined with cv2.TERM_CRITERIA_EPS). If the centroid movements between iterations are less than 1.0,
# the algorithm will stop, assuming it has converged.
K = 2
attempts=10
sum_of_squared,label,center=cv2.kmeans(vectorized,K,None,criteria,attempts,cv2.KMEANS_PP_CENTERS) #kMEAN++ TO CHOOSE THE OPTIMAL POSITION OF CENTEROID
# It selects the first centroid randomly from the dataset.
# Then, for each subsequent centroid, it chooses a point that is farthest from the existing centroids 
# (based on some probability distribution). This ensures that the initial centroids are spread out as much as possible.
center = np.uint8(center)
res = center[label.flatten()]
result_image = res.reshape((img.shape))
figure_size = 15
plt.figure(figsize=(figure_size,figure_size))
plt.subplot(1,2,1),plt.imshow(img)
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(1,2,2),plt.imshow(result_image)
plt.title('Segmented Image when K = %i' % K), plt.xticks([]), plt.yticks([])
plt.show()
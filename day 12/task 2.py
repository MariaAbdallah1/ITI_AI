import pandas as pd
import numpy as np

df = pd.read_csv('d:/Maria_iti/day 12/iris.csv')

features = df[['slength', 'swidth', 'plength', 'pwidth']].values

def standardize_data(data):
    mean = np.mean(data, axis=0)
    std_dev = np.std(data, axis=0)
    standardized_data = (data - mean) / std_dev
    return standardized_data

def compute_covariance_matrix(data):
    return np.cov(data, rowvar=False)

def compute_eigenvectors_covariance(cov_matrix):
    eigenvalues, eigenvectors = np.linalg.eig(cov_matrix)
    return eigenvalues, eigenvectors

def sort_eigenvectors(eigenvalues, eigenvectors):
    sorted_indices = np.argsort(eigenvalues)[::-1]
    sorted_eigenvalues = eigenvalues[sorted_indices]
    sorted_eigenvectors = eigenvectors[:, sorted_indices]
    return sorted_eigenvalues, sorted_eigenvectors

def project_data(data, eigenvectors, num_components):
    return np.dot(data, eigenvectors[:, :num_components])

standardized_features = standardize_data(features)
cov_matrix = compute_covariance_matrix(standardized_features)
eigenvalues, eigenvectors = compute_eigenvectors_covariance(cov_matrix)
sorted_eigenvalues, sorted_eigenvectors = sort_eigenvectors(eigenvalues, eigenvectors)

num_components = 2
pca_features = project_data(standardized_features, sorted_eigenvectors, num_components)

print("Original Features Shape:", features.shape)
print("PCA Features Shape:", pca_features.shape)
print("PCA Features Head:\n", pca_features[:5])
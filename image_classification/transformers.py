# -*- coding: utf-8 -*-
"""
Created on Mon Mar  1 15:01:06 2021

@author: straw
"""
from sklearn.base import BaseEstimator, TransformerMixin
import skimage
import numpy as np
from skimage.feature import hog

class RGB2GrayTransformer(BaseEstimator, TransformerMixin):
    """
    Convert an array of RGB images to grayscale
    """
    def __init__(self):
        pass
    
    def fit(self, X, y=None):
        return self
    
    def transform(self, X, y=None):
        T = np.array([skimage.color.rgb2gray(img) for img in X])
        return T

class HogTransformer(BaseEstimator, TransformerMixin):
    """
    Calculates hog features for each img
    """
    def __init__(self, y=None, orientations=9, pixels_per_cell=(8, 8), cells_per_block=(3, 3), block_norm='L2-Hys'):
        self.y = y
        self.orientations = orientations
        self.pixels_per_cell = pixels_per_cell
        self.cells_per_block = cells_per_block
        self.block_norm = block_norm
    
    def fit(self, X, y=None):
        return self
 
    def transform(self, X, y=None):
        def local_hog(X):
            orientations = self.orientations
            pixels_per_cell = self.pixels_per_cell
            cells_per_block = self.cells_per_block
            block_norm = self.block_norm
            hog_results = hog(X, orientations, pixels_per_cell, cells_per_block, block_norm)
            return hog_results
        
        try:
            return np.array([local_hog(img) for img in X])
        except:
            return np.array([local_hog(img) for img in X])
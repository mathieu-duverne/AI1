from sklearn.impute import SimpleImputer
imputer = SimpleImputer(strategy = "median")
import pandas as pd 
import numpy as np
from sklearn.model_selection import train_test_split


class Clean_and_transform_data:
    def __init__(self, df):
        self.df = df
        self.X = None
        self.len_train = None
        self.len_test = None
        

    def clean_and_transform_data(self):
        imputer.fit(self.df.iloc[:,4:5])
        self.df.iloc[:,4:5] = imputer.transform(self.df.iloc[:,4:5])

        self.df["income_cat"] = pd.cut(self.df["median_income"],
                                   bins=[0., 1.5, 3.0, 4.5, 6., np.inf],
                                   labels=[1, 2, 3, 4, 5])

        trdata, tedata = train_test_split(self.df,test_size=0.3,random_state=43)

        maxval2 = trdata['median_house_value'].max() # get the maximum value

        # training data
        trdata_upd = trdata[trdata['median_house_value'] != maxval2] 

        # testing data
        tedata_upd = tedata[tedata['median_house_value'] != maxval2]
        
        # Make a feature that contains both longtitude & latitude
        trdata_upd['diag_coord'] = ( trdata_upd['longitude'] + trdata_upd['latitude'] )         # 'diagonal coordinate', works for this coord
        
        # update test data as well
        tedata_upd['diag_coord'] = ( tedata_upd['longitude'] + tedata_upd['latitude'] )
        
        del trdata_upd['ocean_proximity']
        del tedata_upd['ocean_proximity']

        # # lets remove two of the three similar features
        
        del trdata_upd['total_bedrooms']
        del trdata_upd['total_rooms']
        del trdata_upd['median_income']
        
        del tedata_upd['total_bedrooms']
        del tedata_upd['median_income']
        del tedata_upd['total_rooms']
        self.X = pd.concat([trdata_upd, tedata_upd])
        self.len_test = len(tedata_upd)
        self.len_train = len(trdata_upd)

        y_train = trdata_upd.pop('median_house_value')
        y_test = tedata_upd.pop('median_house_value')
        # self.y = (y_train + y_test)
        return trdata_upd, y_train, tedata_upd, y_test

# X_train = trdata_upd

# X_test = tedata_upd
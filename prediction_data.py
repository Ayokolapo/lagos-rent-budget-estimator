import pandas as pd
import numpy as np
from math import sqrt
from sklearn.ensemble import RandomForestRegressor
import _pickle as cPickle
import bz2

def build_model(data):
    x_train = data[['bed','bath', 'toilet','location_rank','location', 'serviced_flag','furnish_flag','terrace_flag']]
    y_train = data['price']
    x_train = pd.get_dummies(x_train)
    model1 = RandomForestRegressor(random_state=5, max_depth=11,n_estimators= 1400)
    model1.fit(x_train,y_train)
    return model1

def predict_data(location,area,bed,serviced,terraced,furnished):
    locationrank = pd.read_csv('locationrank.csv')
    columns = ['location','bed','area']
    sample = [['0',0,'0']]
    data = pd.DataFrame(sample,columns=columns)
    data['location'] = location
    data['area'] = area
    data['bed'] = bed
    data['toilet'] = data['bed']
    data['bath'] = data['bed']
    data['location_rank'] = locationrank['location_rank'
                                       ][(locationrank['location'] == location)&
                                        (locationrank['bed'] == bed)&
                                        (locationrank['area'] == area)].iloc[0]
    if serviced == 'serviced? Yes':
        data['serviced_flag'] = 1
    else:
        data['serviced_flag'] = 0
    if terraced == 'terraced? Yes':
        data['terrace_flag'] = 1
    else:
        data['terrace_flag'] = 0
    if furnished == 'furnished? Yes':
        data['furnish_flag'] = 1
    else:
        data['furnish_flag'] = 0
    
    data = data.drop('area',axis=1)
    data = pd.get_dummies(data)
    model_locations = ['location_'+c for c in locationrank.location.unique() if c != location]
    for model_location in model_locations:
        data[model_location] = 0
     
    return data


def compressed_pickle(title, data):
    with bz2.BZ2File(title + '.pbz2', 'w') as f: 
        cPickle.dump(data, f)


def decompress_pickle(file):
    data = bz2.BZ2File(file, 'rb')
    data = cPickle.load(data)
    return data


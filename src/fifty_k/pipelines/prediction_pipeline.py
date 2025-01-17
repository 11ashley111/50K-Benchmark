# Create prediction pipeline class -> completed
# create function for load a object -> completed
# Create custom class based upon our dataset -> completed
# Create function to convert data into DataFrame with the help of DIct

import os, sys
from src.fifty_k.logger import logging
from src.fifty_k.exception import CustomException
import numpy as np
import pandas as pd
from dataclasses import dataclass
from src.fifty_k.utils import load_object


class PredictionPipeline:
    def __init__(self) :
        pass
    
    def predict(self,features):
        preprocessor_path=os.path.join('artifacts','preprocessor.pkl')
        model_path=os.path.join('artifacts','model.pkl')
        
        processor=load_object(preprocessor_path)
        model=load_object(model_path)
        
        scaled=processor.transform(features)
        pred=model.predict(scaled)
        
        return pred
    
    
class CustomClass:
    
    def __init__(self, 
                  age:int,
                  workclass:str, 
                  education_num:int, 
                  marital_status:str, 
                  occupation:str,
                  relationship:str,  
                  race:str,
                  sex:str,  
                  capital_gain:int, 
                  capital_loss:int,
                  hours_per_week:int, 
                  native_country:str):
        
        self.age = age
        self.workclass = workclass
        self.education_num = education_num
        self.marital_status = marital_status
        self.occupation = occupation
        self.relationship = relationship
        self.race = race
        self.sex = sex
        self.capital_gain = capital_gain
        self.capital_loss = capital_loss
        self.hours_per_week = hours_per_week
        self.native_country = native_country
        
    
    def get_data_as_dataframe(self):
        try:
            custom_input={
                "age":[self.age],
                "workclass": [self.workclass],
                "education_num":[self.education_num],
                "marital_status":[self.marital_status],
                "occupation":[self.occupation],
                "relationship":[self.relationship],
                "race":[self.race],
                "sex":[self.sex],
                "capital_gain":[self.capital_gain],
                "capital_loss":[self.capital_loss],
                "hours_per_week":[self.hours_per_week],
                "native_country":[self.native_country]

            }
                
            data= pd.DataFrame(custom_input)

            return data
        
        
        except Exception as e:
            raise CustomException (e,sys)
    
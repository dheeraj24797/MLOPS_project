import os
from MLOPS_project import logger
from sklearn.model_selection import train_test_split
import pandas as pd
from MLOPS_project.entity.config_entity import DataTransformationConfig

class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config
    
    def preprocess_data(self, data: pd.DataFrame) -> pd.DataFrame:
        data = data.drop(columns=['type'])

        cols_to_fill = ["fixed acidity", "volatile acidity", "citric acid", "residual sugar", "chlorides", "pH", "sulphates"]
        for col in cols_to_fill:
            data[col] = data[col].fillna(data[col].mean())

        return data

    def train_test_spliting(self):
        raw_data = pd.read_csv(self.config.data_path)
        data = self.preprocess_data(raw_data)

        # Split the data into training and test sets. (0.75, 0.25) split.
        train, test = train_test_split(data)

        train.to_csv(os.path.join(self.config.root_dir, "train.csv"),index = False)
        test.to_csv(os.path.join(self.config.root_dir, "test.csv"),index = False)

        logger.info("Splited data into training and test sets")
        logger.info(train.shape)
        logger.info(test.shape)

        print(train.shape)
        print(test.shape)
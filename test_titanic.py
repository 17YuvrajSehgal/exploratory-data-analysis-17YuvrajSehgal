# Test Cases using pytest
import pytest
import titanic as tt
import pandas as pd
from pandas.testing import assert_frame_equal

@pytest.fixture
def titanic_dataset():
    titanic_dataset = tt.TitanicAnalysis()
    return titanic_dataset

def test_load_titanic_dataset(titanic_dataset):
    df = titanic_dataset.get_dataframe()
    assert isinstance(df, pd.DataFrame)
    assert len(df) > 0

def test_head(titanic_dataset):
    assert len(titanic_dataset.get_first_rows())  == 5
    assert len(titanic_dataset.get_first_rows(3))  == 3

def test_shape(titanic_dataset):
     assert titanic_dataset.get_dataframe_shape() == (891,12)

def test_get_datatypes(titanic_dataset):
    data_types = titanic_dataset.get_dataframe_datatypes()
    assert data_types[0] == 'int64'
    assert data_types[3] == 'object'

def test_get_age_datatypes(titanic_dataset):
    data_types = titanic_dataset.get_dataframe_age_datatypes()
    assert data_types == 'float64'

def test_get_sum_missing_values(titanic_dataset):
    sum_missing = titanic_dataset.get_sum_of_missing_values()
    assert sum_missing.Age == 177
    assert sum_missing.Cabin == 687
    assert sum_missing.Embarked == 2
    assert sum_missing.Survived == 0

def test_describe(titanic_dataset):
    df = titanic_dataset.get_dataframe_stats()
    assert isinstance(df, pd.DataFrame)
    assert len(df) > 0
    assert df.shape == (8, 7)
    assert df.Survived[0] == 891.0
    assert df.Survived[1] == 0.3838383838383838


def test_transform_class(titanic_dataset):
    df = titanic_dataset.data_transform()
    df1 = df[df["class"] == "First"]
    df2 = df[df['Pclass'] == 1]
    assert_frame_equal(df1, df2)

def test_transform_adult_male(titanic_dataset):
    df = titanic_dataset.data_transform()
    df1 = df[df["adult_male"] == True]
    df2 = df[df["who"] == "man"]
    assert_frame_equal(df1, df2)

def test_transform_embark_town(titanic_dataset):
    df = titanic_dataset.data_transform()
    df1 = df[df["embark_town"] == "Cherbourg"]
    df2 = df[df["Embarked"] == "C"]
    assert_frame_equal(df1, df2)

    df1 = df[df["embark_town"] == "Queenstown"]
    df2 = df[df["Embarked"] == "Q"]
    assert_frame_equal(df1, df2)

    df1 = df[df["embark_town"] == "Southampton"]
    df2 = df[df["Embarked"] == "S"]
    assert_frame_equal(df1, df2)
 
def test_transform_alive(titanic_dataset):
    df = titanic_dataset.data_transform()
    df1 = df[df["alive"] == "0"]
    df2 = df[df["Survived"] == "no"]
    assert_frame_equal(df1, df2)
    df1 = df[df["alive"] == "1"]
    df2 = df[df["Survived"] == "yes"]
    assert_frame_equal(df1, df2)

def test_transform_alone(titanic_dataset):
    df = titanic_dataset.data_transform()
    df1 = df[df["alone"] == False]
    df2 = df[(df["Parch"] > 0) | (df["SibSp"] > 0)]
    assert_frame_equal(df1, df2)

def test_transform_fam_size(titanic_dataset):
    df = titanic_dataset.data_transform()
    df1 = df[df["family_size"] > 1]
    df2 = df[(df["Parch"] > 0) | (df["SibSp"] > 0)]
    assert_frame_equal(df1, df2)
 
def test_fare_mean(titanic_dataset):
    mean = titanic_dataset.get_dataframe_fare_mean()
    assert mean == 32.204207968574636

def test_fare_max(titanic_dataset):
    mean = titanic_dataset.get_dataframe_fare_max()
    assert mean == 512.329200

def test_75_perc(titanic_dataset):
    mean = titanic_dataset.get_dataframe_fare_75_perc()
    assert mean == 31

def test_survival_rate_by_class(titanic_dataset):
    df = titanic_dataset.data_transform()
    titanic_dataset.set_dataframe(df)
    df = titanic_dataset.survival_rate_by_class()
    assert df.First == 0.6296296296296297


#return the average survival rates based on passenger's gender
def test_survival_rate_by_gender(titanic_dataset):
    df = titanic_dataset.data_transform()
    titanic_dataset.set_dataframe(df)
    df = titanic_dataset.survival_rate_by_gender()
    assert df.female == 0.7420382165605095

    # return average survival rates based on embarkation port
def test_survival_rate_by_embark_port(titanic_dataset):
    df = titanic_dataset.data_transform()
    titanic_dataset.set_dataframe(df)
    df = titanic_dataset.survival_rate_by_embark_port()
    assert df.C == 0.5535714285714286
    
    # return survival count based on family size
def test_survival_count_by_family_size(titanic_dataset):
    df = titanic_dataset.data_transform()
    titanic_dataset.set_dataframe(df)
    df = titanic_dataset.survival_count_by_family_size()
    assert df[2] == 89

def test_cross_tabulation_class_survived(titanic_dataset):
    df = titanic_dataset.data_transform()
    titanic_dataset.set_dataframe(df)
    df = titanic_dataset.cross_tabulation_class_survived()
    assert df[0].First == 80

#TITANIC DATASET ANALYSIS

# The sinking of the RMS Titanic is one of the most infamous shipwrecks in history. 
# On April 15, 1912, during her maiden voyage, the Titanic sank after colliding with 
# an iceberg, killing 1502 out of 2224 passengers and crew. This tragedy shocked the 
# international community and led to better safety regulations for ships.

# One of the reasons that the shipwreck led to such loss of life was that there were 
# not enough lifeboats for the passengers and crew. Although there was some element of 
# luck involved in surviving the sinking, some groups of people were more likely to 
# survive than others, such as women, children, and the upper-class.

# You are asked to do an analysis of the sinking of the RMS Titanic using the Titanic dataset available in 
# Seaborn. This implementation includes tasks such as visualizing the distribution of ages of the passengers, 
# analyzing survival rates based on passenger class, analyzing survival rates based on the embarkation port, 
# and analyzing survival counts based on family size. 

#The dataset is provide under "titanic/train.csv"

#Data Dictionary
#Variable	Definition	Key
#--------------------------
#survival	Survival	    0 = No, 1 = Yes
#pclass	    Ticket class	1 = 1st, 2 = 2nd, 3 = 3rd
#sex	    Sex	
#Age	    Age in years	
#sibsp	    # of siblings / spouses aboard the Titanic	
#parch	    # of parents / children aboard the Titanic	
#ticket	    Ticket number	
#fare	    Passenger fare	
#cabin	    Cabin number	
#embarked	Port of Embarkation	    C = Cherbourg, Q = Queenstown, S = Southampton

#The titanic dataset has roughly the following types of features:

#Categorical/Nominal: Variables that can be divided into multiple categories but having no order or priority. 
#Eg. Embarked (C = Cherbourg; Q = Queenstown; S = Southampton)
#Binary: A subtype of categorical features, where the variable has only two categories. 
#Eg: Sex (Male/Female)
#Ordinal: They are similar to categorical features but they have an order(i.e can be sorted). 
#Eg. Pclass (1, 2, 3)
#Continuous: They can take up any value between the minimum and maximum values in a column. 
#Eg. Age, Fare
#Count: They represent the count of a variable. 
#Eg. SibSp, Parch

# Please, if not already done, install the libraries we need for this exercise using the following command (in your command line)
## pip install pandas numpy matplotlib seaborn pytest

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

class TitanicAnalysis():
    def __init__(self):
        self.df = self.load_dataset()

    def get_dataframe(self):
        return self.df
    
    def set_dataframe(self, df):
        self.df = df
    
    # load the Titanic dataset from the csv file "titanic/train.csv"
    def load_dataset(self):
        # ADD YOUR CODE HERE
        return 

    #display the first few rows of the dataset
    def get_first_rows(self, n = 5):
        ## ADD YOUR CODE HERE
        return 

    # return the dimensions of the dataset
    def get_dataframe_shape(self):
        ## ADD YOUR CODE HERE
        return

    # return a concise summary of a DataFrame including the index dtype and columns, non-null values and memory usage.
    ## Notice that 3 of these 11 columns in train_data have missing data for - 
    ## Age, Cabin &  Embarked. 
    def get_dataframe_information(self):
        ## ADD YOUR CODE HERE
        return 

    # return the data types of variables
    def get_dataframe_datatypes(self):
        ## ADD YOUR CODE HERE
        return 
    
    # return the data types of colum 'age'
    def get_dataframe_age_datatypes(self):
        ## ADD YOUR CODE HERE
        return 
    
    # return the sum of the missing values. Missing values are NaN in numeric arrays, None or NaN in object arrays, NaT in datetimelike.
    ## Notice that 3 of these 11 columns in train_data have missing data for - 
    ## Age, Cabin &  Embarked. We obviously cannot drop these 3 columns entirely as they could contain 
    ##useful information which may help us determine if the passenger survives or not. 
    ##We also can't drop rows containing these missing columns as they could also contain 
    ##valuable info.
    def get_sum_of_missing_values(self):
        ## ADD YOUR CODE HERE
        return 

    # return a summary statistics of the numerical variables
    # Note that only numeric columns are shown in describe() function. 
    #You can see in the o/p cell that min, max, std deviation etc get printed.
    #Examples:
    ## Mean age is 30. 
    ##The mean of the SURVIVED col shows 38% survival rate. Roughly 1 in 3 survive the Titanic
    ##Fare=0 needs investigation
    def get_dataframe_stats(self):
        ## ADD YOUR CODE HERE
        return 



    # Lets do some clearning. You must handle missing values, outliers, 
    # and inconsistencies in the dataset. 
    # 1 - We have a Cabin column with 687 out of 891 values as null so we will drop it.
    # Along with it, lets drop the columns Name and Ticket
    # 2 - Embarked has 2 missing values as null and Age 177 values. 
    # We will replace them with "S" and mean.
    def data_cleaning(self):
        df = self.df
        #Drop the unwanted (Cabin) columns
        ## ADD YOUR CODE HERE

        # Handling missing values
         ## ADD YOUR CODE HERE
        return df ## Returned cleaned dataframe

    def woman_child_or_man(self,passenger):
        age, sex = passenger
        if age < 16:
            return "child"
        else:
            return dict(male="man", female="woman")[sex]
    
    # Transforms the dataset: create new columns based on condition
    # 1 - create a new column called 'class' such that the values are the strings "First", "Second", or 'Third" when the column 'Pclass' has value 1,2,3 respectively
    # 2 - create a new column called 'who' such that the values are "woman", "man", or "child", depending on the values of the columns "Age" and "Sex". Use the function "woman_child_or_man" provided
    # 3 - create a new column called 'adult_male" such that the value is 1 when the value of the column 'who' is man
    # 4 - create a new column called 'embark_town' such that the valies are "Cherbourg", "Queenstown", or "Southampton" if the passager has 'Embarked" in "C", "Q", or "S".
    # 5 - create a new column called 'alive' such that the value are 1 if the passenger survived, and 0 otherwise
    # 6 - create a new column called 'alone' such that the values is 'True' if the person does not have any siblings / spouses or  parents / children aboard the Titanic
    # 7 - create a new column called 'family_size' by conmbining the number of siblings/spouses and parents/children and the individual
    def data_transform(self):
        df = self.df
        df["class"] =  ## ADD YOUR CODE HERE
        df["who"] =  ## ADD YOUR CODE HERE
        df["adult_male"] =  ## ADD YOUR CODE HERE
        df["embark_town"] =  ## ADD YOUR CODE HERE
        df["alive"] =  ## ADD YOUR CODE HERE
        df["alone"] =  ## ADD YOUR CODE HERE
        df["family_size"] =  ## ADD YOUR CODE HERE
        return df
        

    # return the mean of the fare prices
    def get_dataframe_fare_mean(self):
       ## ADD YOUR CODE HERE
       return 
    
    # return max of the fare prices
    def get_dataframe_fare_max(self):
       ## ADD YOUR CODE HERE
       return 
    
    # return the value that 75% of the passengers have paied as fare or less.
    def get_dataframe_fare_75_perc(self):
        ## ADD YOUR CODE HERE
        return 

    # return the cross tabulation of class and Survived (check the method crosstab)
    def cross_tabulation_class_survived(self):
        # Cross-tabulation
        ## ADD YOUR CODE HERE
        return 
    
    # return the average survival rates based on passenger class
    def survival_rate_by_class(self):
        ## ADD YOUR CODE HERE
        return 
    
    #return the average survival rates based on passenger's gender
    def survival_rate_by_gender(self):
        ## ADD YOUR CODE HERE
        return 

    # return average survival rates based on embarkation port
    def survival_rate_by_embark_port(self):
        ## ADD YOUR CODE HERE
        return 
    
    # return survival count based on family size
    def survival_count_by_family_size(self):
        ## ADD YOUR CODE HERE
        return 

    # create a bar plot to visualize the survival status of passengers
    def visualize_survival(self):
        plt.figure(figsize=(10, 6))
        ## ADD YOUR CODE HERE
        plt.xlabel('Survival Status')
        plt.ylabel('Count')
        plt.title('Survival Count')
        plt.savefig('plots/survival_count.png')
        plt.show()
   
    # create a density plot to cisualize the distribution of fair of passengers
    # Fare Distribution: The majority of passengers paid lower fares, aligning with a larger number of third-class tickets.
    def visualize_fair_distribution(self):
        plt.figure(figsize=(10, 6))
        ## ADD YOUR CODE HERE
        plt.title('Fare Distribution of Passengers')
        plt.xlabel('Fare')
        plt.ylabel('Frequency')
        plt.savefig('plots/fare_distribution.png')
        plt.show()
    
    # create a density plot to see the Age distribution in the titanic (using kdeplot)
    def vis_age_distribution(self):
        plt.figure(figsize=(10, 6))
        ## ADD YOUR CODE HERE
        plt.title('Age Distribution of Passengers')
        plt.xlabel('Age')
        plt.ylabel('Frequency')
        plt.savefig('plots/age_distribution.png')
        plt.show()
    
    # create a historgram to visualize the distribution of ages of passengers (using histplot with option kde=True)
    def visualize_age_distribution(self):
        plt.figure(figsize=(10, 6))
        ## ADD YOUR CODE HERE
        plt.title('Age Distribution of Passengers')
        plt.xlabel('Age')
        plt.ylabel('Frequency')
        plt.savefig('plots/age_distribution2.png')
        plt.show()

    # create a histogram to visualize the distribution of ages of the passengers by gender.
    def visualize_age_distribution_by_gender(self):
        plt.figure(figsize=(10, 6))
        ## ADD YOUR CODE HERE
        plt.title('Age Distribution by Gender')
        plt.savefig('plots/age_distribution_gender.png')
        plt.show()


    # create a barplot to analyze survival rates based on passenger gender.
    def vis_survival_rate_by_gender(self):
        plt.figure(figsize=(10, 6))
        ## ADD YOUR CODE HERE
        plt.title('Survival Rate by Passenger Gender')
        plt.savefig('plots/survival_by_gender.png')
        plt.show()

    # create a barplot to analyze survival rates based on passenger class and gender.
    def vis_survival_rate_by_class_and_gender(self):
        plt.figure(figsize=(10, 6))
        ## ADD YOUR CODE HERE
        plt.title('Survival Rate by Passenger Class and Gender')
        plt.savefig('plots/survival_by_gender_class.png')
        plt.show()
    
    # create a countplot to analyze survival rates based on class.
    def vis_survival_rate_by_class(self):
        plt.figure(figsize=(10, 6))
        ## ADD YOUR CODE HERE
        plt.title('Survival Count based on Class')
        plt.savefig('plots/survival_by_class.png')
        plt.show()
        
    # create a countplot to analyze survival rates based on embarkation port.
    def vis_survival_rate_by_embarkation(self):
        plt.figure(figsize=(10, 6))
        ## ADD YOUR CODE HERE
        plt.title('Survival Count based on Embarkation Port')
        plt.savefig('plots/survival_by_embarkation.png')
        plt.show()

    
    # create a countplot to visualize the survival count based on the family size.
    def vis_survival_rate_by_family_size(self):
        plt.figure(figsize=(10, 6))
        ## ADD YOUR CODE HERE
        plt.title('Survival Count based on Family Size')
        plt.savefig('plots/survival_by_fam_size.png')
        plt.show()


    # create box plot to visualize the shows the fare distribution and survived
    def vis_fare_distribution_by_passenger_survival(self):
        plt.figure(figsize=(10, 6))
        ## ADD YOUR CODE HERE
        plt.xlabel('Survival Status')
        plt.ylabel('Fare')
        plt.title('Survival Status vs. Fare')
        plt.savefig('plots/fare_dist_by_surv.png')
        plt.show()
    
    # create a boxplot to shows the fare distribution by passenger class and survival
    def vis_fare_distribution_by_passenger_class_and_survival(self):
        plt.figure(figsize=(10, 6))
        ## ADD YOUR CODE HERE
        plt.ylim(0, 300)  # Limiting y-axis to 300 for better visualization
        plt.title('Fare distribution by Passenger Class and Survival')
        plt.savefig('plots/fare_dist_by_class_surv.png')
        plt.show()
    
     
    # create scatter plot to visualize the relationship between fare and age
    def vis_relationship_fare_and_age(self):
        plt.figure(figsize=(10, 6))
        ## ADD YOUR CODE HERE
        plt.xlabel('Age')
        plt.ylabel('Fare')
        plt.title('Age vs. Fare')
        plt.savefig('plots/scatter_age_fare.png')
        plt.show()

   
   
    
    
    

    
    

    

   






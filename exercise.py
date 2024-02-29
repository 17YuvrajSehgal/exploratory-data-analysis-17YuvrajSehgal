
import titanic as tt

titanic = tt.TitanicAnalysis()
df = titanic.get_dataframe()

print('Dataframe First Rows:')
print(titanic.get_first_rows())
print('----------------------------------------------\n')

print('Dataframe Shape:')
print(titanic.get_dataframe_shape())
print('----------------------------------------------\n')

## Notice that 3 of these 11 columns in train_data have missing data for - 
## Age, Cabin &  Embarked. 
print('Dataframe Info:')
print(titanic.get_dataframe_information())
print('----------------------------------------------\n')

print('Dataframe Datatypes:')
print(titanic.get_dataframe_datatypes())
print('----------------------------------------------\n')

print('Dataframe Datatype for Age:')
print(titanic.get_dataframe_age_datatypes())
print('----------------------------------------------\n')
        
    
## Notice that 3 of these 11 columns in train_data have missing data for - 
## Age, Cabin &  Embarked. We obviously cannot drop these 3 columns entirely as they could contain 
##useful information which may help us determine if the passenger survives or not. 
##We also can't drop rows containing these missing columns as they could also contain 
##valuable info.

print('Dataframe Missing Values:')
print(titanic.get_sum_of_missing_values())
print('----------------------------------------------\n')

# Summary statistics of the numerical variables
# Note that only numeric columns are shown in describe() function. 
#You can see in the o/p cell that min, max, std deviation etc get printed.
#Examples:
## Mean age is 30. 
##The mean of the SURVIVED col shows 38% survival rate. Roughly 1 in 3 survive the Titanic
##Fare=0 needs investigation
print('Dataframe Stats:')
print(titanic.get_dataframe_stats())
print('----------------------------------------------\n')

# Lets do some clearning. You must handle missing values, outliers, 
# and inconsistencies in the dataset. 
# 1 - We have a Cabin column with 687 out of 891 values as null so we will drop it.
# Along with it, lets drop the columns Name and Ticket
# 2 - Embarked has 2 missing values as null and Age 177 values. 
# We will replace them with suitable mode and mean.print('Dataframe After Cleaning:')
df = titanic.data_cleaning()
titanic.set_dataframe(df)
print('Dataframe After Cleaning:')
print(titanic.get_first_rows())
print('----------------------------------------------\n')

print('Dataframe Missing Values After Cleaning:')
print(titanic.get_sum_of_missing_values())
print('----------------------------------------------\n')

# Transforms the dataset: create new columns based on condition
# 1 - create a new column called 'class' such that the values are the strings "First", "Second", or 'Third" when the column 'Pclass' has value 1,2,3 respectively
# 2 - create a new column called 'who' such that the values are "woman", "man", or "child", depending on the values of the columns "Age" and "Sex". Use the function "woman_child_or_man" provided
# 3 - create a new column called 'adult_male" such that the value is 1 when the value of the column 'who' is man
# 4 - create a new column called 'embark town' such that the valies are "Cherbourg", "Queenstown", or "Southampton" if the passager has 'Embarked" in "C", "Q", or "S".
# 5 - create a new column called 'alive' such that the value are 1 if the passenger survived, and 0 otherwise
# 6 - reate a new column called 'alone' such that the values is 'True' if the person does not have any siblings / spouses or  parents / children aboard the Titanic
   
df = titanic.data_transform()
titanic.set_dataframe(df)
print('Dataframe After Transformation:')
print(titanic.get_first_rows())
print('----------------------------------------------\n')


print('The mean of the fare prices:')
print(titanic.get_dataframe_fare_mean())
print('----------------------------------------------\n')
 
print('The max of the fare prices:')
print(titanic.get_dataframe_fare_max())
print('----------------------------------------------\n')
    
# You got the mean and max values of the fare. 
# It is know that some passenger paid a lot of money for their tickets, while most of them paid a much cheaper fare
# 75% of the passengers have paied this value or less. What is the value?
print('The max of the fare prices:')
print(titanic.get_dataframe_fare_75_perc())
print('----------------------------------------------\n')
   
print('Survival rates based on passenger class:')
#Findings: Passenger Class: First-class passengers had a higher survival rate, indicating socio-economic status played a role in survival chances.
print(titanic.survival_rate_by_class())
print('----------------------------------------------\n')


print('Survival rates based on passenger gender:') 
#Findings: Gender and Survival: Women had a significantly higher survival rate than men.
print(titanic.survival_rate_by_gender())
print('----------------------------------------------\n')

print('Survival rates based on embarkation port')
#Findings: #Embarkation Port: The survival count varied based on the embarkation port, potentially reflecting the socio-economic distribution of passengers from these ports.
print(titanic.survival_rate_by_embark_port())
print('----------------------------------------------\n')
     
print('Survival count(sum) based on family size')
print(titanic.survival_count_by_family_size())
print('----------------------------------------------\n')

print('Cross tabulation to examine relationships between class and survived')
print(titanic.cross_tabulation_class_survived())
    

# create a bar plot to visualize the survival status of passengers
titanic.visualize_survival()
   
# create a density plot to cisualize the distribution of fair of passengers
# Fare Distribution: The majority of passengers paid lower fares, aligning with a larger number of third-class tickets.
titanic.visualize_fair_distribution()
    
# create a density plot to see the Age distribution in the titanic (using kdeplot)
titanic.vis_age_distribution()
    
# create a historgram to visualize the distribution of ages of passengers (using histplot with option kde=True)
titanic.visualize_age_distribution()

# create a histogram to visualize the distribution of ages of the passengers by gender.
titanic.visualize_age_distribution_by_gender()

# create a barplot to analyze survival rates based on passenger gender.
titanic.vis_survival_rate_by_gender()

# create a barplot to analyze survival rates based on passenger class and gender.
titanic.vis_survival_rate_by_class_and_gender()
    
# create a countplot to analyze survival rates based on class.
titanic.vis_survival_rate_by_class()
        
# create a countplot to analyze survival rates based on embarkation port.
titanic.vis_survival_rate_by_embarkation()
  
# create a countplot to visualize the survival count based on the family size.
titanic.vis_survival_rate_by_family_size()

# create box plot to visualize the shows the fare distribution and survived
titanic.vis_fare_distribution_by_passenger_survival()
    
# create a boxplot to shows the fare distribution by passenger class and survival
titanic.vis_fare_distribution_by_passenger_class_and_survival()
    
# create scatter plot to visualize the relationship between fare and age
titanic.vis_relationship_fare_and_age()














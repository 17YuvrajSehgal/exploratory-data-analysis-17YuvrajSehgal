[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-718a45dd9cf7e7f842a935f5ebbe5719a5e09af4491e668f4dbf3b35d5cca122.svg)](https://classroom.github.com/online_ide?assignment_repo_id=14097605&assignment_repo_type=AssignmentRepo)
# PRACTICAL ASSIGNMENT 05: Exploratory Data Analysis


The sinking of the RMS Titanic is one of the most infamous shipwrecks in history. On April 15, 1912, during her maiden voyage, the Titanic sank after colliding with 
an iceberg, killing 1502 out of 2224 passengers and crew. This tragedy shocked the international community and led to better safety regulations for ships.

One of the reasons that the shipwreck led to such loss of life was that there were 
not enough lifeboats for the passengers and crew. Although there was some element of luck involved in surviving the sinking, some groups of people were more likely to survive than others, such as women, children, and the upper-class.

You are asked to do an analysis of the sinking of the RMS Titanic. This implementation includes tasks such as visualizing the distribution of ages of the passengers, analyzing survival rates based on passenger class, analyzing survival rates based on the embarkation port, and analyzing survival counts based on family size. 

The dataset is provide under "titanic/train.csv"

Data Dictionary

|Variable|	Definition|	Key|
|--------|------------|-------|
|Survived|	Survival|	    0 = No, 1 = Yes|
|Pclass|	    Ticket class|	1 = 1st, 2 = 2nd, 3 = 3rd|
|Sex|	        Sex||	
|Age|	        Age in years||	
|SibSp|	    # of siblings / spouses aboard the Titanic||	
|Parch|	    # of parents / children aboard the Titanic||	
|Ticket|	    Ticket number||	
|Fare|	    Passenger fare||	
|Cabin|	    Cabin number||	
|Embarked|	Port of Embarkation|C = Cherbourg, Q = Queenstown, S = Southampton|

Please, if not already done, install the libraries we need for this exercise using the following command (in your command line)

`pip install pandas numpy matplotlib seaborn pytest`

Exercise:

- Please implement all methods in titanic.py file
- You can see if your implementation is working using the file exercise.py
- You can test your implementatin using the test_titanic.py file and pytest.

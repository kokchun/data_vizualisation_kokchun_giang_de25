# In-class Exercise - Power BI Semantic Model

In this exercise, you are going to create a semantic model from the csv files of bike orders. The data come from Kaggle ([link](https://www.kaggle.com/datasets/dillonmyrick/bike-store-sample-database?select=orders.csv)). 

You will use three csv files: *orders.csv*, *staffs.csv* and *stores.csv*. You can find these files under this repo under the subfolder *data*.

## 1. Create a Semantic Model
Create a new workspace and semantic model by using the three csv files. 

After this task, you should see that in your new workspace, there will be a semantic model with three separate tables.

## 2. Set Up Relationships
Check out the ER diagram on Kaggle and set up relationships between the three tables. How many relationships will you create?

After this task, you should see that your semantic model contains three connected tables. 

## 3. Add Measures
Create measures for the following on the *orders* table:
- total number of row in the *orders* table
- total number of distinct orders 
- total number of distinct stores that have had orders 
- total number of distinct staffs that have handled orders
- total number of distinct orders that are completed
  
>[!TIP]
>You can use the DAX function *DISTINCTCOUNT()*



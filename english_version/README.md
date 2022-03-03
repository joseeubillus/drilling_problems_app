# Software Development for Evaluation of Drilling Problems in Wells at Sacha Field.
## Abstract
The Sacha field is located in the Ecuadorian province of Orellana, it is part of Block 60 and is considered one of the most important in Ecuador because it registers a high daily production of hydrocarbons. Due to this, it is necessary to identify the type of drilling problems that occur in the field, their origin, and consequences, in order to correct such setbacks to reduce non-productive times and optimize the drilling of hydrocarbon wells in this field.

For this investigation, the final reports of drilling and fluids prepared between 2014 and 2019 of different wells in the Sacha field were used. From the data extracted from the reports, statistical analysis was applied, to elaborate a clean data matrix that allows to implement principal component analysis for the reduction of dimensions and understanding the relationship of the variables in a two-dimensional plane.

Finally, a classification model based on artificial intelligence was built, where 82% accuracy was achieved when predicting drilling problems in well drilling operations, which allows us to anticipate new scenarios of occurrence of problems and to act with possible engineering solutions.

## What was done to develop the software?
In the development of this tool, different methodologies were used to execute a data analysis project, which are listed below:

1. Exploratory Data Analysis
2. Principal Component Analysis
3. Supervised Learning: K Nearest Neighbors
4. Frontend Development

The detailed steps made in this research can be found in the [Jupyter Notebook](https://github.com/pizzio98/drilling_problems_app/blob/main/english_version/Research_Methodology.ipynb).

## ¿Cómo utilizar la herramienta computacional?
With the model trained, we developed a tool published in [Streamlit Share](https://share.streamlit.io/pizzio98/drilling_problems_app/main/spanish_version/app_tesis.py).
Once inside the tool, we proceed to upload the [test file](https://github.com/pizzio98/drilling_problems_app/blob/main/spanish_version/Set%20de%20prueba%20Streamlit.xlsx) uploaded in the spanish version of this research

Once the file is upload, we can show the predictions of the model and the solutions established to solve the problem.

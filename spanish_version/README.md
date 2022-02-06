# Desarrollo de una herramienta computacional de evaluación de problemas operacionales en la perforación de pozos en el campo sacha
## Descripción del problema
El campo Sacha se ubica en la provincia de Orellana del Oriente ecuatoriano, forma parte del Bloque 60 siendo considerado uno de los más importantes en Ecuador debido a que registra una alta producción diaria de hidrocarburos. Debido a ello, es necesario identificar las clases de problemas operacionales en la perforación que ocurren en el campo, su origen y consecuencias, para corregir dichos contratiempos con el objetivo de disminuir tiempos no productivos y optimizar la perforación de pozos de hidrocarburos en el campo. 

Para este trabajo se utilizó los reportes finales de perforación y fluidos de perforación elaborados entre los años 2014 y 2019 de diferentes pozos del campo Sacha. A partir de los datos extraídos de los reportes, se aplicó análisis estadístico para elaborar una matriz limpia de datos que permita implementar análisis de componentes principales para la reducción de dimensiones y comprensión de la relación de las variables en un plano bidimensional. 

Finalmente, se construyó un modelo de clasificación basado en inteligencia artificial, donde se alcanzó un 82% de exactitud al predecir problemas en la perforación de pozos, que permite anticipar nuevos escenarios de ocurrencia de problemas operacionales y actuar con las posibles soluciones de ingeniería
## ¿Qué se hizo para desarrollar la herramienta computacional?
En el desarrollo de esta herramienta se utilizaron diferentes metodologías para ejecutar un proyecto de análisis de datos, los cuáles se enumeran a continuación:

1. Análisis exploratorio de datos
2. Análisis de componentes principales
3. Aprendizaje supervisado - K Nearest Neighbors
4. Desarrollo Frontend de la herramienta

Los pasos completos efectuados en la investigación se encuentran en el [Jupyter Notebook](https://github.com/pizzio98/drilling_problems_app/blob/main/spanish_version/METODOLOG%C3%8DA_TESIS_SECCIONADO.ipynb)
## ¿Cómo utilizar la herramienta computacional?
Con el modelo entrenado, se desarrolló una herramienta computacional la cual se encuentra publicada para el uso en [Streamlit]()

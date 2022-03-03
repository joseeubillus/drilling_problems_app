import streamlit as st
import pandas as pd
import plotly.express as px
import pickle
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report,confusion_matrix, ConfusionMatrixDisplay

st.set_page_config(
    page_title="Drilling Problems Evaluation Tool",
    page_icon="📱",
    layout="wide",
)


st.markdown("# Drilling Problems Evaluation at the Sacha Field")
st.markdown("**Authors:** José Ubillús y Wilson Pacheco")
st.markdown("**Director:** MSc. Diego Cuzco")
st.markdown("**Co - Director:** PhD. José Luis Rivera")
st.subheader("Upload and data visualization")
#upload the database
archivo=st.file_uploader("Choose the file which you want to evaluate possible drilling problems and solutions")
if archivo is None:
		st.write("Upload an Excel file(.xlsx)")
else:
	X_test = pd.read_excel(archivo)
	check_database=st.checkbox("Show parameters dataframe",value=False)
	if check_database==True:
		st.dataframe(X_test,width=2000)

	#methodoology
	feature_names=X_test.columns
	from sklearn.preprocessing import scale 
	from sklearn import decomposition 
	x_scale=scale(X_test)
	x_scale=pd.DataFrame(x_scale, columns=feature_names)
	pca=decomposition.PCA(n_components=8)
	pca.fit(x_scale)
	scores=pca.transform(x_scale)
	scores_df=pd.DataFrame(scores,columns=["PC1","PC2","PC3","PC4","PC5","PC6","PC7","PC8"])
	check_database_1=st.checkbox("Show Principal Component Analysis",value=False)
	if check_database_1==True:
		col1, col2=st.beta_columns([1,1])
		with col1:
			st.write("")
			st.write("")
			st.write("")
			st.write("")
			st.dataframe(scores_df)
		with col2:
			fig=px.scatter(x=scores_df["PC1"],y=scores_df["PC2"],title="Principal Component Analysis")
		#st.image("PCA problema sub.png")
			st.plotly_chart(fig)
			
	#upload pickle model from jupyter
	
	check_database_2=st.checkbox("Show drilling problems predictions",value=False)
	loaded_model = pickle.load(open("spanish_version/modelo_finalizado.sav", 'rb'))
	y_pred=loaded_model.predict(scores_df)
	y_df=pd.DataFrame(y_pred)
	resultados=pd.concat([X_test['md, ft'],y_df],axis=1)
	resultados.rename(columns={0:"Predicted problem"},inplace=True)
	fig=px.scatter(x=scores_df["PC1"],y=scores_df["PC2"],color=resultados["Predicted problem"],title="Drilling Problem Predictions",labels={"x":"PC1","y":"PC2","color":"Drilling Problem"})
	if check_database_2==True:
		st.subheader("Results")
		col3,col4=st.beta_columns([1,1])
		with col3:
			st.dataframe(resultados)
		with col4:
			st.plotly_chart(fig)
			
		st.subheader('Posibles soluciones de ingeniería')
		soluciones_boton = st.button('Soluciones en español')
		if "load_state" not in st.session_state:
    			st.session_state.load_state = False
			
		if soluciones_boton or st.session_state.load_state:
			st.session_state.load_state = True
			soluciones=st.selectbox('Seleccione el problema operacional',('Broca Embolada','Pega Mecánica','Pega Diferencial','Pérdida de Circulación','Patadas','Taponamiento del Flowline'))
			if soluciones=='Broca Embolada':
				st.markdown('''
				- Aumentar la RPM para hacer girar más a los recortes alrededor de la broca y aumentar
				la tasa de flujo hacia la máxima permitida para limpiar la broca
				- Disminuir el WOB para permitir la limpieza efectiva de la broca evitando nuevos casos
				de embolamiento
				- Bombear una píldora dispersa para aflojar el material embolado haciendo que la litología se vuelva más arenosa
				- Bombear píldora de alta viscosidad para intentar sacar los recortes
				- Reciprocar y sacudir la broca para intentar limpiarla de los recortes adheridos''')
			elif soluciones=='Pega Mecánica':
				st.markdown('''
				- Falta de limpieza del hoyo o derrumbe de la formación se procede a rotar, mover hacia arriba o abajo la sarta de 
				perforación e incrementar el caudal sin exceder la máxima Densidad Equivalente de Circulación
				- Presencia de lutita plástica se procede a un aumento en el peso del lodo
				- Presencia de lutita reactiva se procede a bombear una píldora con inhibidores químicos que evite el hinchamiento de estas, 
				evitando así su derrumbe''')
			elif soluciones=='Pega Diferencial':
				st.markdown('''
				- Reducir el peso de la columna hidrostática mediante dilución, gasificación por nitrógeno o colocar un packer sobre el punto atascado
				para aislar la zona y remover el efecto de sobre balance
				- Lavar la tubería atascada colocando un bache de aceite que permita bañar la zona de la pegadura''')
			elif soluciones=='Pérdida de Circulación':
				st.markdown('''
				- Bombear píldoras de sellado en la zona donde se está produciendo la pérdida de circulación
				- Para evitar la pérdida excesiva de fluido se debe reducir el peso del lodo disminuyendo el diferencial de presión y a su vez reducir la tasa
				de circulación
				- En caso de que estas soluciones no den resultados, se puede optar por el bombeo de cemento en la zona fracturada para buscar sellar la formación''')
			elif soluciones== 'Patadas':
				st.markdown('''
				- Controlar el pozo mediante el aumento de la densidad del lodo para aumentar la presión hidrostática y así evitar el flujo de fluidos desde el reservorio hacia superficie''')
			elif soluciones== 'Taponamiento del Flowline':
				st.markdown('''
				- Parar la perforación, manteniendo el flujo de ser posible y limpiar la línea taponada
				- Bombear el lodo desde el stand pipe directamente al flowline para limpiarla''')
		
		else:
			solutions=st.selectbox('Seleccione el problema operacional',('Bit Balling','Mechanical Sticking','Differential Sticking','Loss of Circulation','Kicks','Flowline Plugging'))
			if solutions=='Bit Balling':
				st.markdown('''
				- Aumentar la RPM para hacer girar más a los recortes alrededor de la broca y aumentar
				la tasa de flujo hacia la máxima permitida para limpiar la broca
				- Disminuir el WOB para permitir la limpieza efectiva de la broca evitando nuevos casos
				de embolamiento
				- Bombear una píldora dispersa para aflojar el material embolado haciendo que la litología se vuelva más arenosa
				- Bombear píldora de alta viscosidad para intentar sacar los recortes
				- Reciprocar y sacudir la broca para intentar limpiarla de los recortes adheridos''')
			elif solutions=='Mechanical Sticking':
				st.markdown('''
				- Falta de limpieza del hoyo o derrumbe de la formación se procede a rotar, mover hacia arriba o abajo la sarta de 
				perforación e incrementar el caudal sin exceder la máxima Densidad Equivalente de Circulación
				- Presencia de lutita plástica se procede a un aumento en el peso del lodo
				- Presencia de lutita reactiva se procede a bombear una píldora con inhibidores químicos que evite el hinchamiento de estas, 
				evitando así su derrumbe''')
			elif solutions=='Differential Sticking':
				st.markdown('''
				- Reducir el peso de la columna hidrostática mediante dilución, gasificación por nitrógeno o colocar un packer sobre el punto atascado
				para aislar la zona y remover el efecto de sobre balance
				- Lavar la tubería atascada colocando un bache de aceite que permita bañar la zona de la pegadura''')
			elif solutions=='Loss of Circulation':
				st.markdown('''
				- Bombear píldoras de sellado en la zona donde se está produciendo la pérdida de circulación
				- Para evitar la pérdida excesiva de fluido se debe reducir el peso del lodo disminuyendo el diferencial de presión y a su vez reducir la tasa
				de circulación
				- En caso de que estas soluciones no den resultados, se puede optar por el bombeo de cemento en la zona fracturada para buscar sellar la formación''')
			elif solutions== 'Kicks':
				st.markdown('''
				- Controlar el pozo mediante el aumento de la densidad del lodo para aumentar la presión hidrostática y así evitar el flujo de fluidos desde el reservorio hacia superficie''')
			elif solutions== 'Flowline Plugging':
				st.markdown('''
				- Parar la perforación, manteniendo el flujo de ser posible y limpiar la línea taponada
				- Bombear el lodo desde el stand pipe directamente al flowline para limpiarla''')
			     
			     

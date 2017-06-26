import numpy as np

#Construyemos los datos  para entrenar nuestro modelp


#Datos de entrada
def get_X_train_data():
	return np.array( [ [1,1,0,0,0,0,0,0,0,0,0,0],
		              [1,0,0,1,0,0,0,0,0,0,0,0],
		              [0,1,0,0,1,0,0,0,0,0,0,0],
		              [0,1,0,0,0,0,1,0,0,0,0,0],
		              [0,1,1,0,0,0,0,0,0,0,0,0],
		              [0,0,0,0,1,0,0,0,0,0,1,0],
		              [0,0,0,0,0,0,0,0,0,0,1,1],
		              [0,0,0,0,1,1,0,0,0,0,0,0],
		              [0,0,0,1,1,0,0,0,0,0,0,0],
		              [0,0,0,0,0,0,1,1,0,0,0,0],
		              [0,0,0,1,0,0,1,0,0,0,0,0],
		              [0,0,0,0,0,0,0,0,1,0,1,1],
		              [0,0,0,0,0,0,0,0,1,1,0,0]]
		              )

#Datos de salida
def get_Y_train_data():
	return np.array([1,0,1,1,0,1,1,0,0,0,1,1,0])

# Preparamos Datos de prueba

def Train_Data():
	str1 ="Today I am going to play."
	str2 ="What are you playing?"
	str3= "Not sure , but some guy is comming"
	str4 ="he needs fire for cigarettes"
	str5 = "ooh I was afraid, but a girl came as well"
	str6 ="it seems she has a gun, ooh she is a police"
	return np.array([getEntryData(str1),getEntryData(str2),getEntryData(str3)
					,getEntryData(str4),getEntryData(str5),getEntryData(str6)])




# Este metodo nos permite convertir los resultados de las predicciones de nuestro modelo en valores binarios 
# Ya que las predicciones suelen ser valores entre 0 y 1
def ConvertToBynary(vect):
	for i in xrange(len(vect)):
		if(vect[i]<0.5):
			vect[i]=0
		else:
			vect[i]=1
	return vect




#Aqui construyemos  nuestros datos de entrada a partir de un texto
def getEntryData(stringData):
	data =np.array([0,0,0,0,0,0,0,0,0,0,0,0])
	lowcase= stringData.lower()
	wordList = lowcase.split(".")
	empty = " "
	wordList = empty.join(wordList)
	wordList =lowcase.split(",")
	wordList = empty.join(wordList)
	wordList =lowcase.split("?")
	wordList = empty.join(wordList)
	wordList =lowcase.split(" ")


	if('bomb' in wordList):
		data[0]=1
	if('fire' in wordList):
		data[1]=1
	if('fireplace' in wordList):
		data[2]=1
	if('girl' in wordList):
		data[3]=1
	if('gun' in wordList):
		data[4]=1
	if('guy' in wordList):
		data[5]=1
	if('acid' in wordList):
		data[6]=1
	if('hydrochloric' in wordList):
		data[7]=1
	if('kalash' in wordList):
		data[8]=1
	if('clip' in wordList):
		data[9]=1
	if('bullet' in wordList):
		data[10]=1
	if('play' in wordList):
		data[11]=1
	return data
 
# Aqui saltamos  la alerta danger si la salida de  nuestro modelo vale 1

def setDataClass(val):
	if (val==1):
		return 'Danger'
	else:
		return 'No Danger'




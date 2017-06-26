# KerasDeepLearning

En este proyecto tratamos de solucionar el problema siguiente:
   Por motivos de seguridad , un govierno decide analizar el contenidod de comunicaciones para detectar emails peligrosos.
   Para ello, establece una lista de palabras consideradas como recurentes en conversaciones de terroristas.
   En este proyecto, eligimos 12 palabras como viene presentado en la tabla siguiente:
   -------------------------------------------------------------------------------------------------
   bomb	| fire	|fireplace	|girl |	gun	|guy	|acid	|hydrochloric	|kalash	|clip	|bullet	|play	|danger
   ---------------------------------------------------------------------------------------------------
    1	1	0	0	0	0	0	0	0	0	0	0	1
    1	0	0	1	0	0	0	0	0	0	0	0	0
    0	1	0	0	1	0	0	0	0	0	0	0	1
    0	1	0	0	0	0	1	0	0	0	0	0	1
    0	1	1	0	0	0	0	0	0	0	0	0	0
    0	0	0	0	1	0	0	0	0	0	1	0	1
    0	0	0	0	0	0	0	0	0	0	1	1	1
    0	0	0	0	1	1	0	0	0	0	0	0	0
    0	0	0	1	1	0	0	0	0	0	0	0	0
    0	0	0	0	0	0	1	1	0	0	0	0	0
    0	0	0	1	0	0	1	0	0	0	0	0	1
    0	0	0	0	0	0	0	0	1	0	1	1	1
    0	0	0	0	0	0	0	0	1	1	0	0	0
   --------------------------------------------------------------------------------------------------------
   El valor 1 indica que la palabre correspondiente aparece en el email.
   La ultima columna de la tabla "Danger" nos indica si el email esta clasificado como peligroso "1" o no "0"
   
  El resultado de nuestro modelo(Clasificacion binaria con perceptron multicapas) ha tenido una puntuacion de 67%.
  
  Se podria mejorar el modelo .Este es solo una demostración.
   

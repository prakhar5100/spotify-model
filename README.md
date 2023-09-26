# spotify-model
This model recommend songs on basis of energy level of a song from spotify. To use this visit this link : http://prakhar5100.pythonanywhere.com/

The core back-end of this model is a python function. In this function we first input a song's name and it's artist and use it to receive energy level of the particular song. 
To derive that we use a python library named "spotipy" and use Client ID and Client Secret from Spotify for Developers to get song attributes. 
Next we create a database of song with different energy values, I have put only 27 songs in my database. 
Now, our function checks energy difference of the input songs and the songs given in database, if the difference is less than or equal to 0.1, the song is stored in an array along with details and the array is returned. 
Thus, the user gets similar energy range songs.
Next, I use Flask to convert my program in a web application. 
To host the flask app, I use pythonanywhere which lets limited hosting free. 

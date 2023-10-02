#Spotify Energy-Based Song Recommendation Model

This model is designed to provide song recommendations based on the energy level of songs from Spotify. To access and utilize this model, please visit the following link: 

[Spotify Energy-Based Song Recommendation.
](http://prakhar5100.pythonanywhere.com/)

The core functionality of this model is implemented as a Python function. This function takes as input the name of a song and its artist, and then retrieves the energy level of the specified song. To accomplish this, we utilize the "spotipy" Python library and authenticate with Spotify for Developers using Client ID and Client Secret credentials.

Subsequently, we construct a database containing various songs with their respective energy values. It's worth noting that the current database comprises only 27 songs, serving as a demonstration dataset.

The core functionality of our function involves comparing the energy difference between the input song and the songs stored in the database. If the energy difference is less than or equal to 0.1, the song is added to an array along with its details, and the array is returned to the user. This process ensures that the user receives song recommendations within a similar energy range.

To provide a user-friendly interface, we have implemented a web application using Flask, incorporating HTML for data submission and display. This allows users to easily interact with the model through a web-based interface.

For hosting the Flask application, we have opted for PythonAnywhere, which offers limited free hosting capabilities, making it accessible to a wide audience.

#Prakhar Pratap Singh @prakhar5100

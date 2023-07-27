# Popular Tracks Web App

Popular Tracks Web App is a simple Django-based web application that allows users to retrieve popular tracks for various music genres.

## Backend Component

### Installation and Setup

1. Clone the repository to your local machine.

2. Only required package is:
```
pip install django
```

3. Ensure you have a Spotify API client ID and client secret. Set them as environment variables:
 ```
SPOTIFY_CLIENT_ID=your_client_id
SPOTIFY_CLIENT_SECRET=your_client_secret
```

4. Run the Django development server:

```
python manage.py runserver
```

5. The backend server will start running at `http://localhost:8000/`.

### API Endpoint

#### GET /tracks/{genre}

Description: Returns a list of 10 tracks sorted by popularity for the given genre.

Query parameters:
- genre: Name of the genre desired by the user.

Response Content-Type: application/json


## Frontend Component

### Visualization

- The popular tracks will be displayed in a table.
- The popularity of each track will be indicated by a color gradient from red to green, where higher popularity is greener and lower popularity is redder.
- If a preview link exists for a track, a "Preview" hyperlink will be displayed in the last column. If no preview link exists, a tilde (`~`) will be displayed to indicate its absence.

## Author

- Başar YILMAZ


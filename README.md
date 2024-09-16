# spotify-clone
simple spotify-clone web app developed with Django

# How to Install

## Prerequisites

- [Anaconda](https://www.anaconda.com/products/distribution) or [Miniconda](https://docs.conda.io/en/latest/miniconda.html) installed on your system.

## Setting Up the Conda Environment

### 1. Clone the Repository 

```bash
git clone https://github.com/KeennyyW/spotify-clone.git
```

### 2. Create and activate Virtual Environment 

```bash
conda create --name <env_name>
conda activate <env_name>
```

### 3. Install requirements 

```bash
pip install -r requirements.txt
```

### 4. Get Spotify API Credentials

1. Go on the [Spotify Developer](https://developer.spotify.com/dashboard) site, create an account and get your credentials
2. Create .env file in root and pass the credentials in

```.env
SPOTIFY_CLIENT_ID='your-credentials' 
SPOTIFY_CLIENT_SECRET='your-credentials' 
```

### 5. Start django server 

```bash
cd spotify
python manage.py runserver
```



## Project still in development!
note that the linked vercel app is not working




from flask import Flask, render_template, request, redirect
from phue import Bridge
from spotipy import Spotify, SpotifyOAuth
from cryptography.fernet import Fernet
import base64
import cv2

# Generate a secret key for encryption
def generate_key():
    key = Fernet.generate_key()
    return base64.urlsafe_b64encode(key).decode()

# Encrypt sensitive data
def encrypt_data(data, key):
    f = Fernet(key.encode())
    encrypted_data = f.encrypt(data.encode())
    return encrypted_data.decode()

# Decrypt sensitive data
def decrypt_data(encrypted_data, key):
    f = Fernet(key.encode())
    decrypted_data = f.decrypt(encrypted_data.encode())
    return decrypted_data.decode()

app = Flask(__name__)

# Set up encryption key (replace with your own generated key or use a secure key management solution)
encryption_key = generate_key()

# Philips Hue bridge IP address
bridge_ip = 'your_bridge_ip'

# Spotify credentials (encrypted)
encrypted_spotify_client_id = 'encrypted_client_id'
encrypted_spotify_client_secret = 'encrypted_client_secret'
spotify_redirect_uri = 'http://localhost:5000/callback'

# Create Spotify client
spotify = Spotify(auth_manager=SpotifyOAuth(client_id=decrypt_data(encrypted_spotify_client_id, encryption_key),
                                            client_secret=decrypt_data(encrypted_spotify_client_secret, encryption_key),
                                            redirect_uri=spotify_redirect_uri,
                                            scope='user-read-currently-playing'))

# Connect to Philips Hue bridge
b = Bridge(bridge_ip)
b.connect()

@app.route('/')
def index():
    # Retrieve currently playing track from Spotify
    try:
        current_track = spotify.current_user_playing_track()
        if current_track is not None:
            track_name = current_track['item']['name']
            artist_name = current_track['item']['artists'][0]['name']
            album_name = current_track['item']['album']['name']
            album_artwork_url = current_track['item']['album']['images'][0]['url']
        else:
            track_name = None
            artist_name = None
            album_name = None
            album_artwork_url = None
    except Exception as e:
        print(f"Error retrieving currently playing track from Spotify: {e}")
        track_name = None
        artist_name = None
        album_name = None
        album_artwork_url = None

    return render_template('index.html', track_name=track_name, artist_name=artist_name, album_name=album_name,
                           album_artwork_url=album_artwork_url)

@app.route('/controls', methods=['POST'])
def controls():
    action = request.form['action']

    # Brighten lights
    if action == 'brighten':
        b.set_light(1, 'bri', 254)

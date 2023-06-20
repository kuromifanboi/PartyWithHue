# PartyWithHue

PartyWithHue is a project that synchronizes Philips Hue lights with music from Spotify. It provides a web interface where users can control the lights, and the lights will change color and brightness based on the currently playing song.

## Features

- Retrieve currently playing track information from Spotify.
- Control Philips Hue lights to adjust brightness and change color.
- Extract dominant color from album artwork to set the light color.
- Securely store and manage sensitive data using encryption.
- Error handling and exception management.
- Enhanced dominant color extraction algorithm.
- Advanced synchronization techniques.

## Prerequisites

Before running the project, make sure you have the following:

- Python 3.x installed.
- Required Python libraries installed (Flask, phue, spotipy, cryptography, opencv-python).
- Philips Hue bridge connected to your network.
- Spotify account with a client ID and client secret.

## Installation

1. Clone the repository

2. Install the required Python libraries: pip install -r requirements.txt


3. Set up the project:

- Replace `your_bridge_ip` in the Python code with the IP address of your Philips Hue bridge.
- Replace `encrypted_client_id` and `encrypted_client_secret` with your Spotify client ID and client secret, encrypted using the provided encryption functions.
- Implement the dominant color extraction algorithm in the `extract_dominant_color` function.

4. Run the application: python app.py


5. Access the application in your web browser at `http://localhost:5000`.

## Usage

- Launch the application by running `app.py`.
- Open the provided URL in your web browser to access the web interface.
- The web interface will display the currently playing track from Spotify, including the track name, artist name, album name, and album artwork.
- Use the controls to adjust the lights:
  - "Brighten" button: Increases the brightness of the lights.
  - "Dim" button: Decreases the brightness of the lights.
  - "Change Color" button: Extracts the dominant color from the album artwork and sets the light color accordingly.
- The lights will synchronize with the currently playing song on Spotify.

## Contributing

Contributions to this project are welcome. If you have any suggestions, enhancements, or bug fixes, please feel free to open an issue or submit a pull request.

## License

PartyWithHue © 2023 by Peter Missick is licensed under Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0). See [LICENSE](LICENSE) for more information.

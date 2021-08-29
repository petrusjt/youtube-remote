# Youtube Remote

## Description 

This app lets you to control youtube on your PC from any device on your local network that has a browser with JavaScript support.

## Requirements

These can be installed with `pip`

- flask
- pynput

## Configuration on Windows

1. Add Google Chrome's executable (chrome.exe) to the PATH environment variable
    - First method:  
        Add the folder C:\Program Files\Google\Chrome\Application to PATH
    - Second method:
        - Create a bin folder in you user folder
        - Add the created bin folder to PATH
        - Create a shortcut of chrome.exe in the bin folder
        - Rename the shortcut to `chrome` so it only has `.lnk` at the end
        - Append `;.LNK` to the PATHEXT environment variable
2. In static/js/index.js change the `Your PC's local IP here` text to your PC's local IP address
    - This can be found with the `ipconfig` command in cmd or powershell.

## Usage

- Start the server with `python app.py` so you can access the webapge hosted by this app.
- Type your PC's local IP to the address bar on your device you want to use as the "remote".
- Insert a youtube link in the input field then press play.
- From now on you can use the buttons to control the player.





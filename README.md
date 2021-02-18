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
3. In app.py on line 32 change the coordinates to match the X icon on the restore tabs panel
    - This is needed because when you enter a new youtube link, it forcefully stops all chrome instances and opens a new. Chrome will think it was a crash and prompts you to restore you last session.
    - TIP: to find the right coordinates, just close Chrome from the task manager, reopen it, take a screenshot (Print Screen/PrtScr button) open MS Paint, press ctrl+v and hover your mouse on the X icon. The coordinates will show at the left bottom corner.

## Configuration on Linux

1. Add chrome to the PATH environment variable
    - If you use chromium, alias it as chrome
        - `alias chrome=chromium`
2. 2nd and 3rd points are basically the same as on Windows.

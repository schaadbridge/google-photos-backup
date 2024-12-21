# google-photos-backup
Procedure and script to free up storage and backup google photos

# Background
I keep running out of storage on my Google account and its all the fault of google photos! 

![](image.png)

I refuse to spend money on extended storage for every tumblr screenshot I've ever taken. I also don't want to lose the ability to send/receive emails. I also have a Windows computer that doesn't load HEIC photos. I'm sick of it.

Documenting this process for my own reference and as I carry out across different Google accounts. Hopefully this saves me or someone else some time.

# Overview
0. Delete all the photos you don't want before all the processing.
1. Export Google Photos data using Google Takeout.
2. Download photos to desired location.
3. Convert HEIC photos to JPG.
4. Remove JSON objects.
5. Scan for live photos worth saving!
6. Remove MOV files.

# How to run
Set `rootdir` to the root directory for Google Photos. This script will run recursively, converting the contents of all subdirectories. Run `python heictojpg.py`, if path-related errors occur midway, just keep rerunning the script until all HEIC files are converted and the program completes on its own.
# HEIC to JPG image format batch conversion script for Python 3.
# You will need to have ImageMagick installed: https://www.imagemagick.org/

import os, subprocess

# Convert recursively (parsing all sub directories) all HEIC files into JPG from the rootdir below
rootdir = r"D:\Photos\Google Photos"
removeHEIC = False
removeJson = False
removeMP4 = False

def heicToJpg(rootdir):
  for it in os.scandir(rootdir):
    if it.is_dir():
      print('parsing %s...' % it.path)
      heicToJpg(it)
    else:
      # we are on a file
      filename = it.path

      # HEIC to JPG conversion
      if filename.lower().endswith(".heic"):
        print('Converting to JPG %s...' % os.path.join(it, filename))
        subprocess.run(["magick", "%s" % os.path.join(it, filename), "%s" % os.path.join(it, (filename[0:-5] + '.jpg'))])
        
        if removeHEIC:
          os.remove("%s" % os.path.join(it, filename))
        else:
          # These files are easily retrievable through renaming, just remove '.old' from the extension.
          os.rename(os.path.join(it, filename), os.path.join(it, filename[0:-5] + '.heic.old'))

      # Remove JSON files (metadata)
      elif removeJson and filename.lower().endswith(".json"):
        # print('Removing JSON file %s...' % os.path.join(it, filename))
        os.remove("%s" % os.path.join(it, filename))

      # Remove MP4 files (video + audio)
      elif removeMP4 and filename.lower().endswith(".mp4"):
        print('Removing mp4 file %s...' % os.path.join(it, filename))
        os.remove("%s" % os.path.join(it, filename))

heicToJpg(rootdir)
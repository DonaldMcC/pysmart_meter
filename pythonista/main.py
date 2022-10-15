# this should simply take pictures at interval using pythonista an an (old iphone)

import os
import photos
import console

console.clear()

album_name = 'meters'
file_name = album_name + '.jpg'

newAlbum = photos.create_album(album_name)

newimg = photos.capture_image()
newimg.save(file_name)

newAsset = photos.create_image_asset(file_name)
newAlbum.add_assets([newAsset])

os.remove(file_name)


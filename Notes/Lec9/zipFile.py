import zipfile, os

# Reading zip files
path = os.path.join('.')
os.chdir(path)  # move to the current directory (doesn't actually do anything)

exampleZip = zipfile.ZipFile('example.zip')
print(exampleZip.namelist())
# ['example/', 'example/folder2/', 'example/folder1/', 'example/image1.png', ...]
spamInfo = exampleZip.getinfo('example/image1.png')
print(spamInfo.file_size)  # 215872, size of the uncompressed file
print(spamInfo.compress_size)  # 190101, size of the compressed data
exampleZip.close()

'''
# Extracting from ZIP Files
exampleZip = zipfile.ZipFile('example.zip')
exampleZip.extractall()
exampleZip.close()
'''

'''
# Extracting a specific file
exampleZip = zipfile.ZipFile('example.zip')
# By default, extracts to ./example/image1.png
exampleZip.extract('example/image1.png')
# Extract to a specific location
newPath = os.path.join('..', 'Lec8')
exampleZip.extract('example/image1.png', newPath)
exampleZip.close()
'''

'''
# Creating and Adding to ZIP Files
newZip = zipfile.ZipFile('ziptest.zip', 'w')
newZip.write('myCats.py', compress_type=zipfile.ZIP_DEFLATED)
newZip.close()
'''

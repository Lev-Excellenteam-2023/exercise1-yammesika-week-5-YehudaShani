import os

path = 'C://Users//yehuda//Google Drive//Computer Science Degree//Year 3//Second Semester//ExcelenTeam//Python//Jupyter Notebooks//Notebooks//week05//images'

files = os.listdir(path)

for file in files:
    if file.startswith("deep"):
        print(file)
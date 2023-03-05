import codecs
import re
from pathlib import Path
import os



# regex to extract required strings

#rename files

directory = "C:/Users/yehuda/Google Drive/Computer Science Degree/Year 3/Second Semester/ExcelenTeam/Python/Jupyter Notebooks/Notebooks/week05/resources/potter"

pathlist = Path(directory).glob('*.html')

for path in pathlist:
    f = codecs.open(path, 'r', 'utf-8')
    text = f.read()
    f.close()

    reg_str = "<" + "option value=" + "\"[0-9]{,3}\"" + " selected>Chapter " + "(.*?)" + ":" + "(.*?)" + "</option>"

    res = re.findall(reg_str, text)

    chapter_number = res[0][0].zfill(3)
    chapter_name = res[0][1]

    complete_name = chapter_number + chapter_name
    print(complete_name)

    os.rename(path, directory + "/" + complete_name + ".html")











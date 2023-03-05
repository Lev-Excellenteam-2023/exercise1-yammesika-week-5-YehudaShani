# find secret messages in logo file

with open('C:/Users/yehuda/Google Drive/Computer Science Degree/Year 3/Second Semester/ExcelenTeam/Python/Jupyter '
          'Notebooks/Notebooks/week05/images/logo.jpg', 'rb') as file:
    byte = file.read(1)
    word = ''
    while byte:
        # Do stuff with byte.

        try:
            byte = file.read(1).decode('utf-8')
        except UnicodeDecodeError:
            if len(word) > 0:
                word = word[1:]
            continue
        if byte.isalpha() or byte == '!':
            word += byte

        else:
            word = ''

        if len(word) == 6 and word[5] == '!':
            print(word)
            word = ''




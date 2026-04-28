try:
    f = open("diary.txt", "x")
    f.write("Military Diary")
    print("File created!")
except FileExistsError:
    print("File already exists!")



    
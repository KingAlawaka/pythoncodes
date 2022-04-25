
def main():
    file_read = open("grades.txt", "r")
    file_write = open("writefile.txt","w")
    grade = "H1"
    for line in file_read:
        line = line.rstrip()
        number = int(line)
        #grade = getGrade(number)
        print(number)
        print(f"{line}% - {grade}",file=file_write)
    file_read.close()
    file_write.close()

main()
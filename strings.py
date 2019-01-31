def US_to_EU(date):
    slash1 = date.find('/')
    slash2 = date.find('/', slash1 + 1)
    return date[slash1 + 1:slash2] + '.' + date[:slash1] + '.' + date[slash2 + 1:]

#US --> 01/12/2018
#EU -->12.1.2018
    
    

def is_phone_num(number): #123-456-7899
    if len(number) != 12:
        return False

    if number[3] != "-" or number[7] != "-":
        return False
    if not number[:3].isdigit() or not number[4:7].isdigit() or not number[8:].isdigit():
        return False

    return True

    

def redact_line(line): #use the .replace() method to switch out string characters
    for i in range(len(line)):
        if ((i == 0 or line[i - 1] == ' ') and i + 12 < len(line) and line[i + 12] in ' \n' and is_phone_num(line[i:i + 12])):
            line = line[:i] + 'XXX-XXX-XXXX' + line[i + 12:]
    return line


def redact_file(infile): #Use the format method on the given argument. Be sure to redact the argument first!
    lst = infile.split('.')
    redacted_file = open(lst[0] + "_redacted" + '.' + lst[1], "w")
    for sentence in open(infile):
        redacted_file.write(redact_line(sentence))
    redacted_file.close()

    

def highlight(file, word):
    highlight_file = open(file, "r")
    i = 1
    for line in highlight_file:
        if word in line:
            print((str(i) + ':').ljust(5) + line.strip().replace(word, '-->' + word + '<--'))
        i += 1

    

def plagiarism(filename1, filename2):
    filename1_check = open(filename1, "r")
    for line in filename1_check:
        filename2_check = open(filename2, "r")
        for otherline in filename2_check:
            if otherline == line:
                return True
        filename2_check.close()
            
    filename1_check.close()
    return False


def count_word(filename, word): #Use the count() method/ and use the ____ method to open a file. 
    file_count = open(filename, "r")
    counter = 0
    for line in file_count:
        counter += line.count(word)
    return counter

    

    
    



#==========================================================
#def main():





    
#==========================================================
      

#if __name__ == '__main__':
    #main()

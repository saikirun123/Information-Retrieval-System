content = open('corpus.txt').readlines()
counter = 0
foo = False
for line in content:
    if line == '.W\n':
        counter = counter+1
        tempfile = open(str(counter)+".txt",'x')
        foo = True
    elif line[0] == "." and line[1] == "I" and counter > 1:
        tempfile.close()
    else:
        if foo:
            tempfile.write(line)

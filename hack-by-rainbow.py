import hashlib
import csv
def hash_password_hack(input_file_name, output_file_name):
    # makes hashes
    clear_text = ""
    mydict = {}


    for i in range(0, 10000):
        i = str(i).encode('utf-8') 
        encrypted = hashlib.sha256(i).hexdigest()
        mydict[i] = encrypted


    with open(input_file_name, 'r') as hash_file:
        # read's from csv file
        reader = csv.reader(hash_file)
        hash_dict = {}
        # reades every line of csv file
        for row in reader:
                hash_dict[row[0]] = row[1]
                check_hash = []
        for i in list(mydict):
            text = "%s" % (mydict[i])
            check_hash.append(mydict[i])
        for i in list(hash_dict):
            if hash_dict[i] in check_hash:
                hashes = list(mydict.keys())[list(mydict.values()).index(hash_dict[i])]
                names = list(hash_dict.keys())[list(hash_dict.values()).index(hash_dict[i])],
                text = "%s,%s\n" % (names[0], hashes.decode('utf-8'))
                clear_text += text  
        with open(output_file_name, 'w') as passwords:
            passwords.write(clear_text)
            

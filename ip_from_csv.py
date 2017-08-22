import os
import sys
import csv
files = sys.argv[1:]
output = 'server.txt'

def main():

    extract(files)

def extract(files):

    urls = []
    for f in files:
        with open(f, 'r') as csvfile: # open a file f as in_file
            data = csv.DictReader(csvfile) # read the file content to data
            for row in data:
                #print("adding row {0} to urls.".format(row['URL']))

                if "préprod" in row['Group']:
                    print("adding row {0} to urls.".format(row['URL']))
                    urls.append(row['URL'])

    for index, item in enumerate(urls):
        urls[index] = item.strip()

    print("This is the stripped list", urls)

    print('--' * 10)
    ssh = [s for s in urls if "ssh" in s]
    print("This is the ssh servers connections urls : {}".format(ssh))

    with open(f'{output}', mode='wt', encoding=None) as server_file:
        server_file.write('\n'.join(item for item in ssh))


if __name__ == '__main__':

    main()

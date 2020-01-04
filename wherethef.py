#!/usr/bin/python3

import os
import sys
import time
import datetime
import configparser

# Load the configuration file
from configparser import ConfigParser
config = ConfigParser()
config.read('config')

DirSearch = config.get('DirectoryLocations', 'DirSearch')
SaveLocation = config.get('DirectoryLocations', 'SaveLocation')

def splashback():
    print('                                                                                                                                                                    ')
    print('                                                                                                                                                          ,#*       ')
    print('                                                                                                                                                       @@@%&@@      ')
    print('                                                                                                                                                #@@  /@@   *@@      ')
    print('                                                                                                                                     %@#   @@   /@@       @@        ')
    print('                                                                                                                          .&@         ./ @@@@#  ,@&     .@@         ')
    print('                                                                                                                          ,@@  *%%   %@%  %@@   ,@%      ,%         ')
    print('                                                                                                                          ,@@%&,@@@  %@%  %@@     *     #@&         ')
    print('                                                                                                                  &@@@@@, ,@@   *@@  %@%  %@@,. %@@                 ')
    print('                                                                                                         ./      @&       ,@@   *@@  %@%   @&*                      ')
    print('                                                                                                 ,%@    @@       &@@@@@@% ,@@   *@@                                 ')
    print('                                                                                           ,@@@#  @@#  %@*            @@. ,@%                                       ')
    print('                                                                                   #& @@@@@* %@@   @@*,@#        @@@@%                                              ')
    print('                                                                                   @@(  @@%  *@@    @@@@                                                            ')
    print('                                                                     #@@@@@&       @@   @@%  *@@    *@@,                                                            ')
    print('                                                             #@@@.  @@,            @@   @@%  *@#    @@*                                                             ')
    print('                                                     , @@  @@   @@, #@@@@@@@       @@   *.        @@%                                                               ')
    print('                                *%          .#@@/  ,@@&   @@@@@&*    .   (@#                                                                                        ')
    print('                           .%@ %@@   ,.   ,@#  (@@ ,@@.   @@#   @@  &@@@%.                                                                                          ')
    print('                    *%@*   @@# %@@&@@@@# ,@@%@@@@% ,@@    /@@@@@*                                                                                                   ')
    print('             .&@,   @@@@   @@  %@@   @@% #@@    ,# ,@@                                                                                                              ')
    print('              %@&  .@%%@# (@%  %@@   @@%  @@@%@@*                                                                                                                   ')
    print('               @@, %@,.@@ @@.  %@@   @@%                                                                                                                            ')
    print('               %@@.@%  @@%@%   %@@                                                                                                                                  ')
    print('                @@@@.  ,@@@                                                                                                                                         ')
    print('                %@@&                                                                                                                                                ')
    print('                                                                                                                                                                    ')
    print('                                                                                                                                                                    ')
    print('                                                                                      A Big7asty original                                                           ')
    print('                                                        Have you been saving everything you need within the directory you are searching?                            ')
    return 0

def purge():
    #Purges the working directory
    print()
    print('Do you need any of the files in transfer_dir? (They will be deleted)')
    print()
    rm_files = str(input('y or n: '))
    if rm_files == "y":
        print('QUITTING')
        sys.exit()
    elif rm_files == "n":
        clean_up = 'rm transfer_dir/*'
        os.system(clean_up)
    else:
        print('Invalid input, QUITTING')
        sys.exit()
    return 0

def find():
    #Finds all the files saved from within a particular timeframe
    print()
    print('Start date?')
    print()
    print('        i.e. 2001230900 for 9am on the 23rd of January, 2020')
    from_date = input()
    print()
    print('End date?')
    print()
    print('        i.e. 2001231700 for 5pm on the 23rd of January, 2020')
    to_date = input()
    find_start = 'touch -t ' + str(from_date) + ' /tmp/t1'
    find_end = 'touch -t ' + str(to_date) + ' /tmp/t2'
    find_show = 'find ' + str(DirSearch) + ' -newer /tmp/t1 -and -not -newer /tmp/t2 > /tmp/transfer'
    os.system(find_start)
    os.system(find_end)
    os.system(find_show)
    return 0

def movedocs():
    #Brings the files listed in /tmp/ to the pwd
    working_file = 'cat /tmp/transfer > yourfiles.txt'
    os.system(working_file)
    #Reads the listed file paths and consolidates them into one directory
    with open('yourfiles.txt', 'r+') as f:
        contents = [x.strip() for x in f.readlines()]
        counter = 0
        while counter < len(contents):
            file = contents[counter]
            cp_files = 'cp ' + str(file) + ' ' + str(SaveLocation) + '/wherethef-master/transfer_dir > /dev/null 2>&1'
            #print(cp_files)
            os.system(cp_files)
            counter += 1
    return 0

def opendocs():
    #Clean up pwd and opens File Manager for transfer
    clean_up = 'rm yourfiles.txt'
    os.system(clean_up)
    give_me_my_files = 'xdg-open transfer_dir'
    os.system(give_me_my_files)

splashback()

purge()

find()

movedocs()

opendocs()

print()
print('--------------------------------------------------------------------')
print(' If you aren\'t getting the files you expect, check the config file ')
print(' and confirm the file paths are correct.                            ')
print('--------------------------------------------------------------------')

#!/usr/bin/python3

import os
import sys
import time
import datetime
import configparser
import argparse
from termcolor import colored

""" Load the configuration file """
from configparser import ConfigParser
config = ConfigParser()
config.read('config')

DirSearch = config.get('DirectoryLocations', 'DirSearch')
SaveLocation = config.get('DirectoryLocations', 'SaveLocation')
LookBack = config.get('TimeSettings', 'Lookback')

""" Load colour settings """
red = lambda text: '\033[0;31m' + text + '\033[0m'
green = lambda text: '\033[0;32m' + text + '\033[0m'
yellow = lambda text: '\033[0;33m' + text + '\033[0m'
cyan = lambda text: '\033[0;36m' + text + '\033[0m'

def main():
    """ Run main """
    splashback()

    parser = argparse.ArgumentParser(description = 'wherethef - Evidence consolidation tool. When run without arguements, lookup timeframe will be default value in config file.')
    parser.add_argument('-t', '--timeframe', action='store_true', help='Define a from and to timeframe to search')
    args = parser.parse_args()
    if args.timeframe:
        purge()

        customFind()
    else:
        purge()

        defaultFind()

    moveDocs()

    openDocs()

    print()
    print('------------------------------------------------------------------------')
    print(yellow(' [*] If you aren\'t getting the files you expect, check the config file '))
    print(yellow(' [*] and confirm the file paths are correct.                            '))
    print('------------------------------------------------------------------------')

def splashback():
    print(cyan("""                                                                                                                                                                  
                                                                                                                                                                     ,#*       
                                                                                                                                                                  @@@%&@@      
                                                                                                                                                           #@@  /@@   *@@      
                                                                                                                                                %@#   @@   /@@       @@        
                                                                                                                                     .&@         ./ @@@@#  ,@&     .@@         
                                                                                                                                     ,@@  *%%   %@%  %@@   ,@%      ,%         
                                                                                                                                     ,@@%&,@@@  %@%  %@@     *     #@&         
                                                                                                                             &@@@@@, ,@@   *@@  %@%  %@@,. %@@                 
                                                                                                                    ./      @&       ,@@   *@@  %@%   @&*                      
                                                                                                            ,%@    @@       &@@@@@@% ,@@   *@@                                 
                                                                                                      ,@@@#  @@#  %@*            @@. ,@%                                       
                                                                                              #& @@@@@* %@@   @@*,@#        @@@@%                                              
                                                                                              @@(  @@%  *@@    @@@@                                                            
                                                                                #@@@@@&       @@   @@%  *@@    *@@,                                                            
                                                                        #@@@.  @@,            @@   @@%  *@#    @@*                                                             
                                                                , @@  @@   @@, #@@@@@@@       @@   *.        @@%                                                               
                                           *%          .#@@/  ,@@&   @@@@@&*    .   (@#                                                                                        
                                      .%@ %@@   ,.   ,@#  (@@ ,@@.   @@#   @@  &@@@%.                                                                                          
                               *%@*   @@# %@@&@@@@# ,@@%@@@@% ,@@    /@@@@@*                                                                                                   
                        .&@,   @@@@   @@  %@@   @@% #@@    ,# ,@@                                                                                                              
                         %@&  .@%%@# (@%  %@@   @@%  @@@%@@*                                                                                                                   
                          @@, %@,.@@ @@.  %@@   @@%                                                                                                                            
                          %@@.@%  @@%@%   %@@                                                                                                                                  
                           @@@@.  ,@@@                                                                                                                                         
                           %@@&                                                                                                                                                
                                                                                                                                                                               
                                                                                                                                                                               
                                                                                                 A Big7asty original                                                           
                                                                   Have you been saving everything you need within the directory you are searching?                            """))
    return 0

def purge():
    """ Purges the working directory and cleans up /tmp files """
    print()
    print('The system time is:')
    date = 'date'
    print('-------------------------------')
    os.system(date)
    print('-------------------------------')
    print(red('  [!] NOTE! If the system clock is out, files you are searching would have been saved against this time.\n'))
    print(red('  [!] Do you need any of the files in transfer_dir? (They will be deleted!)\n'))
    rm_files = str(input('  [+] y or n: ')).lower()
    if rm_files == "y":
        print(red('  [!] QUITTING'))
        sys.exit()
    elif rm_files == "n":
        clean_up = 'rm -rf transfer_dir/*'
        clean_up_tmp = 'rm /tmp/t1 && rm /tmp/t2 && rm /tmp/t1_command && rm /tmp/t2_command && rm /tmp/transfer'
        os.system(clean_up)
        os.system(clean_up_tmp)
    else:
        print(red('  [!] Invalid input, QUITTING'))
        sys.exit()
    return 0

def defaultFind():
    """ Runs the find function against the defined lookback period as assigned in the config file """
    from_date_command = 'date -d \'' + str(LookBack) + '\' +\"%y-%m-%d-%R\" | sed \'s/-//g\' | sed \'s/://g\' > /tmp/t1_command'
    to_date_command = 'date +\"%y-%m-%d-%R\" | sed \'s/-//g\' | sed \'s/://g\' > /tmp/t2_command'
    os.system(from_date_command)
    os.system(to_date_command)
    with open('/tmp/t1_command', 'r+') as f:
        from_date_list = [x.strip() for x in f.readlines()]
    with open('/tmp/t2_command', 'r+') as g:
        to_date_list = [c.strip() for c in g.readlines()]
    from_date = str(from_date_list)[2:-2]
    to_date = str(to_date_list)[2:-2]
    find_start = 'touch -t ' + str(from_date) + ' /tmp/t1'
    find_end = 'touch -t ' + str(to_date) + ' /tmp/t2'
    find_show = 'find ' + str(DirSearch) + ' -newer /tmp/t1 -and -not -newer /tmp/t2 > /tmp/transfer'
    os.system(find_start)
    os.system(find_end)
    os.system(find_show)
    return 0

def customFind():
    """Finds all the files saved from within a particular timeframe"""
    print()
    print(yellow('  [*] Start date?'))
    print(yellow('  [*] i.e. 2001230900 for 9am on the 23rd of January, 2020'))
    print()
    from_date = input()
    print()
    print(yellow('  [*] End date?'))
    print(yellow('  [*] i.e. 2001231700 for 5pm on the 23rd of January, 2020'))
    print()
    to_date = input()
    find_start = 'touch -t ' + str(from_date) + ' /tmp/t1'
    find_end = 'touch -t ' + str(to_date) + ' /tmp/t2'
    find_show = 'find ' + str(DirSearch) + ' -newer /tmp/t1 -and -not -newer /tmp/t2 > /tmp/transfer'
    os.system(find_start)
    os.system(find_end)
    os.system(find_show)
    return 0

def moveDocs():
    """ Brings the files listed in /tmp/ to the pwd """
    working_file = 'cat /tmp/transfer > yourfiles.txt'
    os.system(working_file)
    """ Reads the listed file paths and consolidates them into one directory """
    with open('yourfiles.txt', 'r+') as f:
        contents = [x.strip() for x in f.readlines()]
        counter = 0
        while counter < len(contents):
            file = contents[counter]
            cp_files = 'cp ' + str(file) + ' ' + str(SaveLocation) + '/wherethef-master/transfer_dir > /dev/null 2>&1'
            cp_pics = 'cp ' + str(file) + '/*.png ' + str(SaveLocation) + '/wherethef-master/transfer_dir > /dev/null 2>&1'
            os.system(cp_files)
            os.system(cp_pics)
            counter += 1
    return 0

def openDocs():
    """ Clean up pwd and opens File Manager for transfer """
    clean_up = 'rm yourfiles.txt'
    give_me_my_files = 'xdg-open transfer_dir'
    os.system(clean_up)
    os.system(give_me_my_files)
    return 0

if __name__ == "__main__":
    main()

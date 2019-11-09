#!/usr/bin/python3

import os
import time
import datetime

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
    print('                                                                   Have you been saving everything within /root/Documents?                                          ')            
    return 0

def purge():
    #Purges the working directory
    clean_up = 'rm transfer_dir/*'
    os.system(clean_up)

def find():
    #Finds all the files saved from within a particular timeframe
    print()
    print('Start date?')
    print()
    print('        i.e. 1906110900 for 9am on the 11/06/2019')
    from_date = input()
    print()
    print('End date?')
    print()
    print('        i.e. 1906111700 for 5pm on the 11/06/2019')
    to_date = input()
    find_start = 'touch -t ' + str(from_date) + ' /tmp/t1'
    find_end = 'touch -t ' + str(to_date) + ' /tmp/t2'
    find_show = 'find /root/Documents -newer /tmp/t1 -and -not -newer /tmp/t2 > /tmp/transfer'
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
            #Make sure the file path below this comment  v     v  here is correct
            #                                             v   v
            #                                               v
            cp_files = 'cp ' + str(file) + ' /root/test/wherethef/transfer_dir > /dev/null 2>&1'
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

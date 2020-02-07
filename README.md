# Wherethef.py

'wherethef.py' is an open source administration tool for pulling all files within a timeframe you specify into a new directory. The use case for this tool is to make penetration tests/vulnerability assessment data transfer a little easier.

# IMPORTANT!

For this tool to be effective, good disipline is required in that you save/pipe ALL evidence, documentation, tool output to the directory of your choosing as defined in the config file. It will not find any files outside of this directory.

In addition, if your system clock is out, this will effect the time search function of the tool. wherethef.py will pull up the current system time for you.

# License

This software is free. You can use it under the terms of GPLv3, see LICENSE.

# Installation

 You can download wherethef.py by cloning this git repository:

    git clone https://github.com/Big7asty/wherethef
    
Or by downloading the ZIP archive.

Then make it executable
    
    chmod +x wherethef.py

Don't forget to define directory locations within the config file.

# To Do

- Add argparse to define timeframe to the last 24 hours and skip user input defining timeframe

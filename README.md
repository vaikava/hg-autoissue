hg-autoissue
============
Automatically converts hashes (#) followed by numbers (#123) in your commit
messages to URL's pointing to your issue tracker with the respective ID.

Installation
============
Extract the `autoissue.py` file to a folder of your choice.

Add this to your global .hgrc file:

    [extensions]
    autoissue = path/to/autoissue.py

And to your repository's .hg/hgrc file:

    [autoissue]
    issuetracker = https://bitbucket.org/username/project/issue/

Usage
============
After installation, perform an commit as follows: 

    hg commit -m "Fixed issue #3"
    
...Which would result in the following commit message used:
    
    "Fixed issue #3 (https://bitbucket.org/username/project/issue/3)"


License
============

See `LICENSE` file.

> Copyright (c) 2012 Joakim B

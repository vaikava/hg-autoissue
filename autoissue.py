"""Automatically converts hashes (#) followed by numbers (#123) in your commit
messages to URL's pointing to your issue tracker with the respective ID.

Add this to your global .hgrc file:

    [extensions]
    autoissue = path/to/autoissue.py

And to your repository's .hg/hgrc file:

    [autoissue]
    issuetracker = https://bitbucket.org/username/project/issue/

Then, perform an commit as follows: 

    hg commit -m "Fixed issue #3"
    
... which would result in the following commit message being set:
    
    "Fixed issue #3 (https://bitbucket.org/username/project/issue/3)"

   See the distributed LICENSE file for license information.
   Copyright (C) 2012 Joakim B
"""


import re
from mercurial import commands, extensions, cmdutil, util

cfe = cmdutil.commitforceeditor
RE_ISSUE = re.compile(r'[#](\d+)', re.IGNORECASE)

def commitforceeditor(repo, ctx, subs):
    text = cfe(repo, ctx, subs)
    print ctx

    # Do not commit unless the commit message differs from 
    # the one you specified on the command line
    if ctx.description() == text.strip():
        raise util.Abort("empty commit message")
    else:
        return text

def commit(originalcommit, ui, repo, *pats, **opts):
    if not opts["message"]:
        return originalcommit(ui, repo, *pats, **opts)
    else:
	issuetracker = ui.config('autoissue', 'issuetracker', 'No issue tracker set IN .hgrc')
	opts['message'] = RE_ISSUE.sub('#'+r'\1'+' ('+issuetracker+r'\1)', opts['message'])

        # monkey-patch
        cmdutil.commitforceeditor = commitforceeditor

        return originalcommit(ui, repo, *pats, **opts)

def uisetup(ui):
    extensions.wrapcommand(commands.table, 'commit', commit)  

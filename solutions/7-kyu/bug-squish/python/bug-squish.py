def debug(s):
    upperBugs = s.replace('bugs','BUGS')
    noBug = upperBugs.replace('bug','')
    return noBug.lower()
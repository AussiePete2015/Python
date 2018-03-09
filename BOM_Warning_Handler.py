import re
import sys
import os.path
import filecmp
import glob
from itertools import islice
 
sourcepth = 'D:\\Cognos_Testing\\Esri\\python\\'
targetpth = 'D:\\Cognos_Testing\\Esri\\python\\warning\\'

os.chdir(r'D:\\Cognos_Testing\\Esri\\python')

def nofileprocessxml(sourcepth,targetpth,file,filenm):
    'Gather each file and generate an output'

    for line in sourcefn:
        line = line.rstrip()
        if re.search(r'<issue-time-local tz=', line) :
            mapsrv = line.strip('<issue-time-local tz=')
            mapsrv = mapsrv.rstrip()
            line = Previousfn.writelines(mapsrv[6:-19] + '\n')
            line = targetfn.writelines(mapsrv[6:-19] + '\n')

    print 'PRODUCT: ' + file[:-4]
    print 'ALERT DATE: ' + mapsrv[6:-19]
    print
    
    sourcefn = open(sourcepth + file,'r')
    # Check for Cancellation string            
    pattern = re.compile('<text type="warning_title">')
        
    for i, line in enumerate(sourcefn):
        for match in re.finditer(pattern, line):
            TITLE = line.strip()
            TITLE = TITLE[27:-7]
            print 'TITLE: ' + TITLE        

    with open(sourcepth + file,'r') as e:
        for line in e:
            if '<product-type>' in line:
                STATUS = (''.join(islice(e, 1)))
                STATUS = STATUS.strip((''.join(islice(e, 1))))
                print 'STATUS: ' + STATUS[6:-7]

    with open(sourcepth + file,'r') as f:
        for line in f:
            if '<text type="warning_title">' in line:
                DESCR = (''.join(islice(f, 1)))
                DESCR = DESCR.strip((''.join(islice(f, 1))))
                print 'Description: ' + DESCR[10:]

    with open(sourcepth + file,'r') as g:
        for line in g:
            if '<area-list>' in line:
                BOMAREA = (''.join(islice(g, 1)))
                BOMAREA = BOMAREA.strip((''.join(islice(g, 1))))
                print 'BOM AREA: ' + BOMAREA[3:12]

    if STATUS == 'phase>CAN</phase':
        print
        print 'Do nothing'
    else:
        print
        print 'do something'

def existprocessxml(sourcepth,targetpth,file,filenm):
    if os.path.isfile(Previousfn) and os.access(Previousfn, os.R_OK):
        print 'File ' + filenm + ' exists and is readable'
            
        Previousfn = open(targetpth + filenm + '_previous.xml', 'r')
        targetfn = open(targetpth + filenm + '_found.xml', 'w')

        for line in sourcefn:
            line = line.rstrip()
            re.search(r'issue-time-local', line)
            mapsrv = line.strip('issue-time-local')
            mapsrv = mapsrv.rstrip()        
            line = targetfn.writelines(mapsrv + '\n')
            
        
        if filecmp.cmp(targetpth + filenm + '_previous.xml', targetpth + filenm + '_found.xml', shallow=False):
            print "stuffed"            
        else:
            sourcefn = open(sourcepth + file,'r')
            # Check for Cancellation string            
            pattern = re.compile('<phase>CAN</phase>')
                
            for i, line in enumerate(sourcefn):
                for match in re.finditer(pattern, line):
                            
                    print line.strip()
                    print
                    
        targetfn.close()
        Previousfn.close()        


def main():
    for file in glob.glob('*.xml'):
        filenm = file[:-4]

        sourcefn = open(sourcepth + file,'r')
        targetfn = open(targetpth + filenm + '_found.xml', 'w')
        Previousfn = targetpth + filenm + '_previous.xml'

        if os.path.isfile(Previousfn) and os.access(Previousfn, os.R_OK):
            print 'File ' + filenm + ' exists and is readable'

            return existprocessxml(sourcepth,targetpth,file,filenm)
##            
##            Previousfn = open(targetpth + filenm + '_previous.xml', 'r')
##            targetfn = open(targetpth + filenm + '_found.xml', 'w')
##
##            for line in sourcefn:
##                line = line.rstrip()
##                re.search(r'issue-time-local', line)
##                mapsrv = line.strip('issue-time-local')
##                mapsrv = mapsrv.rstrip()        
##                line = targetfn.writelines(mapsrv + '\n')
##                
##            
##            if filecmp.cmp(targetpth + filenm + '_previous.xml', targetpth + filenm + '_found.xml', shallow=False):
##                print "stuffed"            
##            else:
##                sourcefn = open(sourcepth + file,'r')
##                # Check for Cancellation string            
##                pattern = re.compile('<phase>CAN</phase>')
##                    
##                for i, line in enumerate(sourcefn):
##                    for match in re.finditer(pattern, line):
##                                
##                        print line.strip()
##                        print
##                        
##            targetfn.close()
##            Previousfn.close()        
            
        else:
            sourcefn = open(sourcepth + file,'r')
            Previousfn = open(targetpth + filenm + '_previous.xml', 'w+')
            targetfn = open(targetpth + filenm + '_found.xml', 'w+')
            
            print 'Either file is missing or is not readable'
            print
            print sourcepth
            print targetpth
            print file
            print filenm
            return processxmlfl(sourcepth,targetpth,file,filenm)

            
    ##        sourcefn = open(sourcepth + file,'r')
    ##        Previousfn = open(targetpth + filenm + '_previous.xml', 'w+')
    ##        targetfn = open(targetpth + filenm + '_found.xml', 'w+')
    ##
    ##        for line in sourcefn:
    ##            line = line.rstrip()
    ##            if re.search(r'<issue-time-local tz=', line) :
    ##                mapsrv = line.strip('<issue-time-local tz=')
    ##                mapsrv = mapsrv.rstrip()
    ##                line = Previousfn.writelines(mapsrv[6:-19] + '\n')
    ##                line = targetfn.writelines(mapsrv[6:-19] + '\n')
    ##
    ##        print 'PRODUCT: ' + file[:-4]
    ##        print 'ALERT DATE: ' + mapsrv[6:-19]
    ##        print
    ##        
    ##        sourcefn = open(sourcepth + file,'r')
    ##        # Check for Cancellation string            
    ##        pattern = re.compile('<text type="warning_title">')
    ##            
    ##        for i, line in enumerate(sourcefn):
    ##            for match in re.finditer(pattern, line):
    ##                TITLE = line.strip()
    ##                TITLE = TITLE[27:-7]
    ##                print 'TITLE: ' + TITLE        
    ##
    ##        with open(sourcepth + file,'r') as e:
    ##            for line in e:
    ##                if '<product-type>' in line:
    ##                    STATUS = (''.join(islice(e, 1)))
    ##                    STATUS = STATUS.strip((''.join(islice(e, 1))))
    ##                    print 'STATUS: ' + STATUS[6:-7]
    ##
    ##        with open(sourcepth + file,'r') as f:
    ##            for line in f:
    ##                if '<text type="warning_title">' in line:
    ##                    DESCR = (''.join(islice(f, 1)))
    ##                    DESCR = DESCR.strip((''.join(islice(f, 1))))
    ##                    print 'Description: ' + DESCR[10:]
    ##
    ##        with open(sourcepth + file,'r') as g:
    ##            for line in g:
    ##                if '<area-list>' in line:
    ##                    BOMAREA = (''.join(islice(g, 1)))
    ##                    BOMAREA = BOMAREA.strip((''.join(islice(g, 1))))
    ##                    print 'BOM AREA: ' + BOMAREA[3:12]
    ##
    ##        if STATUS == 'phase>CAN</phase':
    ##            print
    ##            print 'Do nothing'
    ##        else:
    ##            print
    ##            print 'do something'
         

    Previousfn.close()
    targetfn.close()    
    sourcefn.close()


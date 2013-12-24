#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      hp
#
# Created:
# Copyright:   (c) hp
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import urllib
import os
import sys
import time
from sys import exit

def datafetcher(startroll,endroll,exam):

    print("Please wait. Connecting to MGU website.")
    time.sleep(4)
    print("Connected to server. Printing details")
    mymarklist=[]
    for numberint in range(startroll, endroll):
        number = str(numberint)
        params = urllib.urlencode({'module': 'public', 'attrib': 'result', 'page': 'result','exam':exam,'prn':number,'Submit2':'Submit'})
        f = urllib.urlopen("http://103.251.43.95/mgcbcss/bTech/index.php?%s" % params)
        data= f.read()
        filesize= sys.getsizeof(data)
        if filesize > 19200:
            #valid file
            with open( "temppdf.pdf", "ab+") as code:
                code.write(data)
            input="temppdf.pdf"
            output= "temptxt.txt"
            os.system(("pdftotext %s %s") %( input , output))
            #got op file. Has to get marks of each subject now
            linenumber = 36
            fp = open(output,"r")
            lines = fp.readlines()
            collegename = lines[4].strip(':').strip("\n").lstrip()
            branch = lines[8].strip(':').strip("\n").lstrip()
            name = lines[12].strip(':').strip("\n").lstrip()
            data = collegename+","+branch + "," +number+","+ name + ","
            with open( filename, "a+") as code:
                code.write(data)


            gradelist=[]
            while linenumber<125:
                subjectname = lines[linenumber-2].strip(':').strip("\n").lstrip()
                passfailstatus = lines[linenumber+6].strip(':').strip("\n").lstrip()
                if lines[linenumber].strip("\n")!= "-" and lines[linenumber+2].strip("\n")!="-" and lines[linenumber+4].strip("\n")!="-":
                    internal = int(lines[linenumber])
                    external = int(lines[linenumber+2])
                    total = int(lines[linenumber+4])

                    if total>=75:
                        if external>=40:
                                if total>135:
                                    gradepoint=10
                                elif total>120 and total<=135:
                                    gradepoint=9
                                elif total>105 and total<=120:

                                    gradepoint=8
                                elif total>90 and total<=105:

                                    gradepoint=7
                                elif total>83 and total<=90:

                                    gradepoint=6
                                elif total>74 and total<=83:

                                    gradepoint=5.5
                    else:

                        gradepoint=0
                else:
                    if lines[linenumber+4].strip("\n")=="-":
                        internal = int(lines[linenumber])
                        external = int(lines[linenumber+2])
                        total = 0
                    gradepoint=0

                gradelist.append(gradepoint)
                localdata = subjectname+","+str(internal)+","+str(external)+","+str(total)+","+passfailstatus+","
                with open( filename, "a+") as code:
                    code.write(localdata)
                linenumber = linenumber+12

            #gradelist generation complete

            partoneofgpa = float(2*(gradelist[6]+gradelist[7]))
            sum =0
            for i in range(0,6):
                sum = float(sum+gradelist[i])
            parttwoofgpa = float(4*sum)
            gpa = float((partoneofgpa+parttwoofgpa)/28)

            if lines[128].strip("\n")=="-":
                totalmarks = 0
            else:
                totalmarks = lines[128].strip("\n")
            totalpassfail =lines[130].strip("\n")
            localdata=str(totalmarks)+","+str(gpa)+","+totalpassfail+"\n"
            with open( filename, "a+") as code:
                    code.write(localdata)

def datafetchers1s2(startroll,endroll,exam):

    print("Please wait. Connecting to MGU website.")
    time.sleep(4)
    print("Connected to server. Printing details")
    mymarklist=[]
    for numberint in range(startroll, endroll):
        number = str(numberint)
        params = urllib.urlencode({'module': 'public', 'attrib': 'result', 'page': 'result','exam':exam,'prn':number,'Submit2':'Submit'})
        f = urllib.urlopen("http://103.251.43.95/mgcbcss/bTech/index.php?%s" % params)
        data= f.read()
        filesize= sys.getsizeof(data)
        if filesize > 19200:
            #valid file
            with open( "temppdf.pdf", "ab+") as code:
                code.write(data)
            input="temppdf.pdf"
            output= "temptxt.txt"
            os.system(("pdftotext %s %s") %( input , output))
            #got op file. Has to get marks of each subject now
            linenumber = 36
            fp = open(output,"r")
            lines = fp.readlines()
            collegename = lines[4].strip(':').strip("\n").lstrip()
            branch = lines[8].strip(':').strip("\n").lstrip()
            name = lines[12].strip(':').strip("\n").lstrip()
            data = collegename+","+branch + "," +number+","+ name + ","
            with open( filename, "a+") as code:
                code.write(data)


            gradelist=[]
            while linenumber<164:
                subjectname = lines[linenumber-2].strip(':').strip("\n").lstrip()
                passfailstatus = lines[linenumber+6].strip(':').strip("\n").lstrip()
                if lines[linenumber].strip("\n")!= "-" and lines[linenumber+4].strip("\n")!="-":
                    internal = int(lines[linenumber])
                    if lines[linenumber+2].strip("\n")!="-":
                        external = int(lines[linenumber+2].strip("\n"))
                    else:
                        external=0
                    total = int(lines[linenumber+4])

                    if total>=75:
                        if lines[linenumber+4].strip("\n")!="-":
                            if external>=40:
                                    if total>135:
                                        gradepoint=10
                                    elif total>120 and total<=135:
                                        gradepoint=9
                                    elif total>105 and total<=120:

                                        gradepoint=8
                                    elif total>90 and total<=105:

                                        gradepoint=7
                                    elif total>83 and total<=90:

                                        gradepoint=6
                                    elif total>74 and total<=83:

                                        gradepoint=5.5
                            else:

                                gradepoint=0

                        elif lines[linenumber+4].strip("\n")=="-":

                                    if total>135:
                                        gradepoint=10
                                    elif total>120 and total<=135:
                                        gradepoint=9
                                    elif total>105 and total<=120:

                                        gradepoint=8
                                    elif total>90 and total<=105:

                                        gradepoint=7
                                    elif total>83 and total<=90:

                                        gradepoint=6
                                    elif total>74 and total<=83:

                                        gradepoint=5.5
                                    else:
                                        gradepoint=0
                else:
                    if lines[linenumber+4].strip("\n")=="-":
                        internal = int(lines[linenumber])
                        external = int(lines[linenumber+2])
                        total = 0


                    gradepoint=0

                gradelist.append(gradepoint)
                localdata = subjectname+","+str(internal)+","+str(external)+","+str(total)+","+passfailstatus+","
                with open( filename, "a+") as code:
                    code.write(localdata)
                linenumber = linenumber+12

            #gradelist generation complete

            partoneofgpa = float(gradelist[9]+gradelist[10])
            parttwoofgpa = float(4*float(gradelist[7]+gradelist[6]+gradelist[5]+gradelist[2]+gradelist[1]))
            partthreeofgpa = float(6*float(gradelist[4]+gradelist[3]))
            partfourofgpa = float(5*float(gradelist[0]+gradelist[8]))
            gpa = float((partoneofgpa+parttwoofgpa+partthreeofgpa+partfourofgpa)/44)

            if lines[164].strip("\n")=="-":
                totalmarks = 0
            else:
                totalmarks = lines[164].strip("\n")
            totalpassfail =lines[166].strip("\n")
            localdata=str(totalmarks)+","+str(gpa)+","+totalpassfail+"\n"
            with open( filename, "a+") as code:
                    code.write(localdata)


if os.path.isfile("newlist.txt"):
    os.remove("newlist.txt")
print " Welcome to MGU Data Extractor"
filename = raw_input("Enter filename for the file to be generated.Include the extension also")
print "Enter Semester"
choice0=raw_input("0.Demo Run\n1.S6\n2.S4\n3.S1S2\n")
if choice0=="0":
    exam='11'
    startno="10012615"
    endno="10012625"
    datafetcher(int(startno),int(endno),exam)
elif choice0=="1":
    exam = '11'
    choice1 = raw_input("1.Rajagiri\n2.All Colleges\n")
    if choice1=="1":
        startno="10012421"
        endno="10013081"
        datafetcher(int(startno),int(endno),exam)

    elif choice1=="2":
        startno="10001001"
        endno="10019496"
        datafetcher(int(startno),int(endno),exam)

    else:
        print"Invalid choice4. Exiting"
        exit()
elif choice0=="2":
    exam='10'
    choice1 = raw_input("1.Rajagiri\n2.All Colleges\n")
    if choice1=="1":
        startno="11012141"
        endno="11012924"
        datafetcher(int(startno),int(endno),exam)

    elif choice1=="2":
        startno="11001001"
        endno="11024733"
        datafetcher(int(startno),int(endno),exam)

    else:
        print"Invalid choice3. Exiting"
        exit()
elif choice0=="3":
    exam='9'
    choice1 = raw_input("1.Rajagiri\n2.All Colleges\n")
    if choice1=="1":
        startno="12012471"
        endno="12013233"
        datafetchers1s2(int(startno),int(endno),exam)

    elif choice1=="2":
        startno="12001001"
        endno="12027061"
        datafetchers1s2(int(startno),int(endno),exam)

    else:
        print"Invalid choice1. Exiting"
        exit()
else:
    print"Invalid choice2. Exiting"
    exit()

print filename
if os.path.isfile("temppdf.pdf"):
    os.remove("temppdf.pdf")
import webbrowser
webbrowser.open(filename)
print("Program completed")
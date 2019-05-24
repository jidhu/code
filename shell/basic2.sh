FILELIST=`ls`
echo $FILELIST

    # You can store a shell command to a variable

FileWithTimeStamp=~/workspace/shell/Date_$(/bin/date +%Y-%m-%d).txt
echo $FileWithTimeStamp

    # This will automatically Store the current date from
    # bin/date

#Exercise:

    # The target of this exercise is to create a string,
    # an integer, and a complex variable using command
    # substitution. The string should be named BIRTHDATE
    # and should contain the text "Jan 1, 2000". The
    # integer should be named Presents and should contain
    # the number 10. The complex variable should be named
    # BIRTHDAY and should contain the full weekday name of
    # the day matching the date in variable BIRTHDATE e.g.
    # Saturday. Note that the 'date' command can be used
    # to convert a date format into a different date format.
    # For example, to convert date value, $date1, to day
    # of the week of date1,
    # use: date -d "$date1" +%A

BIRTHDATE="Jan 1, 2000"
a=10

BIRTHDAY
def line_parser(text, text_name):
    """This searches for contact_name, body, and readable_date to output to a
       .csv file in the format readable_date, body\n with the contact_name as
       the CSV name.
    """
    name = text[text.find('" contact_name="') + 16:text.find('" />')]
    if name == text_name:
        body = (text[text.find('" body="')
                + 8:text.find('" toa="')].replace(',', ''))
        date = (text[text.find('" readable_date="')
                + 17:text.find('" contact_name="')].replace(',', ''))

        return date + ',' + body + '\n'
    else:
        return ''


def text_parser(backup_name, text_name):
    """This program takes text messages from a .xml file (specifically the
       ones created by SMS backup and restore) and parses it into a human
       readable csv file based for a certain person.  It takes in two
       parameters: backup_name, which is the name of the XML backup file i.e.
       'sms-backup-20170516.xml' (please include the .xml extension) and
       text_name i.e. 'John Smith' which is the name of the person for whom
       you want to extract the tweets.
    """
    try:
        inputfile = open(backup_name)
        outputfile = open(text_name + '.csv', 'w')

        for i in range(4):
            inputfile.next()  # skip first four lines
        for index, line in enumerate(inputfile):
            outputfile.writelines(line_parser(line, text_name))

        inputfile.close()
        outputfile.close()
        print "'{}.csv' was successfully created'".format(text_name)
    except IOError:
        print 'No file named {}'.format(backup_name)

COMMAND_LINE_DATABASE_FILE_NAME = 'command_line.txt'

def write_in_database(speaker,sentence):
    fw=open(COMMAND_LINE_DATABASE_FILE_NAME,'a')
    fw.write(speaker + "...")
    fw.write(sentence + "\n")
    fw.close()
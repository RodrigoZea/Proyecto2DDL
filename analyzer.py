"""
UVG
Diseno de Lenguajes
Sección 10
Rodrigo Zea - 17058
Proyecto 2
analyzer.py - Esta archivo se enfoca en leer el archivo con el vocabulario especificado.
"""

import re, sys, getopt
chars = {
            "pipe": chr(8746), 
            "concat": chr(8745), 
            "kleene": chr(916), 
            "lt": chr(706), 
            "gt": chr(707), 
            "qmark": chr(439), 
            "numeral": chr(8747)
        }
prec = {'+': 1, '-': 1, else: 0}

class Analyzer:
    def __init__(self, file):
        # ATG File
        self.file = file
        self.current_compiler = ""
        self.tokens = {}
        self.keywords = {}
        self.analyzer_chars = {}
        self.productions = []

    def read_file(self):
        # Init lists
        charas = []
        keywds = []

        # pw[0] = COMPILER, pw[1] = CHARS, pw[2] = KEYWD, pw[3] = TOKENS, pw[4] = PROD
        possible_words = [False, False, False, False, False]

        # Read ATG file
        for w in file:
            # Get word
            keywd = w.split()
            if len(keywd) > 0:
                # Mark keyword is "COMPILER"
                if keywd[0].lower() == 'compiler':
                    possible_words = [True, False, False, False, False]
                # Mark keyword is "CHARACTERS"
                elif keywd[0].lower() == 'characters':
                    possible_words = [False, True, False, False, False]
                # Mark keyword is "KEYWORDS"
                elif keywd[0].lower() == 'keywords':
                    possible_words = [False, False, True, False, False]
                # Mark keyword is "TOKENS"
                elif keywd[0].lower() == 'tokens':
                    possible_words = [False, False, False, True, False]
                # Mark keyword is "PRODUCTIONS"
                elif keywd[0].lower() == 'productions':
                    possible_words = [False, False, False, False, True]
                # Mark keyword is "IGNORE"
                elif keywd[0].lower() == 'ignore':
                    possible_words = [False, False, False, False, False]
                # Mark keyword is "END"
                elif keywd[0].lower() == 'end':
                    break

        tmp = ""
        # Check how the array turned out
        # KEYWD = "COMPILER"
        if possible_words[0]:
            self.current_compiler = keywd[1]
            possible_words[0] = False
        # KEYWD = "CHARACTERS"
        elif possible_words[1]: charas.append(keywd)
        # KEYWD = "KEYWORDS"
        elif possible_words[2]: keywds.append(keywd)
        # KEYWD = "TOKENS"
        elif possible_words[3]:
            tmp += keywd
        # KEYWD = "PRODUCTIONS"
        elif possible_words[3]:

    def readChars(self, characters):
        print("Reading characters")
        # Not to confuse chars and characters
        # Sugerido por companeros, utilizar otros characters en vez de '(' ')' '|'
        any_list = chars["lt"] + chars["pipe"].join(chr(i) for i in list(range(0, 127))) + chars["rt"]

        # We get anything that checks out CHR(number) and it gets replaced by the value wrapped in 
        charcounter = 0
        for c in characters:
            regex = re.findall('(CHR\([0-9]*\))', c)
            for exp in regex:
                temp = c.replace(exp, "'" + eval(exp.lower()) + "'" if eval(exp.lower()) == '"' else '"' + eval(exp.lower()) + '"')
            charcounter += 1
            characters[charcounter] = temp

        self.characters["ANY"] = any_list

        for c in characters:
            # We get the right side of the characters
            # i.e. letter = "ABCDEFGH..." we are only interested in the right part of the =
            divider = c.split('=', 1)
            useful_characters = divider[1]

            isDecorator = False
            nextc = 0
            for i in range(len(useful_characters)):
                full_char = ''
                decorator = None

                # We've read a " or '
                if (useful_characters[i] == '"' or useful_characters[i] == "'") and not isDecorator:
                    isDecorator = True
                    decorator = useful_characters[i]
                    nextc = i + 1
 
                # Decorator has been saved
                if decorator != None:
                    if (useful_characters[i] == decorator and isDecorator):
                        isDecorator = False
                        new = useful_characters[nextc:i]

                        for i in range(len(new)):
                            if i < len(new) - 1:
                                full_char += new[i] + chars["pipe"]
                            else:
                                full_char += new[i]

                        full_char += chars["lt"] + full_char + chars["rt"]

                # We've read a +
                elif (useful_characters[i] == '+' and not isDecorator):
                    full_char += ' + ' 
                # We've read a -
                elif (useful_characters[i] == '-' and not isDecorator):
                    full_char += ' - ' 

    def readKeywds(self, keywds):
        print("Reading keywords")
        for k in keywds:

    def readTokens(self, tokens):
        print("Reading tokens")
        for t in tokens:
            # We get the right side of the characters
            # i.e. letter = "ABCDEFGH..." we are only interested in the right part of the =
            divider = c.split('=', 1)
            useful_tokens = divider[1]

            isDecorator = False
                    
def main(argv):
    atg_file = []
    # get first param (name of ATG file)
    input_file = sys.argv[1]

    with open(input_file, 'r') as reader:
        for line in reader:
            if line != '\n':
                atg_file.append(line.strip())

    analyzer = Analyzer(atg_file)

if __name__ == "__main__":
   main(sys.argv[1:])
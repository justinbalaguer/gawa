import sys
import argparse
import os, os.path
from os import path

def main():
    parse_cmd_args(sys.argv[1:])

    args = sys.argv[1:]
    dir_name = args[0]
    options = args[1]

    if path.exists(dir_name):
        print('directory already exists')
    else: 
        os.mkdir(dir_name)
        os.chdir(dir_name)
        print('project successfully created')

    if str(options)=="basic":
        #BASIC
        basic = open("index.html", "w+")
        basic.write(basic_html())
        basic.close
        # css
        os.mkdir('css')
        os.chdir('css/')
        style = open("style.css","w+")
        style.close()

        os.chdir('../')

        # js
        os.mkdir('js')
        os.chdir('js/')
        script = open("script.js","w+")
        script.close()

        os.chdir('../')

        # open
        print('opening project...please wait')
        os.system("code .")
    else:
        print('invalid argument, try [basic],[basic-bs]')

def parse_cmd_args(cmd_args):
    parser = argparse.ArgumentParser(prog='gawa', usage='%(prog)s [project name] [command]')
    parser._positionals.title = 'commands'
    parser.add_argument('basic', help="Creates basic file (html,css,js)")
    if len(cmd_args) < 2:
        parser.print_help()
        sys.exit(1)
if __name__ == '__main__':
    main()

# includes
def basic_html():
    return """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Document</title>
            <link rel="stylesheet" href="./css/style.css">
        </head>
        <body>
            
        </body>
        <script src="./js/script.js"></script>
        </html>
    """
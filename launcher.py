import subprocess
import glob
import os.path
import sys


class open_files():

 def open_py(files):
    retry = open_files.retry
    for file in files:

        filename, extension = os.path.splitext(file)
        if filename != 'launcher':
            try:
                path = "E:\\twitch_controller_v0001\\"
                file = file
                os.chdir(path)
                subprocess.call(f'start python {path + file}', shell=True)
                print('file ' + file + ' opened')


            except Exception as e:
                attempt_recovery = 3
                start = 0
                while start < attempt_recovery:
                    retry(file)
                    print(e)
                    start +=1
                continue
        else:
            print('Launcher Shell Skipped')
            continue

 def retry(file):
    counter = 0
    max_attempts = 3

    while counter < max_attempts:
        opened = False
        try:
            p = subprocess.Popen(['powershell.exe',r"N:VIDEOS\twitch_bots\botv2"+ file], stdout=sys.stdout)
            p.communicate
            opened = True

            break

        except:
            counter += 1
            counter_str = str(counter)
            print ('file:: '+ file + ' ' + counter_str + ' of 10 attempts')
        print('opened process' + file)
    return opened


 def main ():
    files = glob.glob('controller_*.py')
    open_py = open_files.open_py(files)



if __name__ == '__main__':
    main = open_files.main()
    main


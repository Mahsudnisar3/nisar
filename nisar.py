import platform

arc = str(platform.uname().machine)
if 'arm' in arc:
          __import__("n").nisar()
elif 'aarch' in arc:
              __import__("n").nisar()
else:
        exit(f' Unknow device machine {arc}')

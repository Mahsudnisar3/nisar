import platform

arc = str(platform.uname().machine)
if 'arm' in arc:
          __import__("a").nisar()
elif 'aarch' in arc:
              __import__("a").nisar()
else:
        exit(f' Unknow device machine {arc}')

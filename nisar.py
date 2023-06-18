
import os,platform
os.system("git pull")
a=platform.architecture()[0]
if "64" in a:
    import t
    t.run()
elif "32" in a:
    import t32
    t.run()
















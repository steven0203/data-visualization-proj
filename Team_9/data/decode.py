import sys

s = open(sys.argv[1],"r").read().decode("big5").encode("utf8") 
open(sys.argv[1],"w").write(s) 

#!/usr/bin/python

# This program will copy, rename and decode Vaulty .vdata files back to images and videos for viewing in normal applications.
# Usage: python vaulty-decode.py <directory with .vdata files>

import sys
import os
import glob
import io

def usage():
  print "Usage: %s <path to directory with vdata files>" % sys.argv[0]
  print ""
  sys.exit()

def main(args):
  if len(args) != 2 or not os.path.isdir(args[1]):
    print "Error: Invalid Argument, please provide a valid directory name"
    usage()
  vdata_dir = args[1]
  vdata_files = glob.glob(os.path.join(vdata_dir,'*.vdata'))
  print "Found %s .vdata encoded files" % len(vdata_files)
  for vdata_file in vdata_files:
    with io.open(vdata_file,'rb') as vfdf:
      bn = os.path.basename(vdata_file)
      if vfdf.read(8) == 'obscured':
        nfn = 'decrypted_' + bn + '.jpg'
        with io.open(os.path.join(vdata_dir,nfn),'wb') as idf:
          idf.write(vfdf.read())
        print "processed %s" % nfn
      else:
        nfn = 'decrypted_' + bn + '.3gp'
        vfdf.seek(0)
        with io.open(os.path.join(vdata_dir,nfn),'wb') as idf:
          idf.write(vfdf.read())
        print "processed %s" % nfn
  print "Done!"

if __name__ == '__main__':
  main(sys.argv)

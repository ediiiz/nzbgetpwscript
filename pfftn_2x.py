#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
#
# Metapassword extractor for misformated NZB
#
# $File: MetaPW.py $
#
# Check first line "#!/usr/local/zy-pkgs/bin/python2.6" and maybe adjust it!
#
# v1.0:
# - inital version
##############################################################################
### NZBGET SCAN SCRIPT                                                     ###
# Metapassword extractor for misformated NZBs
#
# This script is filling the Unpack-password from the NZB meta tag
#
# NOTE: This script requires Python (v2 or later) to be installed on your system.
#
### NZBGET SCAN SCRIPT                                                     ###
##############################################################################

import os, re, sys
from xml.dom import minidom

POSTPROCESS_SKIP=95
POSTPROCESS_ERROR=94
POSTPROCESS_SUCCESS=93

if not 'NZBOP_SCRIPTDIR' in os.environ:
	print('*** NZBGet post-processing script ***')
	print('This script is supposed to be called from nzbget (13.0 or later).')
	sys.exit(POSTPROCESS_ERROR)

if not 'NZBNP_FILENAME' in os.environ:
	print('[WARN] Name of File not found in environment')
	sys.exit(POSTPROCESS_ERROR)

Filename = os.environ["NZBNP_FILENAME"]

try:
   nzb = open(Filename, "r")
   xmlnzb = minidom.parse(nzb)
   itemlist = xmlnzb.getElementsByTagName('meta')
   for meta in itemlist:
      try:
         if meta.getAttribute("type") == "password":
            p = (meta.firstChild.nodeValue)
      except AttributeError:
         pass
except:
   print("[ERROR] No PW found: " + Filename)
   sys.exit(POSTPROCESS_ERROR)

try:
   if p:
      print("[INFO] Password: "+ p )
      print('[NZB] NZBPR_*Unpack:Password=' + p)
      sys.exit(POSTPROCESS_SUCCESS)
except NameError:
   print("[ERROR] No PW found: " + Filename)
   sys.exit(POSTPROCESS_ERROR)

#sys.exit(POSTPROCESS_SUCCESS)
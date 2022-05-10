## ###
#  IP: GHIDRA
# 
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#  
#       http://www.apache.org/licenses/LICENSE-2.0
#  
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
##
# Imports a file with lines in the form "0xADDRESS comment" as pre comments
# @author tetracorp.github.io
# @category Data
#

from ghidra.program.model.address.Address import *
from ghidra.program.model.listing.CodeUnit import *
from ghidra.program.model.listing.Listing import *
from ghidra.program.model.symbol.SourceType import *
import string

listing = currentProgram.getListing()

f = askFile("Give me a file to open", "Go baby go!")

comments = {}

for line in file(f.absolutePath):  # note, cannot use open(), since that is in GhidraScript
  pieces = line.split(" ",1)

  address = toAddr(long(pieces[0], 16))
  comment = pieces[1]

  if address in comments.keys():
    comments[address] += comment
  else:
    comments[address] = comment

for address, comment in comments.items():
  comment = comment.strip() # remove trailing newline
  codeUnit = listing.getCodeUnitAt(address)
  print("{} {}".format(address, comment))
  codeUnit.setComment(codeUnit.PRE_COMMENT, "{}".format(comment))

#!/usr/bin/env python3

# Required parameters:
# @raycast.schemaVersion 1
# @raycast.title init
# @raycast.mode compact

# Optional parameters:
# @raycast.icon 🤖
# @raycast.argument1 { "type": "text", "placeholder": "" }
# @raycast.argument2 { "type": "text", "placeholder": "", "optional": true}

import sys

from dispatcher import dispatch

destination = sys.argv[1]
subdivision = sys.argv[2]

dispatch("init-osx", destination, subdivision)

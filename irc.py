#!/usr/bin/env python3

# Required parameters:
# @raycast.schemaVersion 1
# @raycast.title init
# @raycast.mode compact

# Optional parameters:
# @raycast.icon 🤖
# @raycast.argument1 { "type": "text", "placeholder": "Placeholder" }

import sys

from dispatch import dispatch

destination = sys.argv[1]

dispatch("init", destination, )

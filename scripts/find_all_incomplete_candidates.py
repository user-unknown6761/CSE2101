import json
import re
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

# We will build a unified extractor script and run quality checks on all extracted questions.
print("Checking extraction criteria...")

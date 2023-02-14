class color:
   ITALIC = '\033[3m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

print(color.BOLD+color.UNDERLINE+color.ITALIC + 'chain of function decorators ' + color.END)
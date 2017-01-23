import sys

def cat(filename):
  f = open(filename, 'rU') #Reading mode
  for line in f:
    print line,
  f.close()
  
def main():
  cat(sys.argv[1])

if __name__ == '__main__':
  main()
  
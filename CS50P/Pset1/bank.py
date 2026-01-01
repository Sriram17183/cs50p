def main():
  f=input("Greeting:")
  d=value(f)
  print(d)
def value(f):
  f=f.lower().strip()
  if not f.startswith("hello") and f.startswith("h"):
    return 20

  elif f.startswith("hello"):
    return 0

  else:
    return 100




if __name__=="__main__":
    main()

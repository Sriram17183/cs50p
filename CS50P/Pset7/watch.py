import re

def main():
    print(parse(input("HTML: ")))

def parse(s):
    if re.search(r'<iframe[^>]+src="https?://(www\.)?youtube\.com/embed/',s):
         f = re.sub(r'src="https?://(www\.)?youtube\.com/embed/([^"]+)"',lambda m: f'src="https://youtu.be/{m.group(2)}"',s)
         g= re.search(r'src="([^"]+)"',f)
         return g.group(1)
    else:
        return None
if __name__ == "__main__":
    main()

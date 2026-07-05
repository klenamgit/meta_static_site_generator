def extract_title(markdown:str):

    for line in markdown.splitlines():
        if line.startswith("#"):
            line=line.strip()
            line = line.replace("#","")
            return line
        else:
            raise Exception("No h1 header")
    


print("HTML Converter\n")

with open("groceries.html") as f:
    x = f.read()
    

    x = x.replace("<h1>","").replace("</h1>","").replace("<ul>","").replace("<li>","* ").replace("</li>","").replace("</ul>","")
    print(x)
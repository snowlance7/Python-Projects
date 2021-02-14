
def main():
    f = open("rules.txt", "rt")

    for line in f:
        print(line[:-1])
    
    f.close()

if __name__ == "__main__":
    main()
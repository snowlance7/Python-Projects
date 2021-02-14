import pickle

birds = dict()

def main():
    bird = input("Enter name of bird: ").lower()
    if bird != "x":
        if bird in birds:
            birds[bird] += 1
        else:
            birds[bird] = 1

        main()
    else:
        print("Name\t\tCount")
        print("=============== ===============")
        for pair in birds.items():
            print(pair[0] + "\t\t" + str(pair[1]))
        
        pickle.dump(birds, open("birds.txt","wb"))




if __name__ == "__main__":
    print("Bird Counter program")
    print("\nEnter 'x' to exit\n")
    try:
        birds = pickle.load(open("birds.txt","rb"))
    except:
        pass

    main()
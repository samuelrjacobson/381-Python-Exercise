from movies import Movies

movies = Movies('./movies.txt')

# Keep displaying menu till user enters q to quit
request = "";
while(request != "q"):
    print("\nq: quit");
    print("sn: search movie names");
    print("sc: search cast");
    print("list: print all the movie names");

    request = input();

    # Display a list of all movie names
    if(request == "list"):
        for m in movies._movies:
            print(m["name"])

    # Return results for search by movie name
    elif(request == "sn"):
        print("Enter a search term: ")
        word = input();
        for m in movies._movies:
            if(word.lower() in m["name"].lower()):
                print(m["name"])

    # Return results for search by cast names
    elif(request == "sc"):
        print("Enter a search term: ")
        word = input();
        for m in movies._movies:
            matches = [];
            for c in m["cast"]:
                if(word.lower() in c.lower()):
                    matches.append(c);
            if(len(matches) > 0):
                print(m["name"]);
                print("['", end="");
                print(*matches, sep = "' , '", end="");
                print("']");
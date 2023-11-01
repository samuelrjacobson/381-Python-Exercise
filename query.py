from movies import Movies

movies = Movies('./movies.txt')

request = ""
while(request != "q"):
    print("q: quit");
    #print("sn: search movie names");
    #print("sc: search cast");
    #print("list: print all the movie names");

    request = input()

    #if(request != "q"):
    #    print("Do something")
    
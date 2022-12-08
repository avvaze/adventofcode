with open("in.txt", "r") as f:
    data = f.read()

    # Length of the marker with distinct characters 
    mlen = 14

    i = 0
    while True:
        chars = [*data[i:i+mlen]]
        if len(set(chars)) == mlen: break
        i += 1
    
    print(f"First marker after {i+mlen} characters")

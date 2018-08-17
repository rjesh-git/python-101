def main():
    x, y = 10, 100
  
    # conditional flow uses if, elif, else  
    if(x < y):
        st= "x is less than y"
    elif (x == y):
        st= "x is same as y"
    else:
        st= "x is greater than y"
    print (st)

    x = 101
    # conditional statements let you use "a if C else b"
    st = "x is less than y" if (x < y) else "x is greater than or equal to y"
    print (st)

    check = True
    if check: print("check is true")
    
    # Python does not have support for higher-order conditionals
    # like "switch-case" in other languages

if __name__ == "__main__":
    main()


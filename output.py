def formatname(fname, lname):
    if fname == "" or lname=="":
            return
    formatedfname = fname.title()
    formatedlname = lname.title()
    return f"{formatedfname} {formatedlname}"


print(formatname(input("what is your name "), input("what is your last name")))

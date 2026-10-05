def read_file(file_name):
    file = None

    try:
        file = open(file_name, "r")
    except FileNotFoundError:
        return "__CONTENT_START__\n__NO_SUCH_FILE__\n__CONTENT_END__"
    else:
        content = file.read()
        return "__CONTENT_START__\n" + content + "__CONTENT_END__"
    finally:
        if file is not None:
            file.close()


            

print(read_file("file_does_not_exist.txt"))
print(read_file("names.txt"))
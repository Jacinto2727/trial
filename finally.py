def ErrCode():
    try:
        print("I am here,opening all files")
        return "Sucess got all files"
    except ZeroDivisionError as e:
        print(e)
    finally:
        print(" closing all files")
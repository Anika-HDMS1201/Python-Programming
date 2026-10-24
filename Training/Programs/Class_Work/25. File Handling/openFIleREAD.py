try :
    file = open("noob.txt","r") 
    content = file.read()
    print(f"File name : ",file.name)
    print(f"File open mode : ",file.mode)
    print(f"File open/close : ",file.closed) #here the file is open for work
    print(content)
    file.close() #important
    print(f"File open/close : ",file.closed)#here the file is closed
    print("Something went wrong")
except FileNotFoundError:
        print("File not found")
except Exception as e:
        print("Exception occured ",e)
from tkinter import *
from tkinter import filedialog as fd
from simplecrypt import encrypt,decrypt
import hashlib

root=Tk()
root.title("File Encryption")
root.geometry("250x190")
root.configure(bg="#74fc82")

def apply_md5():
    text_file = fd.askopenfilename(title = "Open Text File", filetypes=(("Text Files","*.txt"),))
    File_path = text_file
    read_file= open(File_path,'r')
    paragraph = read_file.read()
    bytes_str = bytes.fromhex(paragraph)
    bite=bytes_str
    file_result = hashlib.md5(bite.encode())
    cyphercode = encrypt('AIM', file_result)
    file_hexd = cyphercode.hex()
    print("Encripted code : " + file_hexd)
    print("MD5 function")
    
    
def apply_sha256():
    text_file = fd.askopenfilename(title = "Open Text File", filetypes=(("Text Files","*.txt"),))
    File_path = text_file
    read_file= open(File_path,'r')
    paragraph = read_file.read()
    bytes_str = bytes.fromhex(paragraph)
    bite = bytes_str
    file_result = hashlib.sha256(bite.encode())
    cyphercode = encrypt('AIM', file_result)
    file_hexd = cyphercode.hex()
    print("Encripted code : " + file_hexd)
    print("SHA function")   
    
    
btn=Button(root, text="Apply MD5",command=apply_md5,bg="#0a8c15",fg="#012b04")
btn.place(relx=0.3,rely=0.5, anchor=CENTER)
btn1=Button(root, text="Apply SHA256",command=apply_sha256,bg="#0a8c15",fg="#012b04")
btn1.place(relx=0.7,rely=0.5, anchor=CENTER)
root.mainloop()
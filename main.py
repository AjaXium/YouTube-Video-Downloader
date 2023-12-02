from customtkinter import *
from pytube import YouTube
import threading


app = CTk()
app.geometry("700x400+350+200")
app.title("YouTube Downloader")

#Functions

class ErrorMsg:
    def __init__(self, root, text):
        self.root = root
        self.text = text
        self.msg = CTkLabel(root, font=("Hind", 15), text=text,
                        text_color="#2A9A28")
        
def browse():
    dest = filedialog.askdirectory(title="Save Video")
    destEntry.delete(0, 'end')
    destEntry.insert(0, dest)

def download():
    link = linkEntry.get()
    dest = destEntry.get()
    YouTube(link).streams.filter(progressive=True, file_extension="mp4").order_by("resolution").desc().first().download(dest)

def onDownloadBtnClick():
    if (len(linkEntry.get()) == 0) or (len(destEntry.get()) == 0):
        if len(linkEntry.get()) == 0:
            missingLink = ErrorMsg(bgFrame, "Video Link cannot be empty, please enter a Video Link")
            missingLink.msg.place(x=250, rely=0.37, anchor="center")
            linkEntry.lift()
            app.after(2000, missingLink.msg.place_forget)
        if len(destEntry.get()) == 0:
            missingDest = ErrorMsg(bgFrame, "Video Save Destination folder cannot be empty")
            missingDest.msg.place(x=225, rely=0.57, anchor="center")
            destEntry.lift()
            app.after(2000, missingDest.msg.place_forget)
    else:
        threading.Thread(target=download).start()
    

bgFrame = CTkFrame(app, width=700, height=400, bg_color="white", fg_color="white")
bgFrame.place(relx=0.5, rely=0.5, anchor="center")

titleLabel = CTkLabel(bgFrame, text="YouTube Downloader", bg_color="white", fg_color="white", font=("Hind", 40),
                      text_color="#2A9A28")
titleLabel.place(relx=0.5, rely=0.15, anchor="center")

linkEntry = CTkEntry(bgFrame, bg_color="white", fg_color="white", border_color="#2A9A28", placeholder_text="YouTube Video Link",
                     placeholder_text_color="#9F9F9F", corner_radius=8,
                     width=600, height=40, font=("Hind", 15), text_color="black")
linkEntry.place(relx=0.5, rely=0.3, anchor="center")

destEntry = CTkEntry(bgFrame, bg_color="white", fg_color="white", border_color="#2A9A28", placeholder_text="YouTube Video Save Destination",
                     placeholder_text_color="#9F9F9F", corner_radius=8,
                     width=500, height=40, text_color="black", font=("Hind", 15))
destEntry.place(x=300, rely=0.5, anchor="center")

browseBtn = CTkButton(bgFrame, width=80, height=40, bg_color="white", fg_color="#2A9A28", hover_color="#3CB13A",
                      text="Browse", text_color="white", font=("Hind", 15), command=browse)
browseBtn.place(x=610, rely=0.5, anchor="center")

downloadBtn = CTkButton(bgFrame, width=200, height=40, bg_color="white", fg_color="#2A9A28", hover_color="#3CB13A",
                      text="DOWNLOAD", text_color="white", font=("Hind", 15), command=onDownloadBtnClick)
downloadBtn.place(relx=0.5, rely=0.7, anchor="center")

app.mainloop()
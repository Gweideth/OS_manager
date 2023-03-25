import os
import shutil
from tkinter import *
from tkinter import messagebox as mb
from tkinter import filedialog as fd


def openFile():
    file_open = fd.askopenfilename(
        title="Wybierz plik",
        filetypes=[("Wszystkie pliki", "*.*")]
    )
    os.startfile(os.path.abspath(file_open))


def copyFile():
    file_copy = fd.askopenfilename(
        title="Wybierz plik do skopiowania",
        filetypes=[("Wszystkie pliki", "*.*")]
    )
    directory_paste = fd.askdirectory(title="Wybierz lokalizację do której zostanie skopiowany plik: ")

    try:
        shutil.copy(file_copy, directory_paste)
        mb.showinfo(
            title="Plik skopiowany!",
            message="Plik pomyślnie skopiowany!"
        )

    except:
        mb.showerror(
            title="Błąd!",
            message="Nieudane kopiowanie. Sprawdź, czy podana lokalizacja istnieje."
        )


def deleteFile():
    file_delete = fd.askopenfilename(
        title="Wybierz plik do usunięcia",
        filetypes=[("Wszystkie pliki", "*.*")]
    )
    os.remove(os.path.abspath(file_delete))
    mb.showinfo(
        title="Plik usunięty!",
        message="Plik został usunięty!"
    )


def renameFile():
    rename_window = Toplevel(root)
    rename_window.title("Zmiana nazwy pliku")
    rename_window.geometry("300x100+300+250")
    rename_window.resizable(0, 0)

    rename_label = Label(
        rename_window,
        text="Enter the new file name:",
        font=("verdana", "8")
    )
    rename_label.pack(pady=4)

    rename_field = Entry(
        rename_window,
        width=26,
        textvariable=enteredFileName,
        relief=GROOVE,
        font=("verdana", "10"),
    )
    rename_field.pack(pady=4, padx=4)

    submitButton = Button(
        rename_window,
        text="Submit",
        command=submitName,
        width=12,
        relief=GROOVE,
        font=("verdana", "8")
    )
    submitButton.pack(pady=2)


def getFilePath():
    file = fd.askopenfilename(title="Wybierz plik którego chcesz zmienić nazwę")
    return file


def submitName():
    renameName = enteredFileName.get()
    enteredFileName.set("")
    fileName = getFilePath()
    newFileName = os.path.join(os.path.dirname(fileName))
    os.rename(fileName, newFileName)
    mb.showinfo(
        title="Zmieniono nazwę pliku!",
        message="Zmiana nazwy pliku zakończona sukcesem."
    )


def openFolder():
    folder = fd.askdirectory(
        title="Wybierz folder",
    )
    os.startfile(folder)


def moveFolder():
    folder_move = fd.askdirectory(
        title="Wybierz folder który chcesz przenieść"
    )
    mb.showinfo(
        message="Folder wybrany."
    )
    destination = fd.askdirectory(title="Lokalizacja")

    try:
        shutil.move(folder_move, destination)
        mb.showinfo(
            title="Folder przeniesiony!",
            message="Folder został pomyślnie przeniesiony."
        )

    except:
        mb.showerror(
            title="Przeniesienie nieudane!",
            message="Przeniesienie folderu zakończone błędem. Upewnij się że lokalizacja jest poprawna"
        )


def listFiles():
    i = 0
    folder = fd.askdirectory(title="Wybierz folder")
    files = os.listdir(os.path.abspath(folder))

    listFilesWindow = Toplevel(root)
    listFilesWindow.title(f"Pliki w {folder}")
    listFilesWindow.geometry("300x500+300+200")
    listFilesWindow.resizable(0, 0)

    listbox = Listbox(
        listFilesWindow,
        font=("Verdana", "10"),
    )
    listbox.place(relx=0, rely=0, relheight=1, relwidth=1)

    scrollbar = Scrollbar(
        listbox,
        orient=VERTICAL,
        command=listbox.yview
    )

    scrollbar.pack(side=RIGHT, fill=Y)

    listbox.config(yscrollcommand=scrollbar.set)

    while i < len(files):
        listbox.insert(END, str(i + 1) + ". " + files[i])
        i += 1

    listbox.insert(END, "")
    listbox.insert(END, "Wszystkie pliki: " + str(len(files)))


if __name__ == "__main__":
    root = Tk()
    root.title("OS Manager")
    root.geometry("300x500+650+250")
    root.resizable(0, 0)

    header_frame = Frame(root)
    buttons_frame = Frame(root)

    header_frame.pack(fill="both")
    buttons_frame.pack(expand=TRUE, fill="both")

    header_label = Label(
        header_frame,
        text="Eksplorator plików",
        font=("verdana", "16"),
    )

    header_label.pack(expand=TRUE, fill="both", pady=12)

    open_button = Button(
        buttons_frame,
        text="Otwórz plik",
        font=("verdana", "10"),
        width=18,
        relief=GROOVE,
        command=openFile
    )

    copy_button = Button(
        buttons_frame,
        text="Skopiuj plik",
        font=("verdana", "10"),
        width=18,
        relief=GROOVE,
        command=copyFile
    )

    delete_button = Button(
        buttons_frame,
        text="Usuń plik",
        font=("verdana", "10"),
        width=18,
        relief=GROOVE,
        command=deleteFile
    )

    rename_button = Button(
        buttons_frame,
        text="Zmień nazwę pliku",
        font=("verdana", "10"),
        width=18,
        relief=GROOVE,
        command=renameFile
    )

    open_folder_button = Button(
        buttons_frame,
        text="Otwórz folder",
        font=("verdana", "10"),
        width=18,
        relief=GROOVE,
        command=openFolder
    )

    delete_folder_button = Button(
        buttons_frame,
        text="Usuń folder",
        font=("verdana", "10"),
        width=18,
        relief=GROOVE,
        command=deleteFile
    )

    move_folder_button = Button(
        buttons_frame,
        text="Przenieś folder",
        font=("verdana", "10"),
        width=18,
        relief=GROOVE,
        command=moveFolder
    )

    list_button = Button(
        buttons_frame,
        text="Lista plików w folderze",
        font=("verdana", "10"),
        width=18,
        relief=GROOVE,
        command=listFiles
    )

    open_button.pack(pady=8)
    copy_button.pack(pady=8)
    delete_button.pack(pady=8)
    rename_button.pack(pady=8)
    open_folder_button.pack(pady=8)
    delete_folder_button.pack(pady=8)
    move_folder_button.pack(pady=8)
    list_button.pack(pady=8)

    enteredFileName = StringVar()

    root.mainloop()

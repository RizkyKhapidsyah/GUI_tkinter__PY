import tkinter

def event_tekan():
    label2 = tkinter.Label(main_window, text = "Tombol Dipijit!")
    label2.pack()

main_window = tkinter.Tk()
label = tkinter.Label(main_window, text = "Halo, saya Rizky Khapidsyah")
tombol = tkinter.Button(main_window, text = "OK", command = event_tekan)

label.pack()
tombol.pack()

main_window.mainloop()

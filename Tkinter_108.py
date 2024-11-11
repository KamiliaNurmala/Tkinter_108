import tkinter as tk  # Mengimpor modul tkinter untuk GUI
from tkinter import ttk  # Mengimpor ttk 
from tkinter import messagebox  # Mengimpor messagebox 

# Fungsi untuk menampilkan hasil prediksi
def prediksi_prodi():
    try:
        # Memeriksa apakah semua input nilai berada dalam rentang 0-100
        for entry in input_fields:
            nilai = int(entry.get())  # Mengonversi nilai input menjadi integer
            if not (0 <= nilai <= 100): # Memeriksa apakah nilai berada dalam rentang 0-100
                raise ValueError("Nilai harus antara 0 dan 100") # Menghasilkan kesalahan jika nilai di luar rentang
        
        # Menampilkan hasil prediksi jika semua input valid
        hasil_label.config(text="Prediksi Prodi: Teknologi Informasi")
    except ValueError:
        # Menampilkan pesan kesalahan jika input tidak valid
        messagebox.showerror("Input Error", "Pastikan semua input adalah angka antara 0 dan 100")

# Membuat jendela utama aplikasi
root = tk.Tk()
root.title("Aplikasi Prediksi Prodi Pilihan") # Menetapkan judul jendela aplikasi
root.geometry("500x500")  # Mengatur ukuran jendela aplikasi
root.configure(bg="#4373dd")  # Menyetel warna latar belakang aplikasi

# Label judul
judul_label = tk.Label(root, text="Aplikasi Prediksi Prodi Pilihan", font=("Arial", 16, "bold"), bg="#4373dd", fg="white") #membuat label judul aplikasi
judul_label.pack(pady=10)  # Menempatkan label judul di bagian atas dengan padding

# Frame untuk input nilai mata pelajaran
frame_nilai = tk.Frame(root, bg="#4373dd")  # Frame untuk mengelompokkan input nilai
frame_nilai.pack(pady=10)  # Menempatkan frame dengan padding vertikal

# Membuat 10 input nilai mata pelajaran
input_fields = []
for i in range(10):
    label = tk.Label(frame_nilai, text=f"Nilai Mata Pelajaran {i+1}:", bg="#4373dd", fg="white") # membuat label untuk setiap mata pelajaran
    label.grid(row=i, column=0, padx=5, pady=5, sticky="w")  # Label untuk tiap mata pelajaran
    
    entry = tk.Entry(frame_nilai, width=20)  # Input nilai untuk tiap mata pelajaran
    entry.grid(row=i, column=1, padx=5, pady=5) # Menempatkan entry di kolom kedua
    input_fields.append(entry)  # Menyimpan setiap input dalam daftar

# Tombol untuk memproses hasil prediksi
prediksi_button = ttk.Button(root, text="Hasil Prediksi", command=prediksi_prodi) 
prediksi_button.pack(pady=20)  # Menempatkan tombol di bawah frame input nilai

# Label untuk menampilkan hasil prediksi
hasil_label = tk.Label(root, text="", font=("Times New Roman", 14), bg="#4373dd", fg="white", width=30)
hasil_label.pack(pady=10)  # Menempatkan label hasil di bagian bawah tombol prediksi

# Menjalankan aplikasi
root.mainloop()

import tkinter as tk

def celsius_a_fahrenheit():
    celsius = float(entrada_celsius.get())
    fahrenheit = (celsius * 9/5) + 32
    entrada_fahrenheit.delete(0, tk.END)
    entrada_fahrenheit.insert(0, f"{fahrenheit:.2f}")

def fahrenheit_a_celsius():
    fahrenheit = float(entrada_fahrenheit.get())
    celsius = (fahrenheit - 32) * 5/9
    entrada_celsius.delete(0, tk.END)
    entrada_celsius.insert(0, f"{celsius:.2f}")

def limpiar():
    entrada_celsius.delete(0, tk.END)
    entrada_fahrenheit.delete(0, tk.END)

ventana = tk.Tk()
ventana.title("Conversor de Temperatura")

label_celsius = tk.Label(ventana, text="Celsius")
label_celsius.grid(row=0, column=0, padx=10, pady=10)

label_fahrenheit = tk.Label(ventana, text="Fahrenheit")
label_fahrenheit.grid(row=1, column=0, padx=10, pady=10)

entrada_celsius = tk.Entry(ventana)
entrada_celsius.grid(row=0, column=1, padx=10, pady=10)

entrada_fahrenheit = tk.Entry(ventana)
entrada_fahrenheit.grid(row=1, column=1, padx=10, pady=10)

boton_c_to_f = tk.Button(ventana, text="Celsius a Fahrenheit", command=celsius_a_fahrenheit)
boton_c_to_f.grid(row=2, column=0, padx=10, pady=10)

boton_f_to_c = tk.Button(ventana, text="Fahrenheit a Celsius", command=fahrenheit_a_celsius)
boton_f_to_c.grid(row=2, column=1, padx=10, pady=10)

boton_limpiar = tk.Button(ventana, text="Limpiar", command=limpiar)
boton_limpiar.grid(row=3, columnspan=2, padx=10, pady=10)

ventana.mainloop()

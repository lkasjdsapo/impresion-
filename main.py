import tkinter as tk
from documento import Documento
from cola_impresion import Cola 


cola = Cola()

documento_actual = None
pagina_actual = 0
imprimiendo = False
def agregar_documento():

    nombre = entrada_nombre.get()
    paginas = int(entrada_paginas.get())
    tiempo = float(entrada_tiempo.get())

    documento = Documento(nombre, paginas, tiempo)

    cola.agregar(documento)

    texto.insert(
        tk.END,
        "Documento agregado: " + nombre + "\n"
    )

    entrada_nombre.delete(0, tk.END)
    entrada_paginas.delete(0, tk.END)
    entrada_tiempo.delete(0, tk.END)

    estado.config(
        text="Documentos en cola: " + str(cola.cantidad())
    )


def iniciar():

    global imprimiendo

    if cola.vacia():
        estado.config(text="No hay documentos en cola")
        return

    if not imprimiendo:
        imprimiendo = True
        imprimir()


def imprimir():

    global documento_actual
    global pagina_actual
    global imprimiendo

    if not imprimiendo:
        return

    if documento_actual is None:

        documento_actual = cola.sacar()
        pagina_actual = 0

        texto.insert(
            tk.END,
            "\nImprimiendo: " +
            documento_actual.nombre + "\n"
        )

    pagina_actual = pagina_actual + 1

    estado.config(
        text="Imprimiendo " +
        documento_actual.nombre +
        " - Página " +
        str(pagina_actual) +
        " de " +
        str(documento_actual.paginas)
    )

    texto.insert(
        tk.END,
        "Página " +
        str(pagina_actual) +
        " de " +
        str(documento_actual.paginas) +
        "\n"
    )

    if pagina_actual == documento_actual.paginas:

        texto.insert(
            tk.END,
            documento_actual.nombre +
            " terminado\n"
        )

        documento_actual = None

        if cola.vacia():

            imprimiendo = False

            estado.config(
                text="No hay documentos en cola"
            )

        else:

            ventana.after(
                100,
                imprimir
            )

    else:

        ventana.after(
            int(documento_actual.tiempo * 1000),
            imprimir
        )


def detener():

    global imprimiendo

    imprimiendo = False

    estado.config(
        text="Impresión detenida"
    )

    texto.insert(
        tk.END,
        "Impresión detenida\n"
    )


ventana = tk.Tk()

ventana.title("Simulador de Impresora")

ventana.geometry("600x500")



tk.Label(
    ventana,
    text="SIMULADOR DE IMPRESORA",
    font=("Arial", 18)
).pack(pady=10)


tk.Label(
    ventana,
    text="Nombre del documento"
).pack()

entrada_nombre = tk.Entry(ventana)

entrada_nombre.pack()



tk.Label(
    ventana,
    text="Número de páginas"
).pack()

entrada_paginas = tk.Entry(ventana)

entrada_paginas.pack()



tk.Label(
    ventana,
    text="Tiempo por página"
).pack()

entrada_tiempo = tk.Entry(ventana)

entrada_tiempo.pack()



tk.Button(
    ventana,
    text="Agregar documento",
    command=agregar_documento
).pack(pady=10)



tk.Button(
    ventana,
    text="Iniciar impresión",
    command=iniciar
).pack(pady=5)



tk.Button(
    ventana,
    text="Detener impresión",
    command=detener
).pack(pady=5)



estado = tk.Label(
    ventana,
    text="No hay documentos en cola"
)

estado.pack(pady=10)



texto = tk.Text(
    ventana,
    width=65,
    height=12
)

texto.pack()

    
# Ejecutar ventana

ventana.mainloop()

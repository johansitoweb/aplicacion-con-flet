import flet as ft

def main(page: ft.Page):
    page.title = "Contador"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    contador = 0

    def incrementar(e):
        nonlocal contador
        contador += 1
        conteo.value = str(contador)
        page.update()

    def decrementar(e):
        nonlocal contador
        contador -= 1
        conteo.value = str(contador)
        page.update()

    conteo = ft.Text(value=str(contador), style="headline4")

    page.add(
        conteo,
        ft.Row(
            [
                ft.ElevatedButton("Incrementar", on_click=incrementar),
                ft.ElevatedButton("Decrementar", on_click=decrementar),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        ),
    )

ft.app(target=main)

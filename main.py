import flet as ft


def main(page: ft.Page):
    page.bgcolor = ft.colors.BLACK
    page.title = 'Svitlo Sumy'
    page.window_width = 400
    page.window_height = 700
    page.window_resizable = True
    page.navigation_bar = ft.NavigationBar(height=80, bgcolor=ft.colors.BLACK, on_change = lambda e: print(e.control.selected_index),
                                           destinations=[
                                               ft.NavigationDestination(
                                                   icon=ft.icons.LIST_ROUNDED, label='Черги',),
                                               ft.NavigationDestination(
                                                   icon=ft.icons.HOME_ROUNDED, label='Головна'),
                                               ft.NavigationDestination(
                                                   icon=ft.icons.INFO, selected_icon=ft.icons.INFO_OUTLINE, label='Інформація')
                                           ]
                                           )
    time_cherg = ft.Container(
        content=ft.Text('Перша Черга:', size=20),
        alignment=ft.alignment.center,
        margin=10,
        height=60,
        width=200,
        padding=10,
        border_radius=10,
        bgcolor=ft.colors.RED,
        visible=False
    )
    name_cherg = ft.Container(
        content=ft.Text('06:00 - 08:00', size=20),
        alignment=ft.alignment.center,
        margin=10,
        height=100,
        padding=10,
        border_radius=10,
        bgcolor=ft.colors.GREEN,
    )
    img = ft.Image(
        src=f'./Images/lamp.jpg',
        border_radius=10,
        width=300,
        height=300,
        fit=ft.ImageFit.CONTAIN,
    )

    page.vertical_alignment = 'End'
    page.add(img, time_cherg, name_cherg)
    page.update()


ft.app(target=main)

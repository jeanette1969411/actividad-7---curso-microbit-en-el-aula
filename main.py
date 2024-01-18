def on_forever():
    if input.button_is_pressed(Button.A):
        basic.show_string("jeanette da la bienvenida")
    else:
        basic.show_string("alumno del jardin")
basic.forever(on_forever)

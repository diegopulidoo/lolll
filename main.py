def pulsador_suma():
    basic.show_string("2+2=4")

def pulsador_resta():
    basic.show_string("2-1=1")

input.on_button_pressed(Button.A, pulsador_suma)
input.on_button_pressed(Button.B, pulsador_resta)
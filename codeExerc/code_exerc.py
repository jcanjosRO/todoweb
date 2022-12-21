import PySimpleGUI as sg
import functions as fc


label1 = sg.Text("Digite quantidade em feet: ")
input1 = sg.Input()

label2 = sg.Text("Digite quantidade em inches: ")
input2 = sg.Input()


convert_button = sg.Button("Converter")

saida_label = sg.Text(key="output", text_color="white")

window = sg.Window("Convertor para Metros",
                   layout=[[label1, input1],
                            [label2, input2],
                             [convert_button, saida_label]])

while True:
    event,values = window.read()
   # print(1, event)
  #  print(2, values)

    match event:
        case "Converter":
            feet = int(values[0])
            inches = int(values[1])
          #  print(feet, inches)

            result = fc.convert(feet, inches)
            window["output"].update(value=f"{result} m")

        case sg.WIN_CLOSED:
            break

window.close()


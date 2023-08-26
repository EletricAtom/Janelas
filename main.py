import PySimpleGUI as sg
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

year = [2002,2003,2004,2005]
unemployement_rate =[9,8,71,23]


def create_plot(year, unemployement_rate):
    plt.plot(year, unemployement_rate,color='blue',marker='o')
    plt.title("Unenployement Rate vs Year",fontsize=14)
    plt.xlabel('Year', fontsize=14)
    plt.ylabel('Unemployement Rate', fontsize=14)
    plt.grid(True)
    #plt.show()
    return plt.gcf()

layout = [[sg.Text('Line Plot')],
          [sg.Canvas(size=(500,500),key='-CANVAS-')],
          [sg.Exit()]]

def draw_figure(canvas,figure):
    figure_canvas_agg = FigureCanvasTkAgg(figure,canvas)
    figure_canvas_agg.draw()
    figure_canvas_agg.get_tk_widget().pack(side='top',fill='both',expand=1)
    return figure_canvas_agg

window = sg.Window('PysimpleGUI + Matplotlib',layout,finalize=True,element_justification='center')

draw_figure(window['-CANVAS-'].TKCanvas, create_plot(year, unemployement_rate))

while True:
    event,values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
        break

window.close()


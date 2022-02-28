import PySimpleGUI as Sg
from datetime import datetime, timedelta


class DateCalculator:

    def __init__(self) -> None:
        self.d_format = '%m / %d / %Y'
        self.current_date = datetime.now()
        self.days_to_add = 0
        self.future_date = datetime.now()
        self.past_date = datetime.now()
        self.add_or_sub = True
        self.icon = "wm-logo.ico"
        self.r_font = ('Verdana', 12)
        self.h_font = ('Arial bold', 20)
        self.e = None
        self.v = None
        self.calc_layout = [[Sg.Text(self.getsdate(), pad=(5, 5), key='cdate', border_width=2, relief='sunken')],
                            [Sg.InputText(0, 5, key='-INPUT-', pad=(2, 2), border_width=1, justification='right')],
                            [Sg.Text(self.getsdate('p'), pad=(5, 5), key='pdate',
                                     border_width=1, relief='sunken')],
                            [Sg.Text(self.getsdate('f'), pad=(5, 5), key='fdate',
                                     border_width=1, relief='sunken')]]
        self.layout = [[Sg.Text('Date Calculator', justification='c', font=self.h_font, size=(20, 1),
                                relief='ridge', border_width=1)], [Sg.Frame('Calculate date:', self.calc_layout,
                                                                            border_width=1,
                                                                            element_justification='center',
                                                                            expand_x=True)],
                       [Sg.Button('Calc', key='calc', button_color=("#000000", "#991a1a")),
                        Sg.Exit(button_color=("#000000", "#991a1a"))]]
        self.calculator = Sg.Window('Calculator', self.layout, icon=self.icon, ttk_theme='aqua',
                                    element_justification='center', element_padding=(10, 10), margins=(5, 5),
                                    font=self.r_font, finalize=True)

    def getsdate(self, t='c'):
        if t == 'p':
            return datetime.strftime(self.past_date, self.d_format)
        elif t == 'f':
            return datetime.strftime(self.future_date, self.d_format)
        else:
            return datetime.strftime(self.current_date, self.d_format)

    def exec_calc(self) -> None:
        while True:  # The Event Loop
            self.e, self.v = self.calculator.read()
            self.days_to_add = int(self.v['-INPUT-'])
            self.future_date = self.current_date + timedelta(days=self.days_to_add)
            self.past_date = self.current_date + timedelta(days=-self.days_to_add)
            self.calculator['fdate'].update(self.getsdate('f'))
            self.calculator['pdate'].update(self.getsdate('p'))
            print(self.days_to_add)
            print(self.future_date)
            # if self.e == 'calc':
            # self.calc_date()

            # if self.e == '-INPUT-':
            # print('input')
            # print(self.calculator['-INPUT-'].get())
            if self.e == Sg.WIN_CLOSED or self.e == 'Exit':
                break

        self.calculator.close()


DateCalculator().exec_calc()

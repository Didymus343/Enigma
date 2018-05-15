import tkinter as tk


class SimpleTableInput(tk.Frame):
    def __init__(self, parent, rows, columns):
        tk.Frame.__init__(self, parent, bg='blue')

        self._entry = {}
        self.rows = rows
        self.columns = columns

        # register a command to use for validation
        vcmd = (self.register(self._validate), "%P")

        # create the table of widgets
        for row in range(self.rows):
            for column in range(self.columns):
                index = (row, column)
                e = tk.Entry(self, validate="key", validatecommand=vcmd)
                e.grid(row=row, column=column, stick="nsew",padx=1, pady=1)
                self._entry[index] = e
        # adjust column weights so they all expand equally
        for column in range(self.columns):
            self.grid_columnconfigure(column, weight=1)
        # designate a final, empty row to fill up any extra space
        self.grid_rowconfigure(rows, weight=1)

    def get(self):
        '''Return a list of lists, containing the data in the table'''
        result = []
        for row in range(self.rows):
            current_row = []
            for column in range(self.columns):
                index = (row, column)
                current_row.append(self._entry[index].get())
            result.append(current_row)
        return result
    
    def getDict(self):
        '''Return a dictionary, containing the data in the table'''
        result = {}
        for row in range(self.rows):
            for column in range(self.columns):
                index = (row, column)
                result[index]=(self._entry[index].get())
           
        return result

    def _validate(self, P):
        '''Perform input validation. 

        Allow only an empty value, or a value that can be converted to a float
        '''
        if P.strip() == "":
            return True

        try:
            f = int(P)
        except ValueError:
            self.bell()
            return False
        return True
    
class TableOutput(tk.Frame):
    def __init__(self, parent, rows, columns, RowColumnLibrary):
        tk.Frame.__init__(self, parent, bg='blue')
        
        self.RowColumnLibrary = RowColumnLibrary
        self._entry = {}
        self.rows = rows
        self.columns = columns

        
        # create the table of widgets
        for row in range(self.rows):
            for column in range(self.columns):
                index = (row, column)
                Number = tk.Label(self, text=self.RowColumnLibrary[index])
                Number.grid(row=row, column=column, stick="nsew", padx=1, pady=1)
                
        # adjust column weights so they all expand equally
        for column in range(self.columns):
            self.grid_columnconfigure(column, weight=1)
        # designate a final, empty row to fill up any extra space
        self.grid_rowconfigure(rows, weight=1)
    
class Example(tk.Frame):
    def __init__(self, parent):
        self.Results =[]
        tk.Frame.__init__(self, parent)
        self.container = tk.Frame(self)
        self.container.pack()
        
        self.table = SimpleTableInput(self.container, 6, 6)
        self.submit = tk.Button(self, text="Submit", command=self.on_submit)
        self.dict = tk.Button(self, text="Get Dictionary", command=self.on_dict)
        self.table.grid(row=0, column=0, sticky='nsew')
        self.submit.pack(side="bottom")
        self.dict.pack(side="bottom")

    def on_submit(self):
        print(self.table.get())
        
    def on_dict(self):
        TempDict = self.table.getDict()
        self.dictTabel = TableOutput(self.container, 6, 6, TempDict)
        self.dictTabel.grid(row=0, column=0, sticky='nsew')
        

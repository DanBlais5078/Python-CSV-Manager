#This module defines the View class of the application. It contains a class which represents the application window, as well
#as methods which are used to build the various components of the Window. All events are handled through callback methods
#which pass the event to the Controller module for processing. 

#Author: Dan Blais - 040826486
#Subject: CST8333
#Due Date: October 13, 2024

#Note on code reference: The CodersLegacy reference was loosely followed to learn how to make treeview cells editable.
#All code in the tutorial was rewritten and modified for this program to fit in an MVC architecture.

#Images
#Search icon by Icons8, Close icon by Icons8, 1 icon by Icons8

#References
#[1] Siddiqi, "How to Make Ttk Treeview Editable in Python," CodersLegacy, 2023. [Online]. 
#            Available: https://coderslegacy.com/how-to-make-ttk-treeview-editable-python/. [Accessed: 24-Sep-2024].
#[2] "Tkinter Documentation," TkDocs, [Online]. Available: https://tkdocs.com/index.html. [Accessed: 25-Sep-2024].

import tkinter as tk
from tkinter import PhotoImage, ttk, Menu, filedialog

class ProgramWindow:
    '''
    A class that creates a program window for managing CSV files.

    This class provides a graphical user interface to open, edit, 
    and save CSV files, including functionalities to search, 
    add, and delete rows in a table representation of the CSV data.

    :attribute fileOpenCallback: Callback for opening a CSV file.
    :attribute addDataCallback: Callback for adding new data to the table.
    :attribute editDataCallback: Callback for editing existing data.
    :attribute deleteRowCallback: Callback for deleting selected rows.
    :attribute searchTableCallback: Callback for searching within the table.
    :attribute showSearchCallback: Callback for showing or hiding the search box.
    :attribute toggleButtonCallback: Callback for toggling the search button.
    :attribute openContextMenuCallback: Callback for opening context menus.
    :attribute openTextInputCallback: Callback for opening text input for editing.
    :attribute reloadDataFromFileCallback: Callback for reloading data from a file.
    :attribute saveFileCallback: Callback for saving the current file.
    :attribute saveFileAsCallback: Callback for saving the file with a new name.
    :attribute resizeSearchBoxCallback: Callback for resizing the search box.
    :attribute openRowDetailsCallback: Callback for viewing details of a row.
    '''
    
    def __init__(self, fileOpenCallback, addDataCallback, editDataCallback, deleteRowCallback, 
                 searchTableCallback, showSearchCallback, toggleButtonCallback, openContextMenuCallback,
                 openTextInputCallback, reloadDataFromFileCallback, saveFileCallback, saveFileAsCallback,
                 resizeSearchBoxCallback, openRowDetailsCallback):
        '''
        Initializes the ProgramWindow class.

        Sets up the main window, including the menu bar and initial widgets. Define callbacks to controller methods.

        :param fileOpenCallback: Callback for opening a CSV file.
        :param addDataCallback: Callback for adding new data to the table.
        :param editDataCallback: Callback for editing existing data.
        :param deleteRowCallback: Callback for deleting selected rows.
        :param searchTableCallback: Callback for searching within the table.
        :param showSearchCallback: Callback for showing or hiding the search box.
        :param toggleButtonCallback: Callback for toggling the search button.
        :param openContextMenuCallback: Callback for opening context menus.
        :param openTextInputCallback: Callback for opening text input for editing.
        :param reloadDataFromFileCallback: Callback for reloading data from a file.
        :param saveFileCallback: Callback for saving the current file.
        :param saveFileAsCallback: Callback for saving the file with a new name.
        :param resizeSearchBoxCallback: Callback for resizing the search box.
        :param openRowDetailsCallback: Callback for viewing details of a row.
        '''
        super().__init__()
        self._fileOpenCallback = fileOpenCallback
        self._addDataCallback = addDataCallback
        self._editDataCallback = editDataCallback
        self._deleteRowCallback = deleteRowCallback
        self._searchTableCallback = searchTableCallback
        self._showSearchCallback = showSearchCallback
        self._toggleButtonCallback = toggleButtonCallback
        self._openContextMenuCallback = openContextMenuCallback
        self._openTextInputCallback = openTextInputCallback
        self._reloadDataFromFileCallback = reloadDataFromFileCallback
        self._saveFileCallback = saveFileCallback
        self._saveFileAsCallback = saveFileAsCallback
        self._resizeSearchBoxCallback = resizeSearchBoxCallback
        self._openRowDetailsCallback = openRowDetailsCallback
        
        self.setupWindow()

    def setupWindow(self):
        '''
        Sets up the main window and initializes UI components.

        Configures the window title, size, menu bar, and initial labels. Also binds search, reload, and overwrite
        callbacks to hotkeys.
        '''
        self.root = tk.Tk()
        self.root.title('CSV File Manager - By Dan Blais')
        self.root.geometry("800x600")
        self.root.minsize(width=800, height=600)
        self.root.bind("<Control-f>", lambda event: self._showSearchCallback())
        self.root.bind("<Control-r>", lambda event: self._reloadDataFromFileCallback())
        self.root.bind("<Control-s>", lambda event: self._saveFileCallback())
        
        self.appBar = Menu(self.root)
        self.root.config(menu=self.appBar)
        
        self.startLabel = tk.Label(self.root, text="No .csv sheet open.\nFile > New to create a new sheet. (Not Implemented yet)\n"
                                                   "File > Open to open an existing .csv file.") 
        self.startLabel.pack(expand=True)
        
        self.searchImg = PhotoImage(file="res/search.png").subsample(4)
        self.firstImg = PhotoImage(file="res/first.png").subsample(4)
        self.closeImg = PhotoImage(file="res/close.png").subsample(5)
        
        self.buildFileMenu(self.appBar) 
        self.buildViewMenu(self.appBar)
        self.buildDataMenu(self.appBar)
        self.buildHelpMenu(self.appBar)
        
    def buildFileMenu(self, appBar):
        '''
        Builds the File menu in the application menu bar.

        :param appBar: The main menu bar of the application.
        '''
        self.fileMenu = Menu(appBar, tearoff=0)
        self.fileMenu.add_command(label='New', state=tk.DISABLED) #Not implemented yet.
        self.fileMenu.add_command(label='Open', command=lambda: self._fileOpenCallback())
        self.fileMenu.add_command(label='Save', command=lambda: self._saveFileCallback(), state=tk.DISABLED)
        self.fileMenu.add_command(label='Save As...', command=lambda: self._saveFileAsCallback(), state=tk.DISABLED)
        self.fileMenu.add_command(label='Quit', command=lambda: self.root.quit())
        self.appBar.add_cascade(label='File', menu=self.fileMenu)
        
    def buildViewMenu(self, appBar):
        '''
        Builds the View menu in the application menu bar.

        :param appBar: The main menu bar of the application.
        '''
        self.viewMenu = Menu(appBar, tearoff=0)
        self.viewMenu.add_command(label='Dark Mode', state=tk.DISABLED) #Not implemented yet.
        self.appBar.add_cascade(label='View', menu=self.viewMenu)
        
    def buildDataMenu(self, appBar):
        '''
        Builds the Data menu in the application menu bar.

        :param appBar: The main menu bar of the application.
        '''
        self.dataMenu = Menu(appBar, tearoff=0)
        self.dataMenu.add_command(label='Reload Data from File', command=lambda: self._reloadDataFromFileCallback(), state=tk.DISABLED)
        self.dataMenu.add_command(label='Change Displayed Rows', state=tk.DISABLED) #Not implemented yet.
        self.appBar.add_cascade(label='Data', menu=self.dataMenu)
        
    def buildHelpMenu(self, appBar):
        '''
        Builds the Help menu in the application menu bar.

        :param appBar: The main menu bar of the application.
        '''
        self.helpMenu = Menu(appBar, tearoff=0)
        self.helpMenu.add_command(label='Program Hotkeys', command=lambda: self.buildInfoBox("Program Hotkeys", "Double-click: Double-click on cell to edit.\n\nEnter: " 
                                                                                             "While cell edit is open to save changes.\n\nEscape: While cell edit open" 
                                                                                             "to cancel edit\n\nRight-click: On a row to open context menu.\n\nCtrl+f: To search," 
                                                                                             "click the search icon to toggle between find first and find all mode.\n\nCtrl+r: "
                                                                                             "To reload data from file.\n\nCtrl+s: To save and overwrite file."))
        
        self.helpMenu.add_command(label='Usage Guide', command=lambda: self.buildInfoBox("Usage Guide", "This program allows for the creation of new .csv files (unimplemented),\n" 
                                                                                         "and the management of existing .csv files.\n\n--Opening Files--\n\n    To begin, open an "
                                                                                         "existing .csv file by selecting File > Open. After selecting a file, a table containing the " 
                                                                                         "contents of the\n    file will open. Once a file is open a table containing a specified number "
                                                                                         "of rows will be displayed, populated with the .csv\n    data. \n\n--Editing Rows--\n\n    Double-clicking "
                                                                                         "a cell will allow a cell value to be edited. Pressing Escape will cancel editing, while pressing Enter "
                                                                                         "will confirm\n    the update. \n\n--Adding and Deleting a Row--\n\n    Right-clicking a row will dispay a "
                                                                                         "context menu providing options such as inserting new rows, and deleting rows."
                                                                                         "\n\n--Selecting Rows--\n\n    Ctrl+f will display a search field which will allow two kinds"
                                                                                         "of searching. The default is find all, where all rows containing values\n    matching the search query are"
                                                                                         "highlighted. Clicking the magnifying glass icon will toggle find first mode. In this "
                                                                                         "mode, the first\n    row containing a matching Row Id is highlighted. \n\n--Reloading and Saving Data--\n\n    "
                                                                                         "The toolbar contains other options, some of which have hotkeys (see: Program Hotkeys). Other options include: "
                                                                                         "Reloading\n    data from the .csv file, and 'overwrite' and 'save as' options."))
        self.appBar.add_cascade(label='Help', menu=self.helpMenu)
        
    def buildCSVTable(self):
        '''
        Builds the CSV table in the application window.

        Initializes the Treeview widget to display the CSV data and sets up
        the necessary scrollbars and context menu.

        '''
        self.table = ttk.Treeview(self.root, columns=("Date", "Month", "Year", "Company", "Pipeline", "Key Point", "Latitude", "Longitude",
                         "Direction of Flow", "Trade Type", "Product", "Throughput", "Committed Volumes",
                         "Uncommitted Volumes", "Nameplate Capacity", "Available Capacity", "Reason For Variance"))
        
        self.table.heading("#0", text="Row")
        self.table.heading("Date", text="Date")
        self.table.heading("Month", text="Month")
        self.table.heading("Year", text="Year")
        self.table.heading("Company", text="Company")
        self.table.heading("Pipeline", text="Pipeline")
        self.table.heading("Key Point", text="Key Point")
        self.table.heading("Latitude", text="Latitude")
        self.table.heading("Longitude", text="Longitude")
        self.table.heading("Direction of Flow", text="Direction of Flow")
        self.table.heading("Trade Type", text="Trade Type")
        self.table.heading("Product", text="Product")
        self.table.heading("Throughput", text="Throughput")
        self.table.heading("Committed Volumes", text="Committed Volumes")
        self.table.heading("Uncommitted Volumes", text="Uncommitted Volumes")
        self.table.heading("Nameplate Capacity", text="Nameplate Capacity")
        self.table.heading("Available Capacity", text="Available Capacity")
        self.table.heading("Reason For Variance", text="Reason For Variance")
        
        self.scrollVert = ttk.Scrollbar(self.root, orient='vertical', command=self.table.yview)
        self.scrollHor = ttk.Scrollbar(self.root, orient='horizontal', command=self.table.xview)
        self.table.configure(yscrollcommand=self.scrollVert.set)
        self.table.configure(xscrollcommand=self.scrollHor.set)
        self.scrollVert.pack(side="right", fill="y")
        self.scrollHor.pack(side="bottom", fill="x")
        
        self.contextMenu = Menu(self.table, tearoff=0)
        self.contextMenu.add_command(label="View Row Details", command=lambda: self._openRowDetailsCallback())
        self.contextMenu.add_command(label="Highlight Row(s)", state=tk.DISABLED) #Not implemented
        self.contextMenu.add_separator()
        self.contextMenu.add_command(label="Move Row Up", state=tk.DISABLED) #Not implemented
        self.contextMenu.add_command(label="Move Row Down", state=tk.DISABLED) #Not implemented
        self.contextMenu.add_separator()
        self.contextMenu.add_command(label="Add Row Above", command=lambda: self._addDataCallback("above"))
        self.contextMenu.add_command(label="Add Row Below", command=lambda: self._addDataCallback("below"))
        self.contextMenu.add_separator()
        self.contextMenu.add_command(label="Delete Row(s)", command=lambda: self._deleteRowCallback()) #Single delete impemented, multi-delete not implemented yet
        
        self.table.bind("<Double-1>", lambda event: self._openTextInputCallback(event))
        self.table.bind("<Button-3>", lambda event: self._openContextMenuCallback(event))
        
        self.table.tag_configure("hidden", foreground="lightgray")
        
        self.table.pack(side="top", fill="both", expand=True)
        
    def buildSearchBox(self):
        '''
        Builds the search box for filtering table entries.

        Initializes the search frame, button, and entry field, and sets up
        the necessary bindings for search functionality.

        '''
        self.searchFrame = tk.Frame(self.root, bd=2, relief="groove")       
        self.searchButton = tk.Button(self.searchFrame, bd=0, image=self.searchImg, command=lambda: self._toggleButtonCallback())
        self.searchButton.pack(side=tk.LEFT) 
        self.searchBox = tk.Entry(self.searchFrame, bg="lightgray", font=("Arial", 12))
        self.searchBox.pack(side=tk.LEFT, fill=tk.X, expand=True)
        self.searchBox.focus_set()       
        self.closeSearchBoxButton = tk.Button(self.searchFrame, bd=0, image=self.closeImg, command=lambda: self._showSearchCallback())
        self.closeSearchBoxButton.pack(side=tk.RIGHT) 
        self.searchBox.bind("<KeyRelease>", lambda event: self._searchTableCallback())
        self.searchBox.bind("<Escape>", lambda event: self._showSearchCallback())  
        self.root.bind("<Configure>", lambda event: self._resizeSearchBoxCallback())
        
    def buildTextEditBox(self, rowId, cellColumn, cellText):
        '''
        Builds the text input box for editing table cell values.

        Initializes the entry widget and sets up bindings for saving or canceling
        the edit action.

        :param rowId: The ID of the row being edited.
        :param cellColumn: The column of the cell being edited.
        :param cellText: The current text of the cell being edited.
        '''
        self.textInput = tk.Entry(self.table)
        self.textInput.insert(0, cellText) 
        self.textInput['exportselection'] = False                                  
        self.textInput.focus_force()    
        self.textInput.bind("<Return>", lambda event: self._editDataCallback(event, rowId, cellColumn)) 
        self.textInput.bind("<Escape>", lambda event: self.textInput.destroy())
        
    def buildInfoBox(self, title, text):
        '''
        Builds an information box to display messages.

        Initializes a new top-level window with the specified title and text.

        :param title: The title of the information box.
        :param text: The text to be displayed in the information box.
        '''
        self.infoBox = tk.Toplevel()
        self.infoBox.title(title)
        self.infoBox.minsize(width=400, height=200)
        self.infoBox.wm_resizable(False, False)
        self.infoLabel = tk.Label(self.infoBox, anchor="w", justify=tk.LEFT, text=text, wraplength=700)
        self.infoLabel.pack(fill="x" , padx=10, pady=10)
        self.infoButton = tk.Button(self.infoBox, text="OK", command=lambda: self.infoBox.destroy())
        self.infoButton.pack(pady=(0, 10))

        
  
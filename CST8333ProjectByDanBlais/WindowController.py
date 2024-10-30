#This module defines the Controller for the application. This module is composed of a class which contains methods for
#processing events from the View and manipulating the Model as needed. This is achieved by maintaining references to both
#the Model and the View and manipulating both as required. The View instance is instantiated from within this class and is
#passed the view processing methods of this class to be used as callbacks. 

#Author: Dan Blais - 040826486
#Subject: CST8333
#Due Date: October 13, 2024

#Note on code reference: The CodersLegacy reference was loosely followed to learn how to make treeview cells editable.
#All code in the tutorial was rewritten and modified for this program to fit in an MVC architecture.

#References
#[1] Siddiqi, "How to Make Ttk Treeview Editable in Python," CodersLegacy, 2023. [Online]. 
#            Available: https://coderslegacy.com/how-to-make-ttk-treeview-editable-python/. [Accessed: 24-Sep-2024].
#[2] "Tkinter Documentation," TkDocs, [Online]. Available: https://tkdocs.com/index.html. [Accessed: 25-Sep-2024].

import KeystonePipelineData as model
import AppWindow as view
import tkinter as tk
import itertools as it
import csv
import threading
from datetime import datetime

class WindowController:
    '''
    The WindowController class manages the interaction between the view and model
    for the pipeline data application. It handles file operations, data parsing,
    and user interactions with the graphical user interface.

    :attribute _view: An instance of the ProgramWindow class that represents the GUI.
    :attribute _highestId: An integer tracking the highest ID used for new rows.
    :attribute _searchOpen: A boolean indicating if the search box is open.
    :attribute _searchButtonToggle: A boolean indicating the state of the search button.
    :attribute _model: A list of PipelineData objects representing the parsed data.
    :attribute _file: A string representing the path of the currently opened file.
    '''
    
    def __init__(self):
        '''
        Initializes the WindowController, setting up the view and initializing attributes.
        '''
        self._view = view.ProgramWindow(self.openFile, self.addData, self.editData, self.deleteData, 
                                          self.searchTable, self.showHideSearchBox, self.toggleButton, 
                                          self.openContextMenu, self.openTextInput, self.reloadDataFromFile,
                                          self.saveFile, self.saveFileAs, self.resizeSearchBox, self.openRowDetails)
        self._highestId = 0
        self._searchOpen = False
        self._searchButtonToggle = False
        
    @property
    def model(self):
        '''
        Gets the current model.

        :returns: The current model.
        '''
        return self._model
    
    @model.setter
    def model(self, newModel):
        '''
        Sets the model to a new value.

        :param newModel: The new model to set.
        '''
        self._model = newModel
        
    @model.deleter
    def model(self):
        '''
        Deletes the current model.
        '''
        del self._model
        
    @property
    def view(self):
        '''
        Gets the current view.

        :returns: The current view.
        '''
        return self._view
    
    @view.setter
    def view(self, newView):
        '''
        Sets the view to a new value.

        :param newView: The new view to set.
        '''
        self._view = newView
        
    @view.deleter
    def view(self):
        '''
        Deletes the current view.
        '''
        del self._view    
    
    def parseCSV(self, file):
        '''
        Parses a csv file row by row into a list by creating objects that represent each row, and then appending
        them to the list. Also validates date and numeric row attributes prior to creating objects.
   
        :param file: A string representing the path of the file.
        :returns: A list of parsed rows, stored as objects.  
        '''
        pipelineDataList = []
   
        try: 
            with open(file, newline='') as dataset:
                dataReader = csv.reader(dataset, delimiter=",", quotechar='"')
                next(dataReader)
            
                for row in dataReader: 
                    
                    try:
                        date = datetime.strptime(row[0], "%Y-%m-%d").date() if row[0] else ""
                        month = int(row[1]) if row[1] else ""
                        year = int(row[2]) if row[2] else ""
                        latitude = float(row[6]) if row[6] else ""
                        longitude = float(row[7]) if row[7] else ""
                        throughput = float(row[11]) if row[11] else ""
                        committedVolumes = float(row[12]) if row[12] else ""
                        uncommittedVolumes = float(row[13]) if row[13] else ""
                        nameplateCapacity = float(row[14]) if row[14] else ""
                        availableCapacity = float(row[15]) if row[15] else ""
                    
                        pipeData = model.PipelineData(date=date, month=month, 
                                        year=year, company=row[3], pipeline=row[4], 
                                        keyPoint=row[5], latitude=latitude, longitude=longitude, 
                                        directionOfFlow=row[8], tradeType=row[9], product=row[10],
                                        throughput=throughput, committedVolumes=committedVolumes,
                                        uncommittedVolumes=uncommittedVolumes, nameplateCapacity=nameplateCapacity,
                                        availableCapacity=availableCapacity, reasonForVariance=row[16])
                        
                        pipelineDataList.append(pipeData)  
                        
                    except Exception as e: 
                        print(f"Error: {e}") 
                        
        except Exception as e: 
           print(f"Error: {e}") 
       
        self._model = pipelineDataList
        
    def loadData(self, rowStart, rowEnd):
        '''
        Loads a range of data into the view table from the model.

        :param rowStart: The starting index of the rows to load.
        :param rowEnd: The ending index of the rows to load.
        '''
        for index, pipelineDataRow in enumerate(it.islice(self._model, rowStart, rowEnd, 1)):
            self._view.table.insert("", "end", str(index), text=str(index), 
                                    values=(pipelineDataRow.date, pipelineDataRow.month, pipelineDataRow.year,
                                            pipelineDataRow.company, pipelineDataRow.pipeline, pipelineDataRow.keyPoint,
                                            pipelineDataRow.latitude, pipelineDataRow.longitude, pipelineDataRow.directionOfFlow,
                                            pipelineDataRow.tradeType, pipelineDataRow.product, pipelineDataRow.throughput,
                                            pipelineDataRow.committedVolumes, pipelineDataRow.uncommittedVolumes, pipelineDataRow.nameplateCapacity,
                                            pipelineDataRow.availableCapacity, pipelineDataRow.reasonForVariance))
            self._highestId += 1
    
    def searchTable(self):
        '''
        Searches the table based on the input in the search box and the toggled search mode.
        '''
        searchQuery = self._view.searchBox.get().lower()

        if self._searchButtonToggle == False:
            for value in self._view.table.get_children():
                values = self._view.table.item(value, "values")

                for searchValue in values:
                    if searchQuery in str(searchValue).lower():
                        self._view.table.item(value, tags=())
                        break 
                else:
                    self._view.table.item(value, tags=("hidden"))
        else:
            for value in self._view.table.get_children():
                if searchQuery == str(value):
                    self._view.table.item(value, tags=())
                    self._view.table.see(value)
                else:
                    self._view.table.item(value, tags=("hidden"))
                    
            if not searchQuery:
                for value in self._view.table.get_children():
                    self._view.table.item(value, tags=())
        
    def editData(self, event, rowId, columnIndex):
        '''
        Edits a cell value in the table and updates the model accordingly.

        :param event: The event triggering the edit.
        :param rowId: The ID of the row being edited.
        :param columnIndex: The index of the column being edited.
        '''
        index = self._view.table.index(self._view.table.selection()[0])  
        vals = self._view.table.item(rowId, 'values') 
        vals = list(vals) 
        vals[columnIndex] = self._view.textInput.get() 
        self._view.table.item(rowId, values=vals)  
        self._view.textInput.destroy() 
        value = vals[columnIndex]
        
        row = int(index)
        if columnIndex == 0:
            self._model[row].date = value;
        elif columnIndex == 1:
            self._model[row].month = value;
        elif columnIndex == 2:
            self._model[row].year = value;
        elif columnIndex == 3:
            self._model[row].company = value;
        elif columnIndex == 4:
            self._model[row].pipeline = value;
        elif columnIndex == 5:
            self._model[row].keyPoint = value;
        elif columnIndex == 6:
            self._model[row].latitude = value;
        elif columnIndex == 7:
            self._model[row].longitude = value;
        elif columnIndex == 8:
            self._model[row].directionOfFlow = value;
        elif columnIndex == 9:
            self._model[row].tradeType = value;
        elif columnIndex == 10:
            self._model[row].product = value;
        elif columnIndex == 11:
            self._model[row].throughput = value;
        elif columnIndex == 12:
            self._model[row].committedVolumes = value;
        elif columnIndex == 13:
            self._model[row].uncommittedVolumes = value;
        elif columnIndex == 14:
            self._model[row].nameplateCapacity = value;
        elif columnIndex == 15:
            self._model[row].availableCapacity = value;
        elif columnIndex == 16:
            self._model[row].reasonForVariance = value;

    def addData(self, position):
        '''
        Adds a new row of data to the table and model.

        :param position: A string indicating whether to add the row 'above' or 'below' the selected row.
        '''
        index = self._view.table.index(self._view.table.selection()[0])
        pipeData = model.PipelineData(date="", month="", year="", company="", pipeline="",  keyPoint="", latitude="", 
                                      longitude="", directionOfFlow="", tradeType="", product="", throughput="", 
                                      committedVolumes="",uncommittedVolumes="", nameplateCapacity="", availableCapacity="", 
                                      reasonForVariance="")
        
        if position == "above":
            self._view.table.insert("", index, str(self._highestId), text=str(self._highestId), values=("", "", "", "", "", "", "", "", 
                                                                                              "", "", "", "", "", "", "", "", ""))
            self._model.insert(index, pipeData) 
        elif position == "below":
            self._view.table.insert("", index + 1, str(self._highestId), text=str(self._highestId), values=("", "", "", "", "", "", "", "", 
                                                                                              "", "", "", "", "", "", "", "", ""))
            self._model.insert(index + 1, pipeData)
            
        self._highestId += 1

    def deleteData(self):
        '''
        Deletes the selected row from the table and model.
        '''
        rowId = int(self._view.table.selection()[0])
        index = self._view.table.index(self._view.table.selection()[0])
        self._model.pop(index)
        self._view.table.delete(rowId)
        
    def reloadDataFromFile(self):
        '''
        Reloads data from the currently selected CSV file, clearing the in memory data and replacing it with data from the file.
        '''
        if hasattr(self, "_file"):
            self._highestId = 0
            self._model.clear()
            
            for child in self._view.table.get_children():
                self._view.table.delete(child)
                
            self.startDaemonThread(self._file)
            self.loadData(0, 354)
        
    def openFile(self):
        '''
        Opens a CSV file and loads its data into the view.
        '''
        self._file = tk.filedialog.askopenfilename(title="Open Pipeline Data", filetypes=[('CSV Files', '*.csv')])
        
        if not self._file:
            return
        
        self._view.buildCSVTable()
        self._view.buildSearchBox()
        self.startDaemonThread(self._file)
        self.loadData(0, 354)
        self._view.startLabel.pack_forget()
        self._view.fileMenu.entryconfig(2, state=tk.NORMAL)
        self._view.fileMenu.entryconfig(3, state=tk.NORMAL)
        self._view.dataMenu.entryconfig(0, state=tk.NORMAL)
    
    def saveFile(self):
        '''
        Saves the current model data to the opened CSV file.
        '''
        if self._file:
            with open(self._file, 'w', newline='') as saveFile:
                dataWriter = csv.writer(saveFile, quoting=csv.QUOTE_MINIMAL)
                headers = ["Date", "Month", "Year", "Company", "Pipeline", "Key Point",
                           "Latitude", "Longitude", "Direction Of Flow", "Trade Type",
                           "Product", "Throughput (1000 m3/d)", "Committed Volumes (1000 m3/d)",
                           "Uncommitted Volumes (1000 m3/d)", "Nameplate Capacity (1000 m3/d)",
                           "Available Capacity (1000 m3/d)", "Reason For Variance"]
                dataWriter.writerow(headers)
           
                for row in range(len(self._model)):
                    dataWriter.writerow([self._model[row].date, self._model[row].month, self._model[row].year,
                                         self._model[row].company, self._model[row].pipeline, self._model[row].keyPoint,
                                         self._model[row].latitude, self._model[row].longitude, self._model[row].directionOfFlow,
                                         self._model[row].tradeType, self._model[row].product, self._model[row].throughput,
                                         self._model[row].committedVolumes, self._model[row].uncommittedVolumes,
                                         self._model[row].nameplateCapacity, self._model[row].availableCapacity,
                                         self._model[row].reasonForVariance])

    def saveFileAs(self):
        '''
        Opens a dialog to save the current model data to a new CSV file.
        '''
        self._saveFile = tk.filedialog.asksaveasfilename(title="Save File As...", defaultextension=".csv", filetypes=[('CSV Files', '*.csv')])
        
        if self._saveFile:
            with open(self._saveFile, 'w', newline='') as saveFile:
                dataWriter = csv.writer(saveFile, quoting=csv.QUOTE_MINIMAL)
                headers = ["Date", "Month", "Year", "Company", "Pipeline", "Key Point",
                           "Latitude", "Longitude", "Direction Of Flow", "Trade Type",
                           "Product", "Throughput (1000 m3/d)", "Committed Volumes (1000 m3/d)",
                           "Uncommitted Volumes (1000 m3/d)", "Nameplate Capacity (1000 m3/d)",
                           "Available Capacity (1000 m3/d)", "Reason For Variance"]
                dataWriter.writerow(headers)
           
                for row in range(len(self._model)):
                    dataWriter.writerow([self._model[row].date, self._model[row].month, self._model[row].year,
                                         self._model[row].company, self._model[row].pipeline, self._model[row].keyPoint,
                                         self._model[row].latitude, self._model[row].longitude, self._model[row].directionOfFlow,
                                         self._model[row].tradeType, self._model[row].product, self._model[row].throughput,
                                         self._model[row].committedVolumes, self._model[row].uncommittedVolumes,
                                         self._model[row].nameplateCapacity, self._model[row].availableCapacity,
                                         self._model[row].reasonForVariance])
        
    def showHideSearchBox(self):
        '''
        Toggles the visibility of the search box.
        '''
        if hasattr(self._view, "table"):
            if not self._searchOpen:
                self._searchOpen = True
                self.resizeSearchBox()
            else:
                self._searchOpen = False
                self._view.searchBox.delete(0, "end")
                self._view.searchFrame.place_forget()
                      
    def toggleButton(self):
        '''
        Toggles the search button state and resets the search box.
        '''
        if self._searchButtonToggle:
            self._view.searchButton.config(image=self._view.searchImg)
            self._searchButtonToggle = False
        else:
            self._view.searchButton.config(image=self._view.firstImg)
            self._searchButtonToggle = True
            
        self._view.searchBox.delete(0, "end")
        
        for value in self._view.table.get_children():
                    self._view.table.item(value, tags=())

    def openContextMenu(self, event):
        '''
        Opens a context menu on a selected row of the table.

        :param event: The event triggering the context menu popup.
        '''
        try: 
            if self._view.textInput:
                self._view.textInput.destroy()
        except AttributeError:
            pass
        
        try:
            rowId = self._view.table.identify_row(event.y)
            
            if not rowId:
                return
            
            self._view.table.selection_set(rowId)
            self._view.contextMenu.tk_popup(event.x_root, event.y_root)
            
        finally:
            self._view.contextMenu.grab_release()
            
    def openTextInput(self, event):
        '''
        Opens a text input field for editing the selected cell in the table.

        :param event: The event triggering the text input.
        '''    
        try: 
            if self._view.textInput:
                self._view.textInput.destroy()
        except AttributeError:
            pass

        rowId = self._view.table.identify_row(event.y)
        column = self._view.table.identify_column(event.x)

        if not rowId or column == "#0":
            return

        x, y, width, height = self._view.table.bbox(rowId, column)
        pady = height // 2
        text = self._view.table.item(rowId, 'values')[int(column[1:])-1]
        self._view.buildTextEditBox(rowId, int(column[1:])-1, text)
        self._view.textInput.place(x=x, y=y+pady, width=width, height=height - 2, anchor='w')
            
    def resizeSearchBox(self):
        '''
        Resizes the search box based on the current window width.
        '''
        if hasattr(self._view, "table"):
            if self._searchOpen:
                rootWidth = self._view.root.winfo_width()

                searchWidth = int(rootWidth * 0.30)
                self._view.searchFrame.place(x=rootWidth - searchWidth - 17, y=2, width=searchWidth)
                
    def openRowDetails(self):
        '''
        Opens a detail view for the currently selected row.
        '''
        rowId = int(self._view.table.selection()[0])
        index = self._view.table.index(self._view.table.selection()[0])
        self._view.buildInfoBox(f"Details For Row: {rowId}", self._model[index])
        
    def startDaemonThread(self, file):
        '''
        Starts a daemon thread which will open and parse a CSV file. 
        '''
        self._daemon = threading.Thread(target=self.parseCSV(file))
        self._daemon.daemon = True
        self._daemon.start()
        
if __name__ == "__main__":
    control = WindowController()
    control._view.root.mainloop()
             
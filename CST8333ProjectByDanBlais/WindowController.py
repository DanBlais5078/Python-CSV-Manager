from email.policy import default
import KeystonePipelineData as model
import AppWindow as window
import csv
import itertools as it
from datetime import datetime
import tkinter as tk

class WindowController:
    
    def __init__(self):
        self._view = window.ProgramWindow(self.openFile, self.addData, self.editData, self.deleteData, 
                                          self.searchTable, self.showHideSearchBox, self.toggleButton, 
                                          self.openContextMenu, self.openTextInput, self.reloadDataFromFile,
                                          self.saveFile, self.saveFileAs)
        self._highestId = 0
        self._searchOpen = False
        self._searchButtonToggle = False
        
    @property
    def model(self):
        return self._model
    
    @model.setter
    def model(self, newModel):
        self._model = newModel
        
    @model.deleter
    def model(self):
        del self._model
        
    @property
    def view(self):
        return self._view
    
    @view.setter
    def view(self, newView):
        self._view = newView
        
    @view.deleter
    def view(self):
        del self._view    
    
    def parseCSV(self, file):
        '''
        This method will parse a csv file row by row into a list by creating objects that represent each row, and then appending
        them to the list. Also validates date and numeric row attributes prior to creating objects.
   
        :param file: A string representing the path of the file.
        :returns: A list of parsed rows, stored as objects.  
        '''
        pipelineDataList = []
   
        try: 
       
            #Open csv file and create a reader object to parse it. Skip first line.
            with open(file, newline='') as dataset:
                dataReader = csv.reader(dataset, delimiter=",", quotechar='"')
                next(dataReader)
            
                #Iterate through csv rows stored in dataReader.
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
                    
                        #Create PipelineData object based on current row of csv.
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
                        
        #Catch program exceptions and print the exception to the console.
        except Exception as e: 
           print(f"Error: {e}") 
       
        self._model = pipelineDataList
        
    def loadData(self, rowStart, rowEnd):
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
    
        #Debugging, remove later
        print(f"\n{self._model[row]}\nRow ID: {rowId}\nArray Index: {row}")

    def addData(self, position):
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
        rowId = int(self._view.table.selection()[0])
        self._model.pop(rowId)
        self._view.table.delete(rowId)
        
    def reloadDataFromFile(self):
        if hasattr(self, "_file"):
            self._highestId = 0
            self._model.clear()
            
            for child in self._view.table.get_children():
                self._view.table.delete(child)
                
            self.parseCSV(self._file)
            self.loadData(0, 100)
        
    def openFile(self):
        self._file = tk.filedialog.askopenfilename(title="Open Pipeline Data", filetypes=[('CSV Files', '*.csv')])
        
        if not self._file:
            return
        
        self._view.buildCSVTable()
        self._view.buildSearchBox()
        self.parseCSV(self._file)
        self.loadData(0, 100)
        self._view.startLabel.pack_forget()
        self._view.fileMenu.entryconfig(2, state=tk.NORMAL)
        self._view.fileMenu.entryconfig(3, state=tk.NORMAL)
        self._view.dataMenu.entryconfig(0, state=tk.NORMAL)
    
    #test this
    def saveFile(self):
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
        if hasattr(self._view, "table"):
            if not self._searchOpen:
                self._view.searchFrame.place(relx=0.979, y=2, anchor='ne', width=self._view.root.winfo_width() * 0.3)
                self._searchOpen = True
            else:
                self._searchOpen = False
                self._view.searchBox.delete(0, "end")
                self._view.searchFrame.place_forget()
                
    def toggleButton(self):
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

    def mainloop(self):
        self._view.root.mainloop()
        
if __name__ == "__main__":
    control = WindowController()
    control.mainloop()
             
#This module defines a PipelineData object, which represents a row of data in the Pipeline Throughput
#and Capacity Data datset, provided by the Government of Canada. This project makes use of the CSV library 
#and the DateTime library. Docstring comments in reST style. 

#Author: Dan Blais - 040826486
#Subject: CST8333
#Due Date: September 22, 2024

#References:
# [1] Government of Canada, “Pipeline Throughput and Capacity Data” open.canada.ca, 2023. [Online]. 
# Available: https://open.canada.ca/data/en/dataset/dc343c43-a592-4a27-8ee7-c77df56afb34. [Accessed: 18 Sep. 2024].

from datetime import datetime

class PipelineData:
    '''
    Defines a class that represents a row of pipeline data as obtained from the Government of
    Canada - Pipeline Throughput and Capacity Data dataset.
    
    :attribute self: A reference to a PipelineData object.
    :attribute date: The date of a PipelineData object.
    :attribute month: The month portion of the date attribute.
    :attribute year: The year portion of the date attribute.
    :attribute company: The company that owns the segment of pipeline.
    :attribute pipeline: The pipeline.
    :attribute keyPoint: The identifying location of the pipeline.
    :attribute latitude: The latitude of the pipeline.
    :attribute longitude: The longitude of the pipeline.
    :attribute directionOfFlow: The direction in which the pipeline transports oil.
    :attribute tradeType: The type of trade that the pipeline is designated for, ie. local or international.
    :attribute product: The type of product that the pipeline is transporting.
    :attribute throughput: The capacity of the volume of flow within the pipeline.
    :attribute committedVolumes: Volume measure for the pipeline.
    :attribute uncommittedVolumes: Volume measure for the pipeline.
    :attribute nameplateCapacity: Total capacity for the pipeline.
    :attribute availableCapacity: Remaining capacity for the pipeline. 
    :attribute reasonForVariance: Reasons for variance in capacity or flow. 
    '''
       
    def __init__(self, date : datetime, month : int, year : int, company, pipeline, keyPoint, latitude : float, longitude : float,
                 directionOfFlow, tradeType, product, throughput : float, committedVolumes : float, uncommittedVolumes : float,
                 nameplateCapacity : float, availableCapacity : float, reasonForVariance):
        '''
        The initialization function for a PipelineData object.
        
        :param self: A reference to a PipelineData object.
        :param date: The date of a PipelineData object.
        :param month: The month portion of the date attribute.
        :param year: The year portion of the date attribute.
        :param company: The company that owns the segment of pipeline.
        :param pipeline: The pipeline.
        :param keyPoint: The identifying location of the pipeline.
        :param latitude: The latitude of the pipeline.
        :param longitude: The longitude of the pipeline.
        :param directionOfFlow: The direction in which the pipeline transports oil.
        :param tradeType: The type of trade that the pipeline is designated for, ie. local or international.
        :param product: The type of product that the pipeline is transporting.
        :param throughput: The capacity of the volume of flow within the pipeline.
        :param committedVolumes: Volume measure for the pipeline.
        :param uncommittedVolumes: Volume measure for the pipeline.
        :param nameplateCapacity: Total capacity for the pipeline.
        :param availableCapacity: Remaining capacity for the pipeline. 
        :param reasonForVariance: Reasons for variance in capacity or flow. 
        '''
        self._date = date
        self._month = month
        self._year = year
        self._company = company
        self._pipeline = pipeline
        self._keyPoint = keyPoint
        self._latitude = latitude
        self._longitude = longitude
        self._directionOfFlow = directionOfFlow
        self._tradeType = tradeType
        self._product = product
        self._throughput = throughput
        self._committedVolumes = committedVolumes
        self._uncommittedVolumes = uncommittedVolumes
        self._nameplateCapacity = nameplateCapacity
        self._availableCapacity = availableCapacity
        self._reasonForVariance = reasonForVariance
        
    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, newDate):
        try:
            datetime.strptime(newDate, '%Y-%m-%d').date()
            self._date = newDate.date()
        except Exception as e:
            print(f"Error: {e}") 

    @date.deleter
    def date(self):
        del self._date

    @property
    def month(self):
        return self._month

    @month.setter
    def month(self, newMonth):
        try:
            int(newMonth)
            self._month = newMonth
        except Exception as e:
            print(f"Error: {e}")   

    @month.deleter
    def month(self):
        del self._month

    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, newYear):
        try:
            int(newYear)
            self._year = newYear
        except Exception as e:
            print(f"Error: {e}") 
        

    @year.deleter
    def year(self):
        del self._year

    @property
    def company(self):
        return self._company

    @company.setter
    def company(self, newCompany):
        self._company = newCompany

    @company.deleter
    def company(self):
        del self._company

    @property
    def pipeline(self):
        return self._pipeline

    @pipeline.setter
    def pipeline(self, newPipeline):
        self._pipeline = newPipeline

    @pipeline.deleter
    def pipeline(self):
        del self._pipeline

    @property
    def keyPoint(self):
        return self._keyPoint

    @keyPoint.setter
    def keyPoint(self, newKeyPoint):
        self._keyPoint = newKeyPoint

    @keyPoint.deleter
    def keyPoint(self):
        del self._keyPoint

    @property
    def latitude(self):
        return self._latitude

    @latitude.setter
    def latitude(self, newLatitude):
        try:
            float(newLatitude)
            self._latitude = newLatitude
        except Exception as e:
            print(f"Error: {e}") 

    @latitude.deleter
    def latitude(self):
        del self._latitude

    @property
    def longitude(self):
        return self._longitude

    @longitude.setter
    def longitude(self, newLongitude):
        try:
            float(newLongitude)
            self._longitude = newLongitude
        except Exception as e:
            print(f"Error: {e}") 

    @longitude.deleter
    def longitude(self):
        del self._longitude

    @property
    def directionOfFlow(self):
        return self._directionOfFlow

    @directionOfFlow.setter
    def directionOfFlow(self, newDirectionOfFlow):
        self._directionOfFlow = newDirectionOfFlow

    @directionOfFlow.deleter
    def directionOfFlow(self):
        del self._directionOfFlow

    @property
    def tradeType(self):
        return self._tradeType

    @tradeType.setter
    def tradeType(self, newTradeType):
        self._tradeType = newTradeType

    @tradeType.deleter
    def tradeType(self):
        del self._tradeType

    @property
    def product(self):
        return self._product

    @product.setter
    def product(self, newProduct):
        self._product = newProduct

    @product.deleter
    def product(self):
        del self._product

    @property
    def throughput(self):
        return self._throughput

    @throughput.setter
    def throughput(self, newThroughput):
        try:
            float(newThroughput)
            self._throughput = newThroughput
        except Exception as e:
            print(f"Error: {e}") 

    @throughput.deleter
    def throughput(self):
        del self._throughput

    @property
    def committedVolumes(self):
        return self._committedVolumes

    @committedVolumes.setter
    def committedVolumes(self, newCommittedVolumes):
        try:
            float(newCommittedVolumes)
            self._committedVolumes = newCommittedVolumes
        except Exception as e:
            print(f"Error: {e}") 

    @committedVolumes.deleter
    def committedVolumes(self):
        del self._committedVolumes

    @property
    def uncommittedVolumes(self):
        return self._uncommittedVolumes

    @uncommittedVolumes.setter
    def uncommittedVolumes(self, newUncommittedVolumes):
        try:
            float(newUncommittedVolumes)
            self._uncommittedVolumes = newUncommittedVolumes
        except Exception as e:
            print(f"Error: {e}") 

    @uncommittedVolumes.deleter
    def uncommittedVolumes(self):
        del self._uncommittedVolumes

    @property
    def nameplateCapacity(self):
        return self._nameplateCapacity

    @nameplateCapacity.setter
    def nameplateCapacity(self, newNameplateCapacity):
        try:
            float(newNameplateCapacity)
            self._nameplateCapacity = newNameplateCapacity
        except Exception as e:
            print(f"Error: {e}") 

    @nameplateCapacity.deleter
    def nameplateCapacity(self):
        del self._nameplateCapacity

    @property
    def availableCapacity(self):
        return self._availableCapacity

    @availableCapacity.setter
    def availableCapacity(self, newAvailableCapacity):
        try:
            float(newAvailableCapacity)
            self._availableCapacity = newAvailableCapacity
        except Exception as e:
            print(f"Error: {e}") 

    @availableCapacity.deleter
    def availableCapacity(self):
        del self._availableCapacity

    @property
    def reasonForVariance(self):
        return self._reasonForVariance

    @reasonForVariance.setter
    def reasonForVariance(self, newReasonForVariance):
        self._reasonForVariance = newReasonForVariance

    @reasonForVariance.deleter
    def reasonForVariance(self):
        del self._reasonForVariance  

    def __repr__(self):
        '''
        The representation function for defining how a PipelineData object is formatted as a text string.
        
        :param self: A reference to a PipelineData object.
        :returns: A string representation of a PipelineData object.
        '''
        return(f"Date: {self.date}\nMonth: {self.month}\nYear: {self.year}\nCompany: {self.company}\n"
                f"Pipeline: {self.pipeline}\nKey Point: {self.keyPoint}\nLatitude: {self.latitude}\n"
                f"Longitude: {self.longitude}\nDirection Of Flow: {self.directionOfFlow}\nTrade Type: {self.tradeType}\n"
                f"Product: {self.product}\nThroughput: {self.throughput}\nCommitted Volumes: {self.committedVolumes}\n"
                f"Uncommitted Volumes: {self.uncommittedVolumes}\nNameplate Capacity: {self.nameplateCapacity}\n"
                f"Available Capacity: {self.availableCapacity}\nReason For Variance: {self.reasonForVariance}")
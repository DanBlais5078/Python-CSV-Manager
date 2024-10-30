#This module defines a PipelineData object, which represents a row of data in the Pipeline Throughput
#and Capacity Data datset, provided by the Government of Canada. This project makes use of the CSV library 
#and the DateTime library. Docstring comments in reST style. 

#Author: Dan Blais - 040826486
#Subject: CST8333
#Due Date: October 13, 2024

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
        Initializes a PipelineData object.
        
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
        '''The date of the pipeline data.'''
        return self._date

    @date.setter
    def date(self, newDate):
        '''Sets the date of the pipeline data.
        
        :param newDate: New date in the format 'YYYY-MM-DD'.
        '''
        try:
            datetime.strptime(newDate, '%Y-%m-%d').date()
            self._date = newDate.date()
        except Exception as e:
            print(f"Error: {e}") 

    @date.deleter
    def date(self):
        '''Deletes the date of the pipeline data.'''
        del self._date

    @property
    def month(self):
        '''The month of the pipeline data.'''
        return self._month

    @month.setter
    def month(self, newMonth):
        '''Sets the month of the pipeline data.
        
        :param newMonth: New month as an integer.
        '''
        try:
            int(newMonth)
            self._month = newMonth
        except Exception as e:
            print(f"Error: {e}")   

    @month.deleter
    def month(self):
        '''Deletes the month of the pipeline data.'''
        del self._month

    @property
    def year(self):
        '''The year of the pipeline data.'''
        return self._year

    @year.setter
    def year(self, newYear):
        '''Sets the year of the pipeline data.
        
        :param newYear: New year as an integer.
        '''
        try:
            int(newYear)
            self._year = newYear
        except Exception as e:
            print(f"Error: {e}") 
        
    @year.deleter
    def year(self):
        '''Deletes the year of the pipeline data.'''
        del self._year

    @property
    def company(self):
        '''The company that owns the segment of the pipeline.'''
        return self._company

    @company.setter
    def company(self, newCompany):
        '''Sets the company of the pipeline data.
        
        :param newCompany: New company name.
        '''
        self._company = newCompany

    @company.deleter
    def company(self):
        '''Deletes the company of the pipeline data.'''
        del self._company

    @property
    def pipeline(self):
        '''The pipeline identifier.'''
        return self._pipeline

    @pipeline.setter
    def pipeline(self, newPipeline):
        '''Sets the pipeline identifier.
        
        :param newPipeline: New pipeline identifier.
        '''
        self._pipeline = newPipeline

    @pipeline.deleter
    def pipeline(self):
        '''Deletes the pipeline identifier.'''
        del self._pipeline

    @property
    def keyPoint(self):
        '''The identifying location of the pipeline.'''
        return self._keyPoint

    @keyPoint.setter
    def keyPoint(self, newKeyPoint):
        '''Sets the key point of the pipeline data.
        
        :param newKeyPoint: New key point location.
        '''
        self._keyPoint = newKeyPoint

    @keyPoint.deleter
    def keyPoint(self):
        '''Deletes the key point of the pipeline data.'''
        del self._keyPoint

    @property
    def latitude(self):
        '''The latitude of the pipeline.'''
        return self._latitude

    @latitude.setter
    def latitude(self, newLatitude):
        '''Sets the latitude of the pipeline.
        
        :param newLatitude: New latitude as a float.
        '''
        try:
            float(newLatitude)
            self._latitude = newLatitude
        except Exception as e:
            print(f"Error: {e}")

    @latitude.deleter
    def latitude(self):
        '''Deletes the latitude of the pipeline.'''
        del self._latitude

    @property
    def longitude(self):
        '''The longitude of the pipeline.'''
        return self._longitude

    @longitude.setter
    def longitude(self, newLongitude):
        '''Sets the longitude of the pipeline.
        
        :param newLongitude: New longitude as a float.
        '''
        try:
            float(newLongitude)
            self._longitude = newLongitude
        except Exception as e:
            print(f"Error: {e}")

    @longitude.deleter
    def longitude(self):
        '''Deletes the longitude of the pipeline.'''
        del self._longitude

    @property
    def directionOfFlow(self):
        '''The direction in which the pipeline transports oil.'''
        return self._directionOfFlow

    @directionOfFlow.setter
    def directionOfFlow(self, newDirectionOfFlow):
        '''Sets the direction of flow for the pipeline data.
        
        :param newDirectionOfFlow: New direction of flow.
        '''
        self._directionOfFlow = newDirectionOfFlow

    @directionOfFlow.deleter
    def directionOfFlow(self):
        '''Deletes the direction of flow of the pipeline.'''
        del self._directionOfFlow

    @property
    def tradeType(self):
        '''The type of trade for the pipeline.'''
        return self._tradeType

    @tradeType.setter
    def tradeType(self, newTradeType):
        '''Sets the trade type of the pipeline data.
        
        :param newTradeType: New trade type.
        '''
        self._tradeType = newTradeType

    @tradeType.deleter
    def tradeType(self):
        '''Deletes the trade type of the pipeline.'''
        del self._tradeType

    @property
    def product(self):
        '''The type of product being transported by the pipeline.'''
        return self._product

    @product.setter
    def product(self, newProduct):
        '''Sets the product type of the pipeline data.
        
        :param newProduct: New product type.
        '''
        self._product = newProduct

    @product.deleter
    def product(self):
        '''Deletes the product type of the pipeline.'''
        del self._product

    @property
    def throughput(self):
        '''The throughput capacity of the pipeline.'''
        return self._throughput

    @throughput.setter
    def throughput(self, newThroughput):
        '''Sets the throughput of the pipeline.
        
        :param newThroughput: New throughput as a float.
        '''
        try:
            float(newThroughput)
            self._throughput = newThroughput
        except Exception as e:
            print(f"Error: {e}")

    @throughput.deleter
    def throughput(self):
        '''Deletes the throughput of the pipeline.'''
        del self._throughput

    @property
    def committedVolumes(self):
        '''The committed volumes for the pipeline.'''
        return self._committedVolumes

    @committedVolumes.setter
    def committedVolumes(self, newCommittedVolumes):
        '''Sets the committed volumes of the pipeline.
        
        :param newCommittedVolumes: New committed volumes as a float.
        '''
        try:
            float(newCommittedVolumes)
            self._committedVolumes = newCommittedVolumes
        except Exception as e:
            print(f"Error: {e}")

    @committedVolumes.deleter
    def committedVolumes(self):
        '''Deletes the committed volumes of the pipeline.'''
        del self._committedVolumes

    @property
    def uncommittedVolumes(self):
        '''The uncommitted volumes for the pipeline.'''
        return self._uncommittedVolumes

    @uncommittedVolumes.setter
    def uncommittedVolumes(self, newUncommittedVolumes):
        '''Sets the uncommitted volumes of the pipeline.
        
        :param newUncommittedVolumes: New uncommitted volumes as a float.
        '''
        try:
            float(newUncommittedVolumes)
            self._uncommittedVolumes = newUncommittedVolumes
        except Exception as e:
            print(f"Error: {e}")

    @uncommittedVolumes.deleter
    def uncommittedVolumes(self):
        '''Deletes the uncommitted volumes of the pipeline.'''
        del self._uncommittedVolumes

    @property
    def nameplateCapacity(self):
        '''The nameplate capacity of the pipeline.'''
        return self._nameplateCapacity

    @nameplateCapacity.setter
    def nameplateCapacity(self, newNameplateCapacity):
        '''Sets the nameplate capacity of the pipeline.
        
        :param newNameplateCapacity: New nameplate capacity as a float.
        '''
        try:
            float(newNameplateCapacity)
            self._nameplateCapacity = newNameplateCapacity
        except Exception as e:
            print(f"Error: {e}")

    @nameplateCapacity.deleter
    def nameplateCapacity(self):
        '''Deletes the nameplate capacity of the pipeline.'''
        del self._nameplateCapacity

    @property
    def availableCapacity(self):
        '''The available capacity of the pipeline.'''
        return self._availableCapacity

    @availableCapacity.setter
    def availableCapacity(self, newAvailableCapacity):
        '''Sets the available capacity of the pipeline.
        
        :param newAvailableCapacity: New available capacity as a float.
        '''
        try:
            float(newAvailableCapacity)
            self._availableCapacity = newAvailableCapacity
        except Exception as e:
            print(f"Error: {e}")

    @availableCapacity.deleter
    def availableCapacity(self):
        '''Deletes the available capacity of the pipeline.'''
        del self._availableCapacity

    @property
    def reasonForVariance(self):
        '''The reasons for variance in capacity or flow.'''
        return self._reasonForVariance

    @reasonForVariance.setter
    def reasonForVariance(self, newReasonForVariance):
        '''Sets the reason for variance in the pipeline data.
        
        :param newReasonForVariance: New reason for variance.
        '''
        self._reasonForVariance = newReasonForVariance

    @reasonForVariance.deleter
    def reasonForVariance(self):
        '''Deletes the reason for variance of the pipeline.'''
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
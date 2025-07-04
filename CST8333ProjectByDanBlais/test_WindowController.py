#This is a pyTest test class.

#Author: Dan Blais - 040826486
#Subject: CST8333
#Due Date: September 22, 2024

#References
#[1] Python Software Foundation, "unittest.mock � mock object library," Python 3.10.0 Documentation, 2021. [Online]. 
#             Available: https://docs.python.org/3/library/unittest.mock.html. [Accessed: 27-Sep-2024].

import pytest
from unittest.mock import MagicMock
import WindowController as controller
import KeystonePipelineData as model

def testDeleteRow():
    '''
    Tests the deleteData() method of the WindowController class. Uses MagicMock from the unittest API to mock the view without
    needing to instantiate the view class to perform the test. Tests the method by forcing the view to return a selected row
    index with a value of 1. The function is then called which deletes the row with a value of 1. Finally an assert statement
    is used to assert that the length of the model list should now be 1, indicating a row was deleted.
    '''
    cont = controller.WindowController()
    cont._model = [model.PipelineData(date='2024-01-01', month=1, year=2023, company='Company A',
                                           pipeline='Pipeline 1', keyPoint='Key Point 1', latitude=0.0,
                                           longitude=0.0, directionOfFlow='North', tradeType='Type A',
                                           product='Product A', throughput=100, committedVolumes=80,
                                           uncommittedVolumes=20, nameplateCapacity=120, availableCapacity=40,
                                           reasonForVariance='None'),
                   model.PipelineData(date='2024-01-02', month=1, year=2023, company='Company B',
                                           pipeline='Pipeline 2', keyPoint='Key Point 2', latitude=1.0,
                                           longitude=1.0, directionOfFlow='South', tradeType='Type B',
                                           product='Product B', throughput=200, committedVolumes=150,
                                           uncommittedVolumes=50, nameplateCapacity=250, availableCapacity=100,
                                           reasonForVariance='None')]
    cont._view = MagicMock()
    cont._view.table.selection.return_value = ['1']
    cont.deleteData()
    assert len(cont._model) == 1
    
if __name__ == '__main__':
    pytest.main()
    print("Program By: Dan Blais")
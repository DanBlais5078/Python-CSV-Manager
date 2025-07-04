#This is a pyTest test class.

#Author: Dan Blais - 040826486
#Subject: CST8333
#Due Date: September 22, 2024

#References
#[1] Python Software Foundation, "unittest.mock � mock object library," Python 3.10.0 Documentation, 2021. [Online]. 
#             Available: https://docs.python.org/3/library/unittest.mock.html. [Accessed: 27-Sep-2024].



import threading
from unittest.mock import MagicMock, patch
import pytest
import WindowController

def testStartDaemonThread():
    '''
    Tests the startDaemonThread() method of the WindowController class.
    Uses MagicMock to mock the parseCSV method and checks if the daemon thread is started
    and that the parseCSV method is called by the daemon thread. If the test passes then
    then daemon is calling the method successfully.
    '''
    
    cont = WindowController.WindowController()
    
    cont.parseCSV = MagicMock()

    test_file = "test.csv"
    cont.startDaemonThread(test_file)

    cont.parseCSV.assert_called_once_with(test_file)

    assert cont._daemon.daemon is True

if __name__ == '__main__':
    pytest.main()
    print("Program By: Dan Blais")
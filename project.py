"""
Muhammet Furkan MUŞTU
160403041
"""

import sys
import time

import binarySearch
import Bubble
import Insertion
import Merge
import heapsort
import numpy
import pyqtgraph
import quicksort
import countingSort
import radixSort
import improvedKthSmallestNumber
import kthSmallestNumber
import fibonacci
from PyQt5.uic import loadUi
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import webbrowser
from PyQt5 import QtTest




# noinspection PyPep8Naming
def ikc():
    link = "https://ikcu.edu.tr/"
    webbrowser.open_new(link)


class Project(QMainWindow):
    # noinspection PyArgumentList
    def __init__(self):
        super(Project, self).__init__()
        loadUi('Project.ui', self)

        ### button connection links
        self.pushButtonCreateArray.clicked.connect(self.CreateRandomArrayFunction)
        self.pushButtonInsertion.clicked.connect(self.InsertionSortFunction)
        self.pushButtonMerge.clicked.connect(self.MergeSortFunction)
        self.pushButtonBubble.clicked.connect(self.BubbleSortFunction)
        self.pushButtonCounting.clicked.connect(self.CountingSortFunc)
        self.pushButtonRadix.clicked.connect(self.radixSortFunc)
        self.pushButtonQuick.clicked.connect(self.QuickSortFunction)
        self.pushButtonHeap.clicked.connect(self.HeapSortFunction)
        self.pushButtonRandQuick.clicked.connect(self.RandQuickSortFunction)
        self.pushButtonSetDefault.clicked.connect(self.SetDefaultFunction)
        self.pushButtonSelectAll.clicked.connect(self.SelectAllFunc)
        self.pushButtonDeselectAll.clicked.connect(self.DeselectAllFunc)
        self.pushButtonCompare.clicked.connect(self.CompareFunc)
        self.pushButtonGenerateArray.clicked.connect(self.visualizeGenerateArrayFunc)
        self.pushButtonInsertionVis.clicked.connect(self.insertionVis)
        self.pushButtonBubbleVis.clicked.connect(self.bubbleVis)
        self.pushButtonCountingVis.clicked.connect(self.countingVis)
        self.pushButtonHeapVis.clicked.connect(self.heapVis)
        self.pushButtonMergeVis.clicked.connect(self.mergeVis)
        self.pushButtonQuickVis.clicked.connect(self.quickVis)
        self.pushButtonRandQuickVis.clicked.connect(self.randQuickVis)
        self.pushButtonRadixVis.clicked.connect(self.radixVis)
        self.pushButtonResetVis.clicked.connect(self.resetVis)
        self.pushButtonSetDefault_2.clicked.connect(self.setDefFunc)
        self.pushButtonCreateArray_2.clicked.connect(self.createArrayFunc)
        self.pushButtonFind.clicked.connect(self.findFunc)
        self.pushButtonFindImproved.clicked.connect(self.finImprovedFunc)
        self.spinBoxLength_2.valueChanged.connect(self.spinBoxValueFunc)
        self.horizontalSliderArrayLength.valueChanged.connect(self.sliderValue)
        self.pushButtonBinary.clicked.connect(self.BinarySearch)
        self.pushButtonFib.clicked.connect(self.fibb)
        self.pushButtonLinkedin.clicked.connect(self.linkedin)
        self.pushButtonGithub.clicked.connect(self.github)
        self.pushButtonIkc.clicked.connect(ikc)
        self.pushButtonLecturer.clicked.connect(self.lecturer)

        ### Global Variables
        self.UnsortedArray = []
        self.UnsortedArray_2 = []
        self.SortedArray_2 = []
        self.StepsCounter = 0
        self.UnsortedArrayComparison = []

        self.graphicsView.addLegend()

    """*******************************************************************************"""
    """ About page button functions"""

    def lecturer(self):
        link = "https://eee.ikcu.edu.tr/Personel/1013724"
        webbrowser.open_new(link)

    def github(self):
        link = "https://github.com/cinereus?tab=repositories"
        webbrowser.open_new(link)

    def linkedin(self):
        link1 = "www.linkedin.com/in/muhammet-furkan-muştu"
        webbrowser.open_new(link1)

    """********************************************************************************"""
    """Fibonacci and K'th Smallest page functions"""

    def setDefFunc(self):
        self.spinBoxMin_2.setValue(0)
        self.spinBoxMax_2.setValue(100)
        self.spinBoxLength_2.setValue(10)
        self.labelNormalTime.setText("")
        self.labelImprovedTime.setText("")
        self.spinBoxIthSmallest.setValue(1)
        self.labelFoundNumber.setText("")
        self.checkBoxNoRepeate_2.setChecked(0)
        self.spinBoxBinary.setValue(1)

    def createArrayFunc(self):
        """self.UnsortedArray = numpy.random.randint(int(self.spinBoxMin_2.value()), int(self.spinBoxMax_2.value()), int(self.spinBoxLength_2.value()))
        self.labelUnsortedArray_2.setText(str(self.UnsortedArray_2))"""
        minVal = int(self.spinBoxMin_2.value())
        maxVal = int(self.spinBoxMax_2.value())
        arrayLength = int(self.spinBoxLength_2.value())
        different = maxVal - minVal
        if self.checkBoxNoRepeate_2.isChecked():
            if different > arrayLength:
                def unique_rand(initial, limit, total):
                    data = []
                    i = 0
                    while i < total:
                        number = numpy.random.randint(initial, limit)
                        if number not in data:
                            data.append(number)
                            i += 1
                    return data

                self.UnsortedArray_2 = unique_rand(minVal, maxVal, arrayLength)
            else:
                err = "Array length must be greater than difference between limits"
                self.labelUnsortedArray_2.setText(str(err))

        else:
            self.UnsortedArray_2 = numpy.random.randint(minVal, maxVal, arrayLength)
        self.labelUnsortedArray_2.setText(str(self.UnsortedArray_2))
        self.SortedArray_2 = Insertion.sorting(self.UnsortedArray_2)
        self.labelSortedArray_2.setText(str(self.SortedArray_2))
        binaryMax = int(self.spinBoxMax_2.value())
        binaryMin = int(self.spinBoxMin_2.value())
        self.spinBoxBinary.setMaximum(binaryMax)
        self.spinBoxBinary.setMinimum(binaryMin)
        self.spinBoxIthSmallest.setMaximum(arrayLength + 1)

    def spinBoxValueFunc(self):
        max = int(self.spinBoxLength_2.value())
        self.spinBoxIthSmallest.setMaximum(max)

    def findFunc(self):
        n = self.spinBoxLength_2.value()
        foundNumber = 0
        k = int(self.spinBoxIthSmallest.value())
        findInitialTime = time.time()
        for i in range(10):
            foundNumber = kthSmallestNumber.kthSmallest(self.SortedArray_2, 0, n - 1, k)
        self.labelFoundNumber.setText(str(foundNumber))
        findFinalTime = time.time()
        findTotalTime = (findFinalTime - findInitialTime) / 10
        self.labelNormalTime.setText(str(findTotalTime))

    def finImprovedFunc(self):
        n = int(self.spinBoxLength_2.value())
        foundNumberImproved = 0
        findImprovedInitialTime = time.time()
        for i in range(10):
            foundNumberImproved = improvedKthSmallestNumber.kthSmallest(self.SortedArray_2, 0, n - 1, int(self.spinBoxIthSmallest.value()))
        self.labelFoundNumber.setText(str(foundNumberImproved))
        findImprovedFinalTime = time.time()
        findImprovedTotalTime = (findImprovedFinalTime - findImprovedInitialTime) / 10
        self.labelImprovedTime.setText(str(findImprovedTotalTime))

    def fibb(self):
        fibIndex = self.spinBoxFib.value()
        fibSeries = []
        for i in range(1, fibIndex+1):
            fibSeries.append(fibonacci.Fibonacci(i))
            QApplication.processEvents()
            self.labelFibSeries.setText(str(fibSeries))
        foundNumber = fibonacci.Fibonacci(fibIndex)
        self.labelFibFound.setText(str(foundNumber))

    def BinarySearch(self):
        k = self.spinBoxBinary.value()
        array = self.SortedArray_2.copy()
        rightEnd = self.spinBoxLength_2.value() - 1
        foundNumber = binarySearch.binarySearch(array, 0, rightEnd, k)
        self.labelFoundNumberBinary.setText(foundNumber)

    """********************************************************************************"""
    """Sorting page functions"""

    def SetDefaultFunction(self):
        self.spinBoxMin.setValue(0)
        self.spinBoxMax.setValue(100)
        self.spinBoxLength.setValue(15)
        self.spinBoxMaxLength.setValue(150)
        self.spinBoxLengthSteps.setValue(10)
        self.checkBoxNoRepeate.setChecked(0)
        self.DeselectAllFunc()
        self.checkBoxNonRepeative.setChecked(0)
        self.labelinsertionTime.setText("")
        self.labelBubbleTime.setText("")
        self.labelCountingTime.setText("")
        self.labelHeapTime.setText("")
        self.labelQuickTime.setText("")
        self.labelRandQuickTime.setText("")
        self.labelMergeTime.setText("")
        self.labelRadixTime.setText("")
        self.labelSortedArray.setText("")
        self.labelUnsortedArray.setText("")

    def CreateRandomArrayFunction(self):
        minVal = int(self.spinBoxMin.value())
        maxVal = int(self.spinBoxMax.value())
        arrayLength = int(self.spinBoxLength.value())
        different = maxVal - minVal
        if self.checkBoxNoRepeate.isChecked():
            if different > arrayLength:
                def unique_rand(initial, limit, total):
                    data = []
                    i = 0
                    while i < total:
                        number = numpy.random.randint(initial, limit)
                        if number not in data:
                            data.append(number)
                            i += 1
                    return data

                self.UnsortedArray = unique_rand(minVal, maxVal, arrayLength)
            else:
                err = "Array length must be greater than difference between limits"
                self.labelUnsortedArray.setText(str(err))

        else:
            self.UnsortedArray = numpy.random.randint(minVal, maxVal, arrayLength)
        self.labelUnsortedArray.setText(str(self.UnsortedArray))

    def CountingSortFunc(self):
        countingInitialTime = time.time()
        for i in range(0, 20):
            unsortedArrayForCounting = self.UnsortedArray.copy()
            maxRange = self.spinBoxMax.value()
            sortedArrayForCounting = countingSort.countSort(unsortedArrayForCounting, maxRange)
            self.labelSortedArray.setText(str(sortedArrayForCounting))
        countingFinalTime = time.time()
        countingTotalTime = (countingFinalTime - countingInitialTime)/20
        self.labelCountingTime.setText(str(countingTotalTime))

    def InsertionSortFunction(self):
        InsertionInitialTime = time.time()
        for i in range(0, 20):
            UnsortedArrayForInsertion = self.UnsortedArray.copy()
            SortedArrayInsertion = Insertion.sorting(UnsortedArrayForInsertion)
            self.labelSortedArray.setText(str(SortedArrayInsertion))
        InsertionFinalTime = time.time()
        InsertionTotalTime = (InsertionFinalTime - InsertionInitialTime) / 20
        self.labelinsertionTime.setText(str(InsertionTotalTime))

    def BubbleSortFunction(self):
        BubbleInitialTime = time.time()
        for i in range(0, 20):
            UnsortedArrayForBubble = self.UnsortedArray.copy()
            SortedArrayBubble = Bubble.Sorting(UnsortedArrayForBubble)
            self.labelSortedArray.setText(str(SortedArrayBubble))
        BubbleFinalTime = time.time()
        BubbleTotalTime = (BubbleFinalTime - BubbleInitialTime) / 20
        self.labelBubbleTime.setText(str(BubbleTotalTime))

    def HeapSortFunction(self):
        HeapInitialTime = time.time()
        for i in range(0, 20):
            UnsortedArrayForHeap = self.UnsortedArray.copy()
            heapsort.heapSort(UnsortedArrayForHeap)
            self.labelSortedArray.setText(str(UnsortedArrayForHeap))
        HeapFinalTime = time.time()
        HeapTotalTime = (HeapFinalTime - HeapInitialTime) / 20
        self.labelHeapTime.setText(str(HeapTotalTime))

    def RandQuickSortFunction(self):
        RandQuickInitialTime = time.time()
        for i in range(0, 20):
            UnsortedArrayForRandQuick = self.UnsortedArray.copy()
            quicksort.RandQuickSort(UnsortedArrayForRandQuick, 0, int(len(UnsortedArrayForRandQuick)) - 1)
            self.labelSortedArray.setText(str(UnsortedArrayForRandQuick))
        RandQuickFinalTime = time.time()
        RandQuickTotalTime = (RandQuickFinalTime - RandQuickInitialTime) / 20
        self.labelRandQuickTime.setText(str(RandQuickTotalTime))

    def QuickSortFunction(self):
        QuickInitialTime = time.time()
        for i in range(0, 20):
            UnsortedArrayForQuick = self.UnsortedArray.copy()
            quicksort.QuickSort(UnsortedArrayForQuick, 0, len(UnsortedArrayForQuick) - 1)
            self.labelSortedArray.setText(str(UnsortedArrayForQuick))
        QuickFinalTime = time.time()
        QuickTotalTime = (QuickFinalTime - QuickInitialTime) / 20
        self.labelQuickTime.setText(str(QuickTotalTime))

    def MergeSortFunction(self):
        MergeInitialTime = time.time()
        for i in range(0, 20):
            UnsortedArrayForMerge = self.UnsortedArray.copy()
            QApplication.processEvents()
            SortedArrayMerge = Merge.merge(UnsortedArrayForMerge)
            self.labelSortedArray.setText(str(SortedArrayMerge))
        MergeFinalTime = time.time()
        MergeTotalTime = (MergeFinalTime - MergeInitialTime) / 20
        self.labelMergeTime.setText(str(MergeTotalTime))

    def radixSortFunc(self):
        radixInitialTime = time.time()
        for i in range(0, 20):
            unsortedArrayForRadix = self.UnsortedArray.copy()
            radixSort.radixSort(unsortedArrayForRadix)
            self.labelSortedArray.setText(str(unsortedArrayForRadix))
        radixFinalTime = time.time()
        radixTotalTime = (radixFinalTime - radixInitialTime)/20
        self.labelRadixTime.setText(str(radixTotalTime))

    def SelectAllFunc(self):
        self.checkBoxInsertion.setChecked(1)
        self.checkBoxBubble.setChecked(1)
        self.checkBoxCounting.setChecked(1)
        self.checkBoxHeap.setChecked(1)
        self.checkBoxQuick.setChecked(1)
        self.checkBoxRandQuick.setChecked(1)
        self.checkBoxMerge.setChecked(1)
        self.checkBoxRadix.setChecked(1)

    def DeselectAllFunc(self):
        self.checkBoxInsertion.setChecked(0)
        self.checkBoxBubble.setChecked(0)
        self.checkBoxCounting.setChecked(0)
        self.checkBoxHeap.setChecked(0)
        self.checkBoxQuick.setChecked(0)
        self.checkBoxRandQuick.setChecked(0)
        self.checkBoxMerge.setChecked(0)
        self.checkBoxRadix.setChecked(0)

    def CreateRandomArrayFunctionForComparison(self):
        # maxLength = (int(self.MaxValSpinBox.value()) - int(self.MinValSpinBox.value()))
        if self.checkBoxNonRepeative.isChecked():
            def unique_rand(initial, limit, total):
                data = []
                i = 0
                while i < total:
                    number = numpy.random.randint(initial, limit)
                    if number not in data:
                        data.append(number)
                        i += 1
                return data

            self.UnsortedArrayComparison = unique_rand(0, int(self.spinBoxMaxLength.value()), self.StepsCounter)
        else:
            self.UnsortedArrayComparison = numpy.random.randint(0, int(self.spinBoxMaxLength.value()),
                                                                self.StepsCounter)

    def CompareFunc(self):
        self.graphicsView.clear()
        self.StepsCounter = int(self.spinBoxLengthSteps.value())
        InsertionTimes = []
        MergeTimes = []
        QuickTimes = []
        RandQuickTimes = []
        BubbleTimes = []
        CountingTimes = []
        HeapTimes = []
        RadixTimes = []
        x = []
        x.append(self.StepsCounter)
        while self.StepsCounter < (int(self.spinBoxMaxLength.value()) + 1):
            QApplication.processEvents()
            self.CreateRandomArrayFunctionForComparison()
            if self.checkBoxInsertion.isChecked():
                InsertionInitial = time.time()
                for i in range(0, 10):
                    UnsortedArrayForInsertion = self.UnsortedArrayComparison.copy()
                    QApplication.processEvents()
                    Insertion.sorting(UnsortedArrayForInsertion)
                InsertionFinal = time.time()
                InsertionTotal = (InsertionFinal - InsertionInitial) / 10
                InsertionTimes.append(InsertionTotal)
            else:
                InsertionTimes = []

            if self.checkBoxBubble.isChecked():
                BubbleInitial = time.time()
                for i in range(0, 10):
                    UnsortedArrayBubble = self.UnsortedArrayComparison.copy()
                    QApplication.processEvents()
                    Bubble.Sorting(UnsortedArrayBubble)
                BubbleFinal = time.time()
                BubbleTotal = (BubbleFinal - BubbleInitial) / 10
                BubbleTimes.append(BubbleTotal)
            else:
                BubbleTimes = []

            if self.checkBoxCounting.isChecked():
                CountingInitial = time.time()
                for i in range(0, 10):
                    UnsortedArrayCounting = self.UnsortedArrayComparison.copy()
                    maxRange = int(self.spinBoxMaxLength.value())*2
                    QApplication.processEvents()
                    countingSort.countSort(UnsortedArrayCounting, maxRange)
                CountingFinal = time.time()
                CountingTotal = (CountingFinal - CountingInitial)/10
                CountingTimes.append(CountingTotal)
            else:
                CountingTimes = []

            if self.checkBoxHeap.isChecked():
                HeapInitial = time.time()
                for i in range(0, 10):
                    UnsortedArrayHeap = self.UnsortedArrayComparison.copy()
                    QApplication.processEvents()
                    heapsort.heapSort(UnsortedArrayHeap)
                HeapFinal = time.time()
                HeapTotal = (HeapFinal - HeapInitial) / 10
                HeapTimes.append(HeapTotal)
            else:
                HeapTimes = []

            if self.checkBoxMerge.isChecked():
                MergeInitial = time.time()
                for i in range(0, 10):
                    UnsortedArrayMerge = self.UnsortedArrayComparison.copy()
                    QApplication.processEvents()
                    Merge.merge(UnsortedArrayMerge)
                MergeFinal = time.time()
                MergeTotal = (MergeFinal - MergeInitial) / 10
                MergeTimes.append(MergeTotal)
            else:
                MergeTimes = []

            if self.checkBoxQuick.isChecked():
                QuickInitial = time.time()
                for i in range(0, 10):
                    UnsortedArrayQuick = self.UnsortedArrayComparison.copy()
                    QApplication.processEvents()
                    quicksort.QuickSort(UnsortedArrayQuick, 0, self.StepsCounter - 1)
                QuickFinal = time.time()
                QuickTotal = (QuickFinal - QuickInitial) / 10
                QuickTimes.append(QuickTotal)
            else:
                QuickTimes = []

            if self.checkBoxRandQuick.isChecked():
                RandQuickInitial = time.time()
                for i in range(0, 10):
                    UnsortedArrayQuick = self.UnsortedArrayComparison.copy()
                    QApplication.processEvents()
                    quicksort.QuickSort(UnsortedArrayQuick, 0, self.StepsCounter - 1)
                RandQuickFinal = time.time()
                RandQuickTotal = (RandQuickFinal - RandQuickInitial) / 10
                RandQuickTimes.append(RandQuickTotal)
            else:
                RandQuickTimes = []

            if self.checkBoxRadix.isChecked():
                radixInitial = time.time()
                for i in range(0, 10):
                    UnsortedArrayRadix = self.UnsortedArrayComparison.copy()
                    QApplication.processEvents()
                    radixSort.radixSort(UnsortedArrayRadix)
                radixFinal = time.time()
                radixTotal = (radixFinal - radixInitial) / 10
                RadixTimes.append(radixTotal)
            else:
                RadixTimes = []


            self.StepsCounter = self.StepsCounter + int(self.spinBoxLengthSteps.value())
            x.append(self.StepsCounter)

        self.graphicsView.setTitle("Time Comparison Graph")
        self.graphicsView.setLabel('left', 'Time', units='s')
        self.graphicsView.setLabel('bottom', 'Array Length')

        if self.checkBoxInsertion.isChecked():
            self.graphicsView.plot(InsertionTimes, name="Insertion", pen=pyqtgraph.mkPen('w', width=1.5))
        if self.checkBoxMerge.isChecked():
            self.graphicsView.plot(MergeTimes, name="Merge", pen=pyqtgraph.mkPen('r', width=1.5))
        if self.checkBoxQuick.isChecked():
            self.graphicsView.plot(QuickTimes, name="Quick", pen=pyqtgraph.mkPen('g', width=1.5))
        if self.checkBoxRandQuick.isChecked():
            self.graphicsView.plot(RandQuickTimes, name="RandQuick", pen=pyqtgraph.mkPen('m', width=1.5))
        if self.checkBoxHeap.isChecked():
            self.graphicsView.plot(HeapTimes, name="Heap", pen=pyqtgraph.mkPen('y', width=1.5))
        if self.checkBoxBubble.isChecked():
            self.graphicsView.plot(BubbleTimes, name="Bubble", pen=pyqtgraph.mkPen('k', width=1.5))
        if self.checkBoxCounting.isChecked():
            self.graphicsView.plot(CountingTimes, name='Counting', pen=pyqtgraph.mkPen('g', width=1.5), style=Qt.DashLine)
        if self.checkBoxRadix.isChecked():
            self.graphicsView.plot(RadixTimes, name='Radix', pen=pyqtgraph.mkPen('r', width=1.5, style=Qt.DotLine))

    """********************************************************************************"""
    """Visualization page functions"""

    def visualizeGenerateArrayFunc(self):
        arrayLength = int(self.horizontalSliderArrayLength.value())
        x = []
        for i in range(1, arrayLength + 1):
            x.append(i)
        self.visualizeArrayUnsorted = numpy.random.randint(0, arrayLength * 2, arrayLength)
        visualizeArrayUnsorted = self.visualizeArrayUnsorted.copy()
        # self.graphicsViewVisualize.setTitle(title='')
        bg1 = pyqtgraph.BarGraphItem(x=x, height=visualizeArrayUnsorted, width=0.3, brush='r')
        self.graphicsViewVisualize.clear()
        self.graphicsViewVisualize.addItem(bg1)

    def resetVis(self):
        self.horizontalSliderArrayLength.setValue(15)
        self.horizontalSliderSpeed.setValue(2)
        arrayLength = int(self.horizontalSliderArrayLength.value())
        x = []
        for i in range(1, arrayLength + 1):
            x.append(i)
        visualizeArrayUnsorted = self.visualizeArrayUnsorted.copy()
        bg1 = pyqtgraph.BarGraphItem(x=x, height=visualizeArrayUnsorted, width=0.3, brush='r')
        self.graphicsViewVisualize.clear()
        self.graphicsViewVisualize.addItem(bg1)
        self.progressBar.setValue(0)
        self.checkBoxStop.setChecked(0)

    def sliderValue(self):
        value = self.horizontalSliderArrayLength.value()
        self.lcdNumberArrayLength.display(value)

    def insertionVis(self):
        arrayInsertion = self.visualizeArrayUnsorted.copy()
        self.insertionSorting(arrayInsertion)

    def bubbleVis(self):
        arrayBubble = self.visualizeArrayUnsorted.copy()
        self.bubbleSorting(arrayBubble)

    def countingVis(self):
        arrayCounting = self.visualizeArrayUnsorted.copy()
        arrayLength = int(self.horizontalSliderArrayLength.value())
        maxVal = arrayLength*2
        self.countingSort(arrayCounting, maxVal)

    def heapVis(self):
        arrayHeap = self.visualizeArrayUnsorted.copy()
        self.heapSort(arrayHeap)

    def mergeVis(self):
        arrayMerge = self.visualizeArrayUnsorted.copy()
        self.mergeSort(arrayMerge)

    def quickVis(self):
        arrayQuick = self.visualizeArrayUnsorted.copy()
        lengthArray = len(arrayQuick)
        self.QuickSort(arrayQuick, 0, lengthArray - 1)

    def randQuickVis(self):
        arrayRandQuick = self.visualizeArrayUnsorted.copy()
        lengthArray = len(arrayRandQuick)
        self.RandQuickSort(arrayRandQuick, 0, lengthArray - 1)

    def radixVis(self):
        arrayRadix = self.visualizeArrayUnsorted.copy()
        self.radixSort(arrayRadix)

    """********************************************************************************"""
    """Visualization Sorting Algorithm functions"""

    def insertionSorting(self, array):
        arrayLength = len(array)
        self.progressBar.setMaximum(arrayLength-1)
        x = []
        for lel in range(1, arrayLength + 1):
            x.append(lel)
        for j in range(1, len(array)):
            swap = int(array[j])
            i = j - 1
            while i >= 0 and int(array[i]) > swap:
                if self.checkBoxStop.isChecked():
                    while self.checkBoxStop.isChecked() == 1 :
                        QtTest.QTest.qWait(50)
                else:
                    speed = (4000 - (self.horizontalSliderSpeed.value()) * 1000) / 2
                QApplication.processEvents()
                QtTest.QTest.qWait(speed)
                self.graphicsViewVisualize.clear()
                bg1 = pyqtgraph.BarGraphItem(x=x, height=array, width=0.3, brush='r')
                self.graphicsViewVisualize.addItem(bg1)
                array[i + 1] = int(array[i])
                i = i - 1
                self.graphicsViewVisualize.clear()
                bg1 = pyqtgraph.BarGraphItem(x=x, height=array, width=0.3, brush='r')
                self.graphicsViewVisualize.addItem(bg1)
                QApplication.processEvents()
            array[i + 1] = swap
            self.progressBar.setValue(j)

        return array

    def bubbleSorting(self, array):  # Sorting Algorithm for Bubble Sort
        n = len(array)
        self.progressBar.setMaximum(n - 2)
        x = []
        for lel in range(1, n + 1):
            x.append(lel)
        for i in range(n):  # Traverse through all array elements
            # Last i elements are already in place
            for j in range(0, n - i - 1):  # Traverse the array from 0 to n-i-1
                if self.checkBoxStop.isChecked():
                    while self.checkBoxStop.isChecked() == 1:
                        QtTest.QTest.qWait(50)
                else:
                    speed = (4000 - (self.horizontalSliderSpeed.value()) * 1000) / 2
                QApplication.processEvents()
                QtTest.QTest.qWait(speed)
                self.graphicsViewVisualize.clear()
                bg1 = pyqtgraph.BarGraphItem(x=x, height=array, width=0.3, brush='r')
                self.graphicsViewVisualize.addItem(bg1)
                if int(array[j]) > int(array[j + 1]):  # Swap if the element found is greater
                    array[j], array[j + 1] = int(array[j + 1]), int(array[j])  # than the next element
                self.graphicsViewVisualize.clear()
                bg1 = pyqtgraph.BarGraphItem(x=x, height=array, width=0.3, brush='r')
                self.graphicsViewVisualize.addItem(bg1)
                self.progressBar.setValue(i)
        return array

    def countingSort(self, arr, maxRange):
        x = []
        n = len(arr)
        self.progressBar.setMaximum(n - 1)
        for lel in range(1, n + 1):
            x.append(lel)
        # The output character array that will have sorted arr
        output = [0] * maxRange

        # Create a count array to store count of inidividul
        # characters and initialize count array as 0
        count = [0] * maxRange

        # For storing the resulting answer since the
        # string is immutable
        # ans = [0] * len(arr)
        ans = numpy.random.randint(0, 1, len(arr))

        # Store count of each character
        for i in arr:
            count[i] += 1

        # Change count[i] so that count[i] now contains actual
        # position of this character in output array
        for i in range(maxRange):
            count[i] += count[i - 1]

        # Build the output character array
        for i in range(len(arr)):
            output[count[arr[i]] - 1] = arr[i]
            count[arr[i]] -= 1

        # Copy the output array to arr, so that arr now
        # contains sorted characters
        for i in range(len(arr)):
            if self.checkBoxStop.isChecked():
                while self.checkBoxStop.isChecked() == 1:
                    QtTest.QTest.qWait(50)
            else:
                speed = (4000 - (self.horizontalSliderSpeed.value()) * 1000) / 2
            QApplication.processEvents()
            QtTest.QTest.qWait(speed)
            self.graphicsViewVisualize.clear()
            bg1 = pyqtgraph.BarGraphItem(x=x, height=ans, width=0.3, brush='r')
            self.graphicsViewVisualize.addItem(bg1)
            ans[i] = output[i]
            self.graphicsViewVisualize.clear()
            bg1 = pyqtgraph.BarGraphItem(x=x, height=ans, width=0.3, brush='r')
            self.graphicsViewVisualize.addItem(bg1)
            self.progressBar.setValue(i)
        return ans
    # To heapify subtree rooted at index i.
    # n is size of heap

    def heapify(self, arr, sizeOfHeap, i):
        """"
        :param arr: Unsorted Array
        :param sizeOfHeap:
        :param i:
        :return: heapified arr
        """
        largest = i  # Initialize largest as root
        left = 2 * i + 1  # left = 2*i + 1
        rigth = 2 * i + 2  # right = 2*i + 2

        # See if left child of root exists and is greater than root
        if left < sizeOfHeap and arr[i] < arr[left]:
            largest = left

            # See if right child of root exists and is greater than root
        if rigth < sizeOfHeap and arr[largest] < arr[rigth]:
            largest = rigth

            # Change root, if needed
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]  # swap

            # Heapify the root.
            self.heapify(arr, sizeOfHeap, largest)

        # The main function to sort an array of given size

    def heapSort(self, arr):
        """

        :param arr: Array
        :return: Sorted Array
        """
        lengthArray = len(arr)
        x = []
        self.progressBar.setMaximum(lengthArray - 2)
        for lel in range(1, lengthArray + 1):
            x.append(lel)
        # Build a maxheap.
        for i in range(lengthArray, -1, -1):
            self.heapify(arr, lengthArray, i)

            # One by one extract elements
        for i in range(lengthArray - 1, 0, -1):
            if self.checkBoxStop.isChecked():
                while self.checkBoxStop.isChecked() == 1:
                    QtTest.QTest.qWait(50)
            else:
                speed = (4000 - (self.horizontalSliderSpeed.value()) * 1000) / 2
            QApplication.processEvents()
            QtTest.QTest.qWait(speed)
            self.graphicsViewVisualize.clear()
            bg1 = pyqtgraph.BarGraphItem(x=x, height=arr, width=0.3, brush='r')
            self.graphicsViewVisualize.addItem(bg1)
            arr[i], arr[0] = arr[0], arr[i]  # swap
            self.graphicsViewVisualize.clear()
            bg1 = pyqtgraph.BarGraphItem(x=x, height=arr, width=0.3, brush='r')
            self.graphicsViewVisualize.addItem(bg1)
            self.progressBar.setValue(lengthArray - i)
            self.heapify(arr, i, 0)

    def mergeSort(self, UnsortedArray):
        ArrayLength = len(UnsortedArray)
        x = []
        self.progressBar.setMaximum(ArrayLength - 1)
        for lel in range(1, ArrayLength + 1):
            x.append(lel)
        if (ArrayLength % 2) == 0:
            m = int(ArrayLength / 2)
            n1 = int(m)
            n2 = int(ArrayLength - m)
        else:
            m = int((ArrayLength + 1) / 2)
            n1 = int(m)
            n2 = int(ArrayLength - m)

        # create temp arrays
        #    Left_array = [0] * (n1)
        #    Right_array = [0] * (n2)
        Left_array = [0] * (n1 + 1)
        Right_array = [0] * (n2 + 1)

        # Copy data to temp arrays Left_array[] and Right_array[]
        for i in range(0, n1):
            Left_array[i] = (int(UnsortedArray[i]))
        Left_array[n1] = 999999999999999999999999999999

        for j in range(0, n2):
            Right_array[j] = (int(UnsortedArray[m + j]))
        Right_array[n2] = 999999999999999999999999999999

        # Sort temp arrays with insertion sorting algorithm
        Left_arraySorted = self.insertionSorting(Left_array)
        Right_arraySorted = self.insertionSorting(Right_array)

        # Merge the temp arrays back into sequence[l..r]
        i = 0  # Initial index of first subarray
        j = 0  # Initial index of second subarray
        k = 0  # l	 # Initial index of merged subarray

        for k in range(0, ArrayLength):
            if self.checkBoxStop.isChecked():
                while self.checkBoxStop.isChecked() == 1:
                    QtTest.QTest.qWait(50)
            else:
                speed = (4000 - (self.horizontalSliderSpeed.value()) * 1000) / 2
            QApplication.processEvents()
            QtTest.QTest.qWait(speed)
            self.graphicsViewVisualize.clear()
            bg1 = pyqtgraph.BarGraphItem(x=x, height=UnsortedArray, width=0.3, brush='r')
            self.graphicsViewVisualize.addItem(bg1)
            if Left_arraySorted[i] <= Right_arraySorted[j]:
                UnsortedArray[k] = int(Left_arraySorted[i])
                if i == n1:
                    continue
                i += 1
            else:
                UnsortedArray[k] = int(Right_arraySorted[j])
                # if j<n2-1:
                if j == n2:
                    continue
                j += 1
            self.graphicsViewVisualize.clear()
            bg1 = pyqtgraph.BarGraphItem(x=x, height=UnsortedArray, width=0.3, brush='r')
            self.graphicsViewVisualize.addItem(bg1)
            QApplication.processEvents()
            self.progressBar.setValue(k)

    def Partition(self, Array, InitialIndex, LastIndex):
        """
        :param Array: Input Array
        :param InitialIndex: First index of Array
        :param LastIndex: Last index of Array
        :return: i+1 // next pivot point
        """
        Pivot = Array[LastIndex]
        i = InitialIndex - 1
        ArrayLength = len(Array)
        x = []
        self.progressBar.setMaximum(ArrayLength - 3)
        for lel in range(1, ArrayLength + 1):
            x.append(lel)
        for j in range(InitialIndex, LastIndex):
            if self.checkBoxStop.isChecked():
                while self.checkBoxStop.isChecked() == 1:
                    QtTest.QTest.qWait(50)
            else:
                speed = (4000 - (self.horizontalSliderSpeed.value()) * 1000) / 2
            QApplication.processEvents()
            QtTest.QTest.qWait(speed)
            self.graphicsViewVisualize.clear()
            bg1 = pyqtgraph.BarGraphItem(x=x, height=Array, width=0.3, brush='r')
            self.graphicsViewVisualize.addItem(bg1)
            if Array[j] <= Pivot:  # if current element is less than or equal to pivot
                i = i + 1
                Array[i], Array[j] = Array[j], Array[i]  # exchange elements
            self.graphicsViewVisualize.clear()
            bg1 = pyqtgraph.BarGraphItem(x=x, height=Array, width=0.3, brush='r')
            self.graphicsViewVisualize.addItem(bg1)
            self.progressBar.setValue(i)
            QApplication.processEvents()
        Array[i + 1], Array[LastIndex] = Array[LastIndex], Array[i + 1]  # exchange elements
        return i + 1

    def RandPartition(self, Array, InitialIndex, LastIndex):
        """
        :param Array: Input Array
        :param InitialIndex: First index of Array
        :param LastIndex: Last index of Array
        :return: Partition function
        """
        i = InitialIndex - 1
        randomNumber = numpy.random.randint(InitialIndex, LastIndex, 1)
        Array[LastIndex], Array[randomNumber] = Array[randomNumber], Array[LastIndex]
        Pivot = Array[LastIndex]
        ArrayLength = len(Array)
        x = []
        self.progressBar.setMaximum(ArrayLength - 3)
        for lel in range(1, ArrayLength + 1):
            x.append(lel)
        for j in range(InitialIndex, LastIndex):
            if self.checkBoxStop.isChecked():
                while self.checkBoxStop.isChecked() == 1:
                    QtTest.QTest.qWait(50)
            else:
                speed = (4000 - (self.horizontalSliderSpeed.value()) * 1000) / 2
            QApplication.processEvents()
            QtTest.QTest.qWait(speed)
            self.graphicsViewVisualize.clear()
            bg1 = pyqtgraph.BarGraphItem(x=x, height=Array, width=0.3, brush='r')
            self.graphicsViewVisualize.addItem(bg1)
            if Array[j] <= Pivot:  # if current element is less than or equal to pivot
                i = i + 1
                Array[i], Array[j] = Array[j], Array[i]  # exchange elements
            self.graphicsViewVisualize.clear()
            bg1 = pyqtgraph.BarGraphItem(x=x, height=Array, width=0.3, brush='r')
            self.graphicsViewVisualize.addItem(bg1)
            self.progressBar.setValue(i)
            QApplication.processEvents()
        Array[i + 1], Array[LastIndex] = Array[LastIndex], Array[i + 1]  # exchange elements
        return i + 1

    def QuickSort(self, Array, InitialIndex, LastIndex):
        """
        Initial call : QuickSort(array,0,arraylength-1)
        :param Array: Input Array
        :param InitialIndex: First index of Array
        :param LastIndex: Last index of Array
        :return: ----
        """
        if InitialIndex < LastIndex:  # check base case
            QApplication.processEvents()
            PivotPoint = self.Partition(Array, InitialIndex, LastIndex)
            self.QuickSort(Array, InitialIndex, PivotPoint - 1)  # call function recursively for subarrays
            self.QuickSort(Array, PivotPoint + 1, LastIndex)

    def RandQuickSort(self, Array, InitialIndex, LastIndex):
        """
        Initial call : RandomizedQuickSort(array,0,arraylength-1)
        :param Array: Input Array
        :param InitialIndex: First index of Array
        :param LastIndex: Last index of Array
        :return: ----
        """
        if InitialIndex < LastIndex:  # check base case
            PivotPoint = self.RandPartition(Array, InitialIndex, LastIndex)
            self.RandQuickSort(Array, InitialIndex, PivotPoint - 1)  # call function recursively for subarrays
            self.RandQuickSort(Array, PivotPoint + 1, LastIndex)

    # A function to do counting sort of arr[] according to
    # the digit represented by exp.
    def countingSortRadix(self, arr, exp1):
        n = len(arr)

        # The output array elements that will have sorted arr
        output = [0] * (n)

        # initialize count array as 0
        count = [0] * (10)

        # Store count of occurrences in count[]
        for i in range(0, n):
            index = (arr[i] / exp1)
            count[int((index) % 10)] += 1

        # Change count[i] so that count[i] now contains actual
        #  position of this digit in output array
        for i in range(1, 10):
            count[i] += count[i - 1]

            # Build the output array
        i = n - 1
        while i >= 0:
            index = (arr[i] / exp1)
            output[count[int((index) % 10)] - 1] = arr[i]
            count[int((index) % 10)] -= 1
            i -= 1

        # Copying the output array to arr[],
        # so that arr now contains sorted numbers
        i = 0
        for i in range(0, len(arr)):
            arr[i] = output[i]

        # Method to do Radix Sort

    def radixSort(self, arr):
        # Find the maximum number to know number of digits
        max1 = max(arr)
        ArrayLength = len(arr)
        x = []
        self.progressBar.setMaximum(100)
        for lel in range(1, ArrayLength + 1):
            x.append(lel)
        # Do counting sort for every digit. Note that instead
        # of passing digit number, exp is passed. exp is 10^i
        # where i is current digit number
        exp = 1
        while max1 / exp > 1:
            if self.checkBoxStop.isChecked():
                while self.checkBoxStop.isChecked() == 1:
                    QtTest.QTest.qWait(50)
            else:
                speed = (4000 - (self.horizontalSliderSpeed.value()) * 1000) / 2
            QApplication.processEvents()
            QtTest.QTest.qWait(speed)
            self.graphicsViewVisualize.clear()
            bg1 = pyqtgraph.BarGraphItem(x=x, height=arr, width=0.3, brush='r')
            self.graphicsViewVisualize.addItem(bg1)
            self.countingSortRadix(arr, exp)
            exp *= 10
            self.graphicsViewVisualize.clear()
            QApplication.processEvents()
            bg1 = pyqtgraph.BarGraphItem(x=x, height=arr, width=0.3, brush='r')
            self.graphicsViewVisualize.addItem(bg1)
            self.progressBar.setValue(exp)

if __name__ == "__main__":
    numpy.random.seed(0)
    app = QApplication(sys.argv)
    ui = Project()
    ui.show()
    sys.exit(app.exec_())
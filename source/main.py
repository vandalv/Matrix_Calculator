import sys
from ui import *
from PyQt5 import QtCore, QtGui, QtWidgets
import numpy as np


class MyWin(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle('Valery Dauzhuk #19648')
        # Buttons
        self.ui.pushButtonPlus.clicked.connect(self.Add)
        self.ui.pushButtonMinus.clicked.connect(self.Subtract)
        self.ui.pushButtonMultiply.clicked.connect(self.Multiply)
        self.ui.pushButtonDetA.clicked.connect(self.DetA)
        self.ui.pushButtonDetB.clicked.connect(self.DetB)
        self.ui.pushButtonDetC.clicked.connect(self.DetC)
        self.ui.pushButtonTransposeA.clicked.connect(self.TransposeA)
        self.ui.pushButtonTransposeB.clicked.connect(self.TransposeB)
        self.ui.pushButtonTransposeC.clicked.connect(self.TransposeC)
        self.ui.pushButtonClearA.clicked.connect(self.ClearA)
        self.ui.pushButtonClearB.clicked.connect(self.ClearB)
        self.ui.pushButtonClearB_2.clicked.connect(self.ClearC)

    def Add(self):

        # MatrixA

        int00 = self.ui.matrixA_00.text()
        int01 = self.ui.matrixA_01.text()
        int02 = self.ui.matrixA_02.text()
        int03 = self.ui.matrixA_03.text()
        int04 = self.ui.matrixA_04.text()
        int05 = self.ui.matrixA_05.text()
        int06 = self.ui.matrixA_06.text()
        int07 = self.ui.matrixA_07.text()
        int08 = self.ui.matrixA_08.text()
        int09 = self.ui.matrixA_09.text()
        int10 = self.ui.matrixA_10.text()
        int11 = self.ui.matrixA_11.text()
        int12 = self.ui.matrixA_12.text()
        int13 = self.ui.matrixA_13.text()
        int14 = self.ui.matrixA_14.text()
        int15 = self.ui.matrixA_15.text()
        int16 = self.ui.matrixA_16.text()
        int17 = self.ui.matrixA_17.text()
        int18 = self.ui.matrixA_18.text()
        int19 = self.ui.matrixA_19.text()
        int20 = self.ui.matrixA_20.text()
        int21 = self.ui.matrixA_21.text()
        int22 = self.ui.matrixA_22.text()
        int23 = self.ui.matrixA_23.text()
        int24 = self.ui.matrixA_24.text()

        # MatrixB

        int25 = self.ui.matrixB_00.text()
        int26 = self.ui.matrixB_01.text()
        int27 = self.ui.matrixB_02.text()
        int28 = self.ui.matrixB_03.text()
        int29 = self.ui.matrixB_04.text()
        int30 = self.ui.matrixB_05.text()
        int31 = self.ui.matrixB_06.text()
        int32 = self.ui.matrixB_07.text()
        int33 = self.ui.matrixB_08.text()
        int34 = self.ui.matrixB_09.text()
        int35 = self.ui.matrixB_10.text()
        int36 = self.ui.matrixB_11.text()
        int37 = self.ui.matrixB_12.text()
        int38 = self.ui.matrixB_13.text()
        int39 = self.ui.matrixB_14.text()
        int40 = self.ui.matrixB_15.text()
        int41 = self.ui.matrixB_16.text()
        int42 = self.ui.matrixB_17.text()
        int43 = self.ui.matrixB_18.text()
        int44 = self.ui.matrixB_19.text()
        int45 = self.ui.matrixB_20.text()
        int46 = self.ui.matrixB_21.text()
        int47 = self.ui.matrixB_22.text()
        int48 = self.ui.matrixB_23.text()
        int49 = self.ui.matrixB_24.text()

        matrixA = [[int00, int01, int02, int03, int04],
                   [int05, int06, int07, int08, int09],
                   [int10, int11, int12, int13, int14],
                   [int15, int16, int17, int18, int19],
                   [int20, int21, int22, int23, int24]]
        matrixB = [[int25, int26, int27, int28, int29],
                   [int30, int31, int32, int33, int34],
                   [int35, int36, int37, int38, int39],
                   [int40, int41, int42, int43, int44],
                   [int45, int46, int47, int48, int49]]

        new_matrixA = [[instance for instance in sublist if len(
            instance) > 0] for sublist in matrixA]
        new_matrixA = list(filter(None, new_matrixA))
        matrixAdimensions = [len(new_matrixA), len(new_matrixA[0])]
        new_matrixA = np.array(new_matrixA)
        new_matrixA = new_matrixA.astype(np.int)
        new_matrixB = [[instance for instance in sublist if len(
            instance) > 0] for sublist in matrixB]
        new_matrixB = list(filter(None, new_matrixB))
        matrixBdimensions = [len(new_matrixB), len(new_matrixB[0])]
        new_matrixB = np.array(new_matrixB)
        new_matrixB = new_matrixB.astype(np.int)
        if (matrixAdimensions[0] == matrixBdimensions[0]) and (matrixAdimensions[1] == matrixBdimensions[1]):
            matrixC = new_matrixA + new_matrixB
            matrixC = np.array(matrixC)
            target = np.zeros((5, 5))
            target[:matrixC.shape[0], :matrixC.shape[1]] = matrixC
            target = target.astype(np.int)
            target = target.astype(np.str)
            target[target == '0'] = ''
            for i in range(len(matrixC)):
                for j in range(len(matrixC[0])):
                    if(target[i][j] == ''):
                        target[i][j] = '0'

            # MatrixC
            self.ui.matrixC_00.setText(target[0][0])
            self.ui.matrixC_01.setText(target[0][1])
            self.ui.matrixC_02.setText(target[0][2])
            self.ui.matrixC_03.setText(target[0][3])
            self.ui.matrixC_04.setText(target[0][4])
            self.ui.matrixC_05.setText(target[1][0])
            self.ui.matrixC_06.setText(target[1][1])
            self.ui.matrixC_07.setText(target[1][2])
            self.ui.matrixC_08.setText(target[1][3])
            self.ui.matrixC_09.setText(target[1][4])
            self.ui.matrixC_10.setText(target[2][0])
            self.ui.matrixC_11.setText(target[2][1])
            self.ui.matrixC_12.setText(target[2][2])
            self.ui.matrixC_13.setText(target[2][3])
            self.ui.matrixC_14.setText(target[2][4])
            self.ui.matrixC_15.setText(target[3][0])
            self.ui.matrixC_16.setText(target[3][1])
            self.ui.matrixC_17.setText(target[3][2])
            self.ui.matrixC_18.setText(target[3][3])
            self.ui.matrixC_19.setText(target[3][4])
            self.ui.matrixC_20.setText(target[4][0])
            self.ui.matrixC_21.setText(target[4][1])
            self.ui.matrixC_22.setText(target[4][2])
            self.ui.matrixC_23.setText(target[4][3])
            self.ui.matrixC_24.setText(target[4][4])
            self.ui.textLabel.setText('addition completed')
        elif (matrixAdimensions[0] != matrixBdimensions[0]) or (matrixAdimensions[1] != matrixBdimensions[1]):
            self.ui.textLabel.setText('wrong matrix dimensions')
            self.ui.matrixC_00.setText('')
            self.ui.matrixC_01.setText('')
            self.ui.matrixC_02.setText('')
            self.ui.matrixC_03.setText('')
            self.ui.matrixC_04.setText('')
            self.ui.matrixC_05.setText('')
            self.ui.matrixC_06.setText('')
            self.ui.matrixC_07.setText('')
            self.ui.matrixC_08.setText('')
            self.ui.matrixC_09.setText('')
            self.ui.matrixC_10.setText('')
            self.ui.matrixC_11.setText('')
            self.ui.matrixC_12.setText('')
            self.ui.matrixC_13.setText('')
            self.ui.matrixC_14.setText('')
            self.ui.matrixC_15.setText('')
            self.ui.matrixC_16.setText('')
            self.ui.matrixC_17.setText('')
            self.ui.matrixC_18.setText('')
            self.ui.matrixC_19.setText('')
            self.ui.matrixC_20.setText('')
            self.ui.matrixC_21.setText('')
            self.ui.matrixC_22.setText('')
            self.ui.matrixC_23.setText('')
            self.ui.matrixC_24.setText('')

    def Subtract(self):

        # MatrixA

        int00 = self.ui.matrixA_00.text()
        int01 = self.ui.matrixA_01.text()
        int02 = self.ui.matrixA_02.text()
        int03 = self.ui.matrixA_03.text()
        int04 = self.ui.matrixA_04.text()
        int05 = self.ui.matrixA_05.text()
        int06 = self.ui.matrixA_06.text()
        int07 = self.ui.matrixA_07.text()
        int08 = self.ui.matrixA_08.text()
        int09 = self.ui.matrixA_09.text()
        int10 = self.ui.matrixA_10.text()
        int11 = self.ui.matrixA_11.text()
        int12 = self.ui.matrixA_12.text()
        int13 = self.ui.matrixA_13.text()
        int14 = self.ui.matrixA_14.text()
        int15 = self.ui.matrixA_15.text()
        int16 = self.ui.matrixA_16.text()
        int17 = self.ui.matrixA_17.text()
        int18 = self.ui.matrixA_18.text()
        int19 = self.ui.matrixA_19.text()
        int20 = self.ui.matrixA_20.text()
        int21 = self.ui.matrixA_21.text()
        int22 = self.ui.matrixA_22.text()
        int23 = self.ui.matrixA_23.text()
        int24 = self.ui.matrixA_24.text()

        # MatrixB

        int25 = self.ui.matrixB_00.text()
        int26 = self.ui.matrixB_01.text()
        int27 = self.ui.matrixB_02.text()
        int28 = self.ui.matrixB_03.text()
        int29 = self.ui.matrixB_04.text()
        int30 = self.ui.matrixB_05.text()
        int31 = self.ui.matrixB_06.text()
        int32 = self.ui.matrixB_07.text()
        int33 = self.ui.matrixB_08.text()
        int34 = self.ui.matrixB_09.text()
        int35 = self.ui.matrixB_10.text()
        int36 = self.ui.matrixB_11.text()
        int37 = self.ui.matrixB_12.text()
        int38 = self.ui.matrixB_13.text()
        int39 = self.ui.matrixB_14.text()
        int40 = self.ui.matrixB_15.text()
        int41 = self.ui.matrixB_16.text()
        int42 = self.ui.matrixB_17.text()
        int43 = self.ui.matrixB_18.text()
        int44 = self.ui.matrixB_19.text()
        int45 = self.ui.matrixB_20.text()
        int46 = self.ui.matrixB_21.text()
        int47 = self.ui.matrixB_22.text()
        int48 = self.ui.matrixB_23.text()
        int49 = self.ui.matrixB_24.text()

        matrixA = [[int00, int01, int02, int03, int04],
                   [int05, int06, int07, int08, int09],
                   [int10, int11, int12, int13, int14],
                   [int15, int16, int17, int18, int19],
                   [int20, int21, int22, int23, int24]]
        matrixB = [[int25, int26, int27, int28, int29],
                   [int30, int31, int32, int33, int34],
                   [int35, int36, int37, int38, int39],
                   [int40, int41, int42, int43, int44],
                   [int45, int46, int47, int48, int49]]

        new_matrixA = [[instance for instance in sublist if len(
            instance) > 0] for sublist in matrixA]
        new_matrixA = list(filter(None, new_matrixA))
        matrixAdimensions = [len(new_matrixA), len(new_matrixA[0])]
        new_matrixA = np.array(new_matrixA)
        new_matrixA = new_matrixA.astype(np.int)
        new_matrixB = [[instance for instance in sublist if len(
            instance) > 0] for sublist in matrixB]
        new_matrixB = list(filter(None, new_matrixB))
        matrixBdimensions = [len(new_matrixB), len(new_matrixB[0])]
        new_matrixB = np.array(new_matrixB)
        new_matrixB = new_matrixB.astype(np.int)
        if (matrixAdimensions[0] == matrixBdimensions[0]) and (matrixAdimensions[1] == matrixBdimensions[1]):
            matrixC = new_matrixA - new_matrixB
            matrixC = np.array(matrixC)
            target = np.zeros((5, 5))
            target[:matrixC.shape[0], :matrixC.shape[1]] = matrixC
            target = target.astype(np.int)
            target = target.astype(np.str)
            target[target == '0'] = ''
            for i in range(len(new_matrixB)):
                for j in range(len(new_matrixB[0])):
                    if(target[i][j] == ''):
                        target[i][j] = '0'
            # MatrixC
            self.ui.matrixC_00.setText(target[0][0])
            self.ui.matrixC_01.setText(target[0][1])
            self.ui.matrixC_02.setText(target[0][2])
            self.ui.matrixC_03.setText(target[0][3])
            self.ui.matrixC_04.setText(target[0][4])
            self.ui.matrixC_05.setText(target[1][0])
            self.ui.matrixC_06.setText(target[1][1])
            self.ui.matrixC_07.setText(target[1][2])
            self.ui.matrixC_08.setText(target[1][3])
            self.ui.matrixC_09.setText(target[1][4])
            self.ui.matrixC_10.setText(target[2][0])
            self.ui.matrixC_11.setText(target[2][1])
            self.ui.matrixC_12.setText(target[2][2])
            self.ui.matrixC_13.setText(target[2][3])
            self.ui.matrixC_14.setText(target[2][4])
            self.ui.matrixC_15.setText(target[3][0])
            self.ui.matrixC_16.setText(target[3][1])
            self.ui.matrixC_17.setText(target[3][2])
            self.ui.matrixC_18.setText(target[3][3])
            self.ui.matrixC_19.setText(target[3][4])
            self.ui.matrixC_20.setText(target[4][0])
            self.ui.matrixC_21.setText(target[4][1])
            self.ui.matrixC_22.setText(target[4][2])
            self.ui.matrixC_23.setText(target[4][3])
            self.ui.matrixC_24.setText(target[4][4])
            self.ui.textLabel.setText('subtraction completed')
        elif (matrixAdimensions[0] != matrixBdimensions[0]) or (matrixAdimensions[1] != matrixBdimensions[1]):
            self.ui.textLabel.setText('wrong matrix dimensions')
            self.ui.matrixC_00.setText('')
            self.ui.matrixC_01.setText('')
            self.ui.matrixC_02.setText('')
            self.ui.matrixC_03.setText('')
            self.ui.matrixC_04.setText('')
            self.ui.matrixC_05.setText('')
            self.ui.matrixC_06.setText('')
            self.ui.matrixC_07.setText('')
            self.ui.matrixC_08.setText('')
            self.ui.matrixC_09.setText('')
            self.ui.matrixC_10.setText('')
            self.ui.matrixC_11.setText('')
            self.ui.matrixC_12.setText('')
            self.ui.matrixC_13.setText('')
            self.ui.matrixC_14.setText('')
            self.ui.matrixC_15.setText('')
            self.ui.matrixC_16.setText('')
            self.ui.matrixC_17.setText('')
            self.ui.matrixC_18.setText('')
            self.ui.matrixC_19.setText('')
            self.ui.matrixC_20.setText('')
            self.ui.matrixC_21.setText('')
            self.ui.matrixC_22.setText('')
            self.ui.matrixC_23.setText('')
            self.ui.matrixC_24.setText('')

    def Multiply(self):

        # MatrixA

        int00 = self.ui.matrixA_00.text()
        int01 = self.ui.matrixA_01.text()
        int02 = self.ui.matrixA_02.text()
        int03 = self.ui.matrixA_03.text()
        int04 = self.ui.matrixA_04.text()
        int05 = self.ui.matrixA_05.text()
        int06 = self.ui.matrixA_06.text()
        int07 = self.ui.matrixA_07.text()
        int08 = self.ui.matrixA_08.text()
        int09 = self.ui.matrixA_09.text()
        int10 = self.ui.matrixA_10.text()
        int11 = self.ui.matrixA_11.text()
        int12 = self.ui.matrixA_12.text()
        int13 = self.ui.matrixA_13.text()
        int14 = self.ui.matrixA_14.text()
        int15 = self.ui.matrixA_15.text()
        int16 = self.ui.matrixA_16.text()
        int17 = self.ui.matrixA_17.text()
        int18 = self.ui.matrixA_18.text()
        int19 = self.ui.matrixA_19.text()
        int20 = self.ui.matrixA_20.text()
        int21 = self.ui.matrixA_21.text()
        int22 = self.ui.matrixA_22.text()
        int23 = self.ui.matrixA_23.text()
        int24 = self.ui.matrixA_24.text()

        # MatrixB

        int25 = self.ui.matrixB_00.text()
        int26 = self.ui.matrixB_01.text()
        int27 = self.ui.matrixB_02.text()
        int28 = self.ui.matrixB_03.text()
        int29 = self.ui.matrixB_04.text()
        int30 = self.ui.matrixB_05.text()
        int31 = self.ui.matrixB_06.text()
        int32 = self.ui.matrixB_07.text()
        int33 = self.ui.matrixB_08.text()
        int34 = self.ui.matrixB_09.text()
        int35 = self.ui.matrixB_10.text()
        int36 = self.ui.matrixB_11.text()
        int37 = self.ui.matrixB_12.text()
        int38 = self.ui.matrixB_13.text()
        int39 = self.ui.matrixB_14.text()
        int40 = self.ui.matrixB_15.text()
        int41 = self.ui.matrixB_16.text()
        int42 = self.ui.matrixB_17.text()
        int43 = self.ui.matrixB_18.text()
        int44 = self.ui.matrixB_19.text()
        int45 = self.ui.matrixB_20.text()
        int46 = self.ui.matrixB_21.text()
        int47 = self.ui.matrixB_22.text()
        int48 = self.ui.matrixB_23.text()
        int49 = self.ui.matrixB_24.text()

        matrixA = [[int00, int01, int02, int03, int04],
                   [int05, int06, int07, int08, int09],
                   [int10, int11, int12, int13, int14],
                   [int15, int16, int17, int18, int19],
                   [int20, int21, int22, int23, int24]]
        matrixB = [[int25, int26, int27, int28, int29],
                   [int30, int31, int32, int33, int34],
                   [int35, int36, int37, int38, int39],
                   [int40, int41, int42, int43, int44],
                   [int45, int46, int47, int48, int49]]

        new_matrixA = [[instance for instance in sublist if len(
            instance) > 0] for sublist in matrixA]
        new_matrixA = list(filter(None, new_matrixA))
        matrixAdimensions = [len(new_matrixA), len(new_matrixA[0])]
        new_matrixA = np.array(new_matrixA)
        new_matrixA = new_matrixA.astype(np.int)
        new_matrixB = [[instance for instance in sublist if len(
            instance) > 0] for sublist in matrixB]
        new_matrixB = list(filter(None, new_matrixB))
        matrixBdimensions = [len(new_matrixB), len(new_matrixB[0])]
        new_matrixB = np.array(new_matrixB)
        new_matrixB = new_matrixB.astype(np.int)
        if (matrixAdimensions[1] == matrixBdimensions[0]):
            matrixC = new_matrixA.dot(new_matrixB)
            matrixC = np.array(matrixC)
            target = np.zeros((5, 5))
            target[:matrixC.shape[0], :matrixC.shape[1]] = matrixC
            target = target.astype(np.int)
            target = target.astype(np.str)
            target[target == '0'] = ''
            for i in range(len(new_matrixA[0])):
                for j in range(len(new_matrixB[1])):
                    if(target[i][j] == ''):
                        target[i][j] = '0'
        

            # MatrixC
            self.ui.matrixC_00.setText(target[0][0])
            self.ui.matrixC_01.setText(target[0][1])
            self.ui.matrixC_02.setText(target[0][2])
            self.ui.matrixC_03.setText(target[0][3])
            self.ui.matrixC_04.setText(target[0][4])
            self.ui.matrixC_05.setText(target[1][0])
            self.ui.matrixC_06.setText(target[1][1])
            self.ui.matrixC_07.setText(target[1][2])
            self.ui.matrixC_08.setText(target[1][3])
            self.ui.matrixC_09.setText(target[1][4])
            self.ui.matrixC_10.setText(target[2][0])
            self.ui.matrixC_11.setText(target[2][1])
            self.ui.matrixC_12.setText(target[2][2])
            self.ui.matrixC_13.setText(target[2][3])
            self.ui.matrixC_14.setText(target[2][4])
            self.ui.matrixC_15.setText(target[3][0])
            self.ui.matrixC_16.setText(target[3][1])
            self.ui.matrixC_17.setText(target[3][2])
            self.ui.matrixC_18.setText(target[3][3])
            self.ui.matrixC_19.setText(target[3][4])
            self.ui.matrixC_20.setText(target[4][0])
            self.ui.matrixC_21.setText(target[4][1])
            self.ui.matrixC_22.setText(target[4][2])
            self.ui.matrixC_23.setText(target[4][3])
            self.ui.matrixC_24.setText(target[4][4])
            self.ui.textLabel.setText('multiplication completed')
        elif (matrixAdimensions[1] != matrixBdimensions[0]):
            self.ui.textLabel.setText('wrong matrix dimensions')
            self.ui.matrixC_00.setText('')
            self.ui.matrixC_01.setText('')
            self.ui.matrixC_02.setText('')
            self.ui.matrixC_03.setText('')
            self.ui.matrixC_04.setText('')
            self.ui.matrixC_05.setText('')
            self.ui.matrixC_06.setText('')
            self.ui.matrixC_07.setText('')
            self.ui.matrixC_08.setText('')
            self.ui.matrixC_09.setText('')
            self.ui.matrixC_10.setText('')
            self.ui.matrixC_11.setText('')
            self.ui.matrixC_12.setText('')
            self.ui.matrixC_13.setText('')
            self.ui.matrixC_14.setText('')
            self.ui.matrixC_15.setText('')
            self.ui.matrixC_16.setText('')
            self.ui.matrixC_17.setText('')
            self.ui.matrixC_18.setText('')
            self.ui.matrixC_19.setText('')
            self.ui.matrixC_20.setText('')
            self.ui.matrixC_21.setText('')
            self.ui.matrixC_22.setText('')
            self.ui.matrixC_23.setText('')
            self.ui.matrixC_24.setText('')

    def DetA(self):

        # MatrixA

        int00 = self.ui.matrixA_00.text()
        int01 = self.ui.matrixA_01.text()
        int02 = self.ui.matrixA_02.text()
        int03 = self.ui.matrixA_03.text()
        int04 = self.ui.matrixA_04.text()
        int05 = self.ui.matrixA_05.text()
        int06 = self.ui.matrixA_06.text()
        int07 = self.ui.matrixA_07.text()
        int08 = self.ui.matrixA_08.text()
        int09 = self.ui.matrixA_09.text()
        int10 = self.ui.matrixA_10.text()
        int11 = self.ui.matrixA_11.text()
        int12 = self.ui.matrixA_12.text()
        int13 = self.ui.matrixA_13.text()
        int14 = self.ui.matrixA_14.text()
        int15 = self.ui.matrixA_15.text()
        int16 = self.ui.matrixA_16.text()
        int17 = self.ui.matrixA_17.text()
        int18 = self.ui.matrixA_18.text()
        int19 = self.ui.matrixA_19.text()
        int20 = self.ui.matrixA_20.text()
        int21 = self.ui.matrixA_21.text()
        int22 = self.ui.matrixA_22.text()
        int23 = self.ui.matrixA_23.text()
        int24 = self.ui.matrixA_24.text()

        matrixA = [[int00, int01, int02, int03, int04],
                   [int05, int06, int07, int08, int09],
                   [int10, int11, int12, int13, int14],
                   [int15, int16, int17, int18, int19],
                   [int20, int21, int22, int23, int24]]

        new_matrixA = [[instance for instance in sublist if len(
            instance) > 0] for sublist in matrixA]
        new_matrixA = list(filter(None, new_matrixA))
        new_matrixA = np.array(new_matrixA)
        new_matrixA = new_matrixA.astype(np.int)
        matrixAdimensions = [len(new_matrixA), len(new_matrixA[0])]
        if(matrixAdimensions[0] == matrixAdimensions[1]):
            self.ui.textLabel.setText(str(int((np.linalg.det(new_matrixA)))))
        else:
            self.ui.textLabel.setText('matrix should be square')

    def DetB(self):

        # MatrixB

        int25 = self.ui.matrixB_00.text()
        int26 = self.ui.matrixB_01.text()
        int27 = self.ui.matrixB_02.text()
        int28 = self.ui.matrixB_03.text()
        int29 = self.ui.matrixB_04.text()
        int30 = self.ui.matrixB_05.text()
        int31 = self.ui.matrixB_06.text()
        int32 = self.ui.matrixB_07.text()
        int33 = self.ui.matrixB_08.text()
        int34 = self.ui.matrixB_09.text()
        int35 = self.ui.matrixB_10.text()
        int36 = self.ui.matrixB_11.text()
        int37 = self.ui.matrixB_12.text()
        int38 = self.ui.matrixB_13.text()
        int39 = self.ui.matrixB_14.text()
        int40 = self.ui.matrixB_15.text()
        int41 = self.ui.matrixB_16.text()
        int42 = self.ui.matrixB_17.text()
        int43 = self.ui.matrixB_18.text()
        int44 = self.ui.matrixB_19.text()
        int45 = self.ui.matrixB_20.text()
        int46 = self.ui.matrixB_21.text()
        int47 = self.ui.matrixB_22.text()
        int48 = self.ui.matrixB_23.text()
        int49 = self.ui.matrixB_24.text()

        matrixB = [[int25, int26, int27, int28, int29],
                   [int30, int31, int32, int33, int34],
                   [int35, int36, int37, int38, int39],
                   [int40, int41, int42, int43, int44],
                   [int45, int46, int47, int48, int49]]

        new_matrixB = [[instance for instance in sublist if len(
            instance) > 0] for sublist in matrixB]
        new_matrixB = list(filter(None, new_matrixB))
        new_matrixB = np.array(new_matrixB)
        new_matrixB = new_matrixB.astype(np.int)
        matrixBdimensions = [len(new_matrixB), len(new_matrixB[0])]
        if(matrixBdimensions[0] == matrixBdimensions[1]):
            self.ui.textLabel.setText(str(int((np.linalg.det(new_matrixB)))))
        else:
            self.ui.textLabel.setText('matrix should be square')

    def DetC(self):

        # MatrixC

        int50 = self.ui.matrixC_00.text()
        int51 = self.ui.matrixC_01.text()
        int52 = self.ui.matrixC_02.text()
        int53 = self.ui.matrixC_03.text()
        int54 = self.ui.matrixC_04.text()
        int55 = self.ui.matrixC_05.text()
        int56 = self.ui.matrixC_06.text()
        int57 = self.ui.matrixC_07.text()
        int58 = self.ui.matrixC_08.text()
        int59 = self.ui.matrixC_09.text()
        int60 = self.ui.matrixC_10.text()
        int61 = self.ui.matrixC_11.text()
        int62 = self.ui.matrixC_12.text()
        int63 = self.ui.matrixC_13.text()
        int64 = self.ui.matrixC_14.text()
        int65 = self.ui.matrixC_15.text()
        int66 = self.ui.matrixC_16.text()
        int67 = self.ui.matrixC_17.text()
        int68 = self.ui.matrixC_18.text()
        int69 = self.ui.matrixC_19.text()
        int70 = self.ui.matrixC_20.text()
        int71 = self.ui.matrixC_21.text()
        int72 = self.ui.matrixC_22.text()
        int73 = self.ui.matrixC_23.text()
        int74 = self.ui.matrixC_24.text()

        matrixC = [[int50, int51, int52, int53, int54],
                   [int55, int56, int57, int58, int59],
                   [int60, int61, int62, int63, int64],
                   [int65, int66, int67, int68, int69],
                   [int70, int71, int72, int73, int74]]

        new_matrixC = [[instance for instance in sublist if len(
            instance) > 0] for sublist in matrixC]
        new_matrixC = list(filter(None, new_matrixC))
        new_matrixC = np.array(new_matrixC)
        new_matrixC = new_matrixC.astype(np.int)
        matrixCdimensions = [len(new_matrixC), len(new_matrixC[0])]
        if(matrixCdimensions[0] == matrixCdimensions[1]):
            self.ui.textLabel.setText(str(int((np.linalg.det(new_matrixC)))))
        else:
            self.ui.textLabel.setText('matrix should be square')

    def TransposeA(self):

        # MatrixA

        int00 = self.ui.matrixA_00.text()
        int01 = self.ui.matrixA_01.text()
        int02 = self.ui.matrixA_02.text()
        int03 = self.ui.matrixA_03.text()
        int04 = self.ui.matrixA_04.text()
        int05 = self.ui.matrixA_05.text()
        int06 = self.ui.matrixA_06.text()
        int07 = self.ui.matrixA_07.text()
        int08 = self.ui.matrixA_08.text()
        int09 = self.ui.matrixA_09.text()
        int10 = self.ui.matrixA_10.text()
        int11 = self.ui.matrixA_11.text()
        int12 = self.ui.matrixA_12.text()
        int13 = self.ui.matrixA_13.text()
        int14 = self.ui.matrixA_14.text()
        int15 = self.ui.matrixA_15.text()
        int16 = self.ui.matrixA_16.text()
        int17 = self.ui.matrixA_17.text()
        int18 = self.ui.matrixA_18.text()
        int19 = self.ui.matrixA_19.text()
        int20 = self.ui.matrixA_20.text()
        int21 = self.ui.matrixA_21.text()
        int22 = self.ui.matrixA_22.text()
        int23 = self.ui.matrixA_23.text()
        int24 = self.ui.matrixA_24.text()

        matrixA = [[int00, int01, int02, int03, int04],
                   [int05, int06, int07, int08, int09],
                   [int10, int11, int12, int13, int14],
                   [int15, int16, int17, int18, int19],
                   [int20, int21, int22, int23, int24]]

        new_matrixA = [[instance for instance in sublist if len(
            instance) > 0] for sublist in matrixA]
        new_matrixA = list(filter(None, new_matrixA))
        matrixAdimensions = [len(new_matrixA), len(new_matrixA[0])]
        new_matrixA = np.array(new_matrixA)
        new_matrixA = new_matrixA.astype(np.int)
        matrixC = new_matrixA.transpose()
        matrixC = np.array(matrixC)
        target = np.zeros((5, 5))
        target[:matrixC.shape[0], :matrixC.shape[1]] = matrixC
        target = target.astype(np.int)
        target = target.astype(np.str)
        target[target == '0'] = ''
        for i in range(len(new_matrixA[0])):
            for j in range(len(new_matrixA)):
                if(target[i][j] == ''):
                    target[i][j] = '0'

        # MatrixA
        self.ui.matrixA_00.setText(target[0][0])
        self.ui.matrixA_01.setText(target[0][1])
        self.ui.matrixA_02.setText(target[0][2])
        self.ui.matrixA_03.setText(target[0][3])
        self.ui.matrixA_04.setText(target[0][4])
        self.ui.matrixA_05.setText(target[1][0])
        self.ui.matrixA_06.setText(target[1][1])
        self.ui.matrixA_07.setText(target[1][2])
        self.ui.matrixA_08.setText(target[1][3])
        self.ui.matrixA_09.setText(target[1][4])
        self.ui.matrixA_10.setText(target[2][0])
        self.ui.matrixA_11.setText(target[2][1])
        self.ui.matrixA_12.setText(target[2][2])
        self.ui.matrixA_13.setText(target[2][3])
        self.ui.matrixA_14.setText(target[2][4])
        self.ui.matrixA_15.setText(target[3][0])
        self.ui.matrixA_16.setText(target[3][1])
        self.ui.matrixA_17.setText(target[3][2])
        self.ui.matrixA_18.setText(target[3][3])
        self.ui.matrixA_19.setText(target[3][4])
        self.ui.matrixA_20.setText(target[4][0])
        self.ui.matrixA_21.setText(target[4][1])
        self.ui.matrixA_22.setText(target[4][2])
        self.ui.matrixA_23.setText(target[4][3])
        self.ui.matrixA_24.setText(target[4][4])
        self.ui.textLabel.setText('transposion completed')

    def TransposeB(self):

        # MatrixB

        int25 = self.ui.matrixB_00.text()
        int26 = self.ui.matrixB_01.text()
        int27 = self.ui.matrixB_02.text()
        int28 = self.ui.matrixB_03.text()
        int29 = self.ui.matrixB_04.text()
        int30 = self.ui.matrixB_05.text()
        int31 = self.ui.matrixB_06.text()
        int32 = self.ui.matrixB_07.text()
        int33 = self.ui.matrixB_08.text()
        int34 = self.ui.matrixB_09.text()
        int35 = self.ui.matrixB_10.text()
        int36 = self.ui.matrixB_11.text()
        int37 = self.ui.matrixB_12.text()
        int38 = self.ui.matrixB_13.text()
        int39 = self.ui.matrixB_14.text()
        int40 = self.ui.matrixB_15.text()
        int41 = self.ui.matrixB_16.text()
        int42 = self.ui.matrixB_17.text()
        int43 = self.ui.matrixB_18.text()
        int44 = self.ui.matrixB_19.text()
        int45 = self.ui.matrixB_20.text()
        int46 = self.ui.matrixB_21.text()
        int47 = self.ui.matrixB_22.text()
        int48 = self.ui.matrixB_23.text()
        int49 = self.ui.matrixB_24.text()

        matrixB = [[int25, int26, int27, int28, int29],
                   [int30, int31, int32, int33, int34],
                   [int35, int36, int37, int38, int39],
                   [int40, int41, int42, int43, int44],
                   [int45, int46, int47, int48, int49]]

        new_matrixB = [[instance for instance in sublist if len(
            instance) > 0] for sublist in matrixB]
        new_matrixB = list(filter(None, new_matrixB))
        matrixBdimensions = [len(new_matrixB), len(new_matrixB[0])]
        new_matrixB = np.array(new_matrixB)
        new_matrixB = new_matrixB.astype(np.int)
        matrixC = new_matrixB.transpose()
        matrixC = np.array(matrixC)
        target = np.zeros((5, 5))
        target[:matrixC.shape[0], :matrixC.shape[1]] = matrixC
        target = target.astype(np.int)
        target = target.astype(np.str)
        target[target == '0'] = ''
        for i in range(len(new_matrixB[0])):
            for j in range(len(new_matrixB)):
                if(target[i][j] == ''):
                    target[i][j] = '0'

        # MatrixB
        self.ui.matrixB_00.setText(target[0][0])
        self.ui.matrixB_01.setText(target[0][1])
        self.ui.matrixB_02.setText(target[0][2])
        self.ui.matrixB_03.setText(target[0][3])
        self.ui.matrixB_04.setText(target[0][4])
        self.ui.matrixB_05.setText(target[1][0])
        self.ui.matrixB_06.setText(target[1][1])
        self.ui.matrixB_07.setText(target[1][2])
        self.ui.matrixB_08.setText(target[1][3])
        self.ui.matrixB_09.setText(target[1][4])
        self.ui.matrixB_10.setText(target[2][0])
        self.ui.matrixB_11.setText(target[2][1])
        self.ui.matrixB_12.setText(target[2][2])
        self.ui.matrixB_13.setText(target[2][3])
        self.ui.matrixB_14.setText(target[2][4])
        self.ui.matrixB_15.setText(target[3][0])
        self.ui.matrixB_16.setText(target[3][1])
        self.ui.matrixB_17.setText(target[3][2])
        self.ui.matrixB_18.setText(target[3][3])
        self.ui.matrixB_19.setText(target[3][4])
        self.ui.matrixB_20.setText(target[4][0])
        self.ui.matrixB_21.setText(target[4][1])
        self.ui.matrixB_22.setText(target[4][2])
        self.ui.matrixB_23.setText(target[4][3])
        self.ui.matrixB_24.setText(target[4][4])
        self.ui.textLabel.setText('transposion completed')

    def TransposeC(self):

        # MatrixC

        int50 = self.ui.matrixC_00.text()
        int51 = self.ui.matrixC_01.text()
        int52 = self.ui.matrixC_02.text()
        int53 = self.ui.matrixC_03.text()
        int54 = self.ui.matrixC_04.text()
        int55 = self.ui.matrixC_05.text()
        int56 = self.ui.matrixC_06.text()
        int57 = self.ui.matrixC_07.text()
        int58 = self.ui.matrixC_08.text()
        int59 = self.ui.matrixC_09.text()
        int60 = self.ui.matrixC_10.text()
        int61 = self.ui.matrixC_11.text()
        int62 = self.ui.matrixC_12.text()
        int63 = self.ui.matrixC_13.text()
        int64 = self.ui.matrixC_14.text()
        int65 = self.ui.matrixC_15.text()
        int66 = self.ui.matrixC_16.text()
        int67 = self.ui.matrixC_17.text()
        int68 = self.ui.matrixC_18.text()
        int69 = self.ui.matrixC_19.text()
        int70 = self.ui.matrixC_20.text()
        int71 = self.ui.matrixC_21.text()
        int72 = self.ui.matrixC_22.text()
        int73 = self.ui.matrixC_23.text()
        int74 = self.ui.matrixC_24.text()

        matrixC = [[int50, int51, int52, int53, int54],
                   [int55, int56, int57, int58, int59],
                   [int60, int61, int62, int63, int64],
                   [int65, int66, int67, int68, int69],
                   [int70, int71, int72, int73, int74]]

        new_matrixC = [[instance for instance in sublist if len(
            instance) > 0] for sublist in matrixC]
        new_matrixC = list(filter(None, new_matrixC))
        matrixCdimensions = [len(new_matrixC), len(new_matrixC[0])]
        new_matrixC = np.array(new_matrixC)
        new_matrixC = new_matrixC.astype(np.int)
        matrixD = new_matrixC.transpose()
        matrixD = np.array(matrixD)
        target = np.zeros((5, 5))
        target[:matrixD.shape[0], :matrixD.shape[1]] = matrixD
        target = target.astype(np.int)
        target = target.astype(np.str)
        target[target == '0'] = ''
        for i in range(len(new_matrixC[0])):
            for j in range(len(new_matrixC)):
                if(target[i][j] == ''):
                    target[i][j] = '0'

        # MatrixC
        self.ui.matrixC_00.setText(target[0][0])
        self.ui.matrixC_01.setText(target[0][1])
        self.ui.matrixC_02.setText(target[0][2])
        self.ui.matrixC_03.setText(target[0][3])
        self.ui.matrixC_04.setText(target[0][4])
        self.ui.matrixC_05.setText(target[1][0])
        self.ui.matrixC_06.setText(target[1][1])
        self.ui.matrixC_07.setText(target[1][2])
        self.ui.matrixC_08.setText(target[1][3])
        self.ui.matrixC_09.setText(target[1][4])
        self.ui.matrixC_10.setText(target[2][0])
        self.ui.matrixC_11.setText(target[2][1])
        self.ui.matrixC_12.setText(target[2][2])
        self.ui.matrixC_13.setText(target[2][3])
        self.ui.matrixC_14.setText(target[2][4])
        self.ui.matrixC_15.setText(target[3][0])
        self.ui.matrixC_16.setText(target[3][1])
        self.ui.matrixC_17.setText(target[3][2])
        self.ui.matrixC_18.setText(target[3][3])
        self.ui.matrixC_19.setText(target[3][4])
        self.ui.matrixC_20.setText(target[4][0])
        self.ui.matrixC_21.setText(target[4][1])
        self.ui.matrixC_22.setText(target[4][2])
        self.ui.matrixC_23.setText(target[4][3])
        self.ui.matrixC_24.setText(target[4][4])
        self.ui.textLabel.setText('transposion completed')

    def ClearA(self):

        self.ui.matrixA_00.setText('')
        self.ui.matrixA_01.setText('')
        self.ui.matrixA_02.setText('')
        self.ui.matrixA_03.setText('')
        self.ui.matrixA_04.setText('')
        self.ui.matrixA_05.setText('')
        self.ui.matrixA_06.setText('')
        self.ui.matrixA_07.setText('')
        self.ui.matrixA_08.setText('')
        self.ui.matrixA_09.setText('')
        self.ui.matrixA_10.setText('')
        self.ui.matrixA_11.setText('')
        self.ui.matrixA_12.setText('')
        self.ui.matrixA_13.setText('')
        self.ui.matrixA_14.setText('')
        self.ui.matrixA_15.setText('')
        self.ui.matrixA_16.setText('')
        self.ui.matrixA_17.setText('')
        self.ui.matrixA_18.setText('')
        self.ui.matrixA_19.setText('')
        self.ui.matrixA_20.setText('')
        self.ui.matrixA_21.setText('')
        self.ui.matrixA_22.setText('')
        self.ui.matrixA_23.setText('')
        self.ui.matrixA_24.setText('')

    def ClearB(self):

        self.ui.matrixB_00.setText('')
        self.ui.matrixB_01.setText('')
        self.ui.matrixB_02.setText('')
        self.ui.matrixB_03.setText('')
        self.ui.matrixB_04.setText('')
        self.ui.matrixB_05.setText('')
        self.ui.matrixB_06.setText('')
        self.ui.matrixB_07.setText('')
        self.ui.matrixB_08.setText('')
        self.ui.matrixB_09.setText('')
        self.ui.matrixB_10.setText('')
        self.ui.matrixB_11.setText('')
        self.ui.matrixB_12.setText('')
        self.ui.matrixB_13.setText('')
        self.ui.matrixB_14.setText('')
        self.ui.matrixB_15.setText('')
        self.ui.matrixB_16.setText('')
        self.ui.matrixB_17.setText('')
        self.ui.matrixB_18.setText('')
        self.ui.matrixB_19.setText('')
        self.ui.matrixB_20.setText('')
        self.ui.matrixB_21.setText('')
        self.ui.matrixB_22.setText('')
        self.ui.matrixB_23.setText('')
        self.ui.matrixB_24.setText('')

    def ClearC(self):

        self.ui.matrixC_00.setText('')
        self.ui.matrixC_01.setText('')
        self.ui.matrixC_02.setText('')
        self.ui.matrixC_03.setText('')
        self.ui.matrixC_04.setText('')
        self.ui.matrixC_05.setText('')
        self.ui.matrixC_06.setText('')
        self.ui.matrixC_07.setText('')
        self.ui.matrixC_08.setText('')
        self.ui.matrixC_09.setText('')
        self.ui.matrixC_10.setText('')
        self.ui.matrixC_11.setText('')
        self.ui.matrixC_12.setText('')
        self.ui.matrixC_13.setText('')
        self.ui.matrixC_14.setText('')
        self.ui.matrixC_15.setText('')
        self.ui.matrixC_16.setText('')
        self.ui.matrixC_17.setText('')
        self.ui.matrixC_18.setText('')
        self.ui.matrixC_19.setText('')
        self.ui.matrixC_20.setText('')
        self.ui.matrixC_21.setText('')
        self.ui.matrixC_22.setText('')
        self.ui.matrixC_23.setText('')
        self.ui.matrixC_24.setText('')


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())

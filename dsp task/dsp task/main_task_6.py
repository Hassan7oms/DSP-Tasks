from main_task_4 import *
from CompareSignal import *
import math
import os
from tkinter.filedialog import askdirectory

def Convolotion(signal1, signal2):
    indices1, amplitudes1 = signal1
    indices2, amplitudes2 = signal2
    result_indices = range(int(indices1[0]), int(indices1[-1] + 1))
    result_amplitudes = []
    norm1=0
    norm2=0
    norm=0
    for i in amplitudes1:
        norm1+=(i*i)
    for i in amplitudes2:
        norm2+=(i*i)
    norm=math.sqrt(norm1*norm2)
    norm/=len(indices1)
    bst_corr=0
    delay_samples=0
    for n in result_indices:
        i=0
        sum=0
        for j in range(n,int(indices1[-1] + 1)):
            sum+=(amplitudes1[i]*amplitudes2[j])
            i+=1
        for j in range(0,n):
            sum+=(amplitudes1[i]*amplitudes2[j])
            i+=1
        sum/=len(indices1)
        sum/=norm
        if sum>bst_corr:
            bst_corr=sum
            delay_samples=n
        result_amplitudes.append(sum)
    
    return delay_samples,bst_corr,result_indices, result_amplitudes

def read_test(file_path):
    print(file_path)
    with open(file_path, 'r') as file:
        lines = file.readlines()
        indices = []
        values = []
        cnt=0
        for line in lines[0:]:
                value = float(line.strip())
                indices.append(cnt)
                cnt+=1
                values.append(value)
                #print(value)
    return np.array(indices), np.array(values)

def read_folder():
    # Let the user select a folder
    folder_path = askdirectory(title="Select Folder with Signal Files")
    if not folder_path:
        print("No folder selected.")
        return []
    folder_path = os.path.normpath(folder_path)
    signals = []  # List to store signals

    # Iterate through all .txt files in the selected folder
    for file_name in os.listdir(folder_path):
        if file_name.endswith(".txt"):
            file_path = os.path.join(folder_path, file_name)
            try:
                signals.append(read_test(file_path))
            except Exception as e:
                print(f"Error reading file {file_name}: {e}")

    print(f"Signals loaded from {len(signals)} files.")
    return signals

def classify(signal,folder):
    A=0
    for i in folder[0]:
        delay_samples,bst_corr,result_indices, result_amplitudes = Convolotion(signal, i)
        A+=bst_corr
    A/=len(folder[0])

    B=0
    for i in folder[1]:
        delay_samples,bst_corr,result_indices, result_amplitudes = Convolotion(signal, i)
        B+=bst_corr
    B/=len(folder[1])
    return A,B


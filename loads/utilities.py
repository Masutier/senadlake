import os
from django.conf import settings


def createFolder(filepath):
    os.makedirs(filepath)
    endDir = filepath
    return endDir


def newFolder(filepath):
    if filepath:
        folderExist = os.path.isdir(filepath)
        if not folderExist:
            endDir = createFolder(filepath)
        else:
            endDir = filepath
    else:
        folderExist = os.path.isdir(filepath)
        if not folderExist:
            endDir = createFolder(filepath)
        else:
            endDir = filepath

    return endDir


def fileList(fileslist):
    filesNames = []
    
    for item in fileslist:
        filex = (item.file).name
        fname = filex.split('.')
        filesNames.append(fname[0])

    return filesNames


def singleList(csvFiles, jsonFiles, xlsxFiles, pdfFiles):
    dataSet = []
    csvSingles = []
    jsonSingles = []
    xlsxSingles = []
    pdfSingles = []

    csvCollect = fileList(csvFiles)
    jsonCollect = fileList(jsonFiles)
    xlsxCollect = fileList(xlsxFiles)
    pdfCollect = fileList(pdfFiles)

    for csv in csvFiles:
        if csv.file_name in jsonCollect:
            dataSet.append(csv)
        elif csv.file_name in xlsxCollect:
            dataSet.append(csv)
        elif csv.file_name in pdfCollect:
            dataSet.append(csv)
        else:
            csvSingles.append(csv)

    for json in jsonFiles:
        if json.file_name in csvCollect:
            dataSet.append(json)
        elif json.file_name in xlsxCollect:
            dataSet.append(json)
        elif json.file_name in pdfCollect:
            dataSet.append(json)
        else:
            jsonSingles.append(json)

    for xlsx in xlsxFiles:
        if xlsx.file_name in csvCollect:
            dataSet.append(xlsx)
        elif xlsx.file_name in jsonCollect:
            dataSet.append(xlsx)
        elif xlsx.file_name in pdfCollect:
            dataSet.append(xlsx)
        else:
            xlsxSingles.append(xlsx)

    for pdf in pdfFiles:
        if pdf.file_name in csvCollect:
            dataSet.append(pdf)
        elif pdf.file_name in jsonCollect:
            dataSet.append(pdf)
        elif pdf.file_name in xlsxCollect:
            dataSet.append(pdf)
        else:
            pdfSingles.append(pdf)

    return csvSingles, jsonSingles, xlsxSingles, pdfSingles


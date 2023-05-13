import os
import json
from django.conf import settings
from django.contrib import messages
from django.shortcuts import render, redirect
from .models import LoadFiles
from .forms import loadFileForm
from .utilities import fileList, singleList, newFolder
from senadlake.dbases import extensions
import pandas as pd


validExt, validExtPro = extensions()
origen_path = "/home/gabriel/Downloads/"
filepath = os.path.join(settings.BASE_DIR, "FILES/json/")


def loadFile(request):
    if request.method == 'POST':
        form = loadFileForm(request.POST, request.FILES)
        if form.is_valid():
            endDir = newFolder(filepath)
            pform = form.save(commit=False)
            inputFile = request.FILES['inputFile']
            namefile = inputFile.name
            filenamex = namefile.split('.')

            if filenamex[-1] == 'csv':
                df = pd.read_csv(inputFile, low_memory=False)
                jsonFile = df.to_json(endDir + filenamex[0] + ".json.gz", indent=4, orient='records', compression='gzip', force_ascii=False)

                pdcolumns = df.columns.tolist()
                pform.jsonFile = namefile
                pform.file_link = endDir + filenamex[0] + ".json.gz"
                pform.file_ext = filenamex[-1]
                pform.file_name = namefile
                pform.file_columns = pdcolumns
                pform.file_numcols = df.shape[1] #- To count columns
                pform.file_numrows = df.shape[0] #- To count rows
                pform.data_set = False
                pform.save()
                messages.success(request, "The file was saved successfully")

                return redirect("allFiles")

            elif filenamex[-1] == 'xlsx':
                df = pd.ExcelFile(inputFile)

                if len(df.sheet_names) > 1:
                    sheets = []

                    for sheet in df.sheet_names:
                        fullSheet = pd.read_excel(inputFile, sheet_name=sheet)
                        jsonOutput_gz = filepath + filenamex[0] + "_" + sheet + ".json" + ".gz"
                        output = fullSheet.to_json(jsonOutput_gz, indent=4, orient='records', compression='gzip', force_ascii=False)
                        sheets.append(sheet)

                    pdcolumns = fullSheet.columns.tolist()
                    pform.jsonFile = namefile
                    pform.file_link = filepath + filenamex[0] + "_<sheet>.json.gz"
                    pform.file_ext = filenamex[-1]
                    pform.file_name = namefile
                    pform.file_columns = pdcolumns
                    pform.file_numcols = fullSheet.shape[1] #- To count columns
                    pform.file_numrows = fullSheet.shape[0] #- To count rows
                    pform.data_set = True
                    pform.sheet_set = sheets
                    pform.save()

                    return redirect("allFiles")
                else:
                    sheet = str(df.sheet_names)
                    df = pd.read_excel(inputFile)
                    jsonOutput_gz = filepath + filenamex[0] + "_" + sheet + ".json" + ".gz"
                    output = df.to_json(jsonOutput_gz, indent=4, orient='records', compression='gzip', force_ascii=False)

                    pdcolumns = df.columns.tolist()
                    pform.jsonFile = namefile
                    pform.file_link = filepath + filenamex[0] + "_" + sheet + ".json.gz"
                    pform.file_ext = filenamex[-1]
                    pform.file_name = namefile
                    pform.file_columns = pdcolumns
                    pform.file_numcols = df.shape[1] #- To count columns
                    pform.file_numrows = df.shape[0] #- To count rows
                    pform.data_set = False
                    pform.save()
                    messages.success(request, "The file was saved successfully")

                    return redirect("allFiles")
            else:
                extMess = "The file has not a valid extension. Please, verify name and extension and try again."
                messages.warning(request, "The file was NOT saved ** WARNING ** " + extMess)
                return redirect("home")
        else:
            messages.error(request + "Something went wrong. " + form.errors)
            return redirect("home")
    else:
        form = loadFileForm()

    context={"title": "Load Files", "banner":"Load Files To Data Lake", 'form':form}
    return render(request, 'loads/loadFile.html', context)


def xlsAllFiles(request):
    if request.method == 'POST':
        form = loadFileForm(request.POST, request.FILES)

        inputFile = request.FILES['inputFile']
        sheetName = request.POST['sheetName']
        separator = request.POST['separator']

        print('inputFile', inputFile)
        filenamex = inputFile.split('.')
        print('filenamex', filenamex)
        print('sheetName', sheetName)

        if filenamex[-1] != "xlsx":
            messages.success(request, "The file you enter is not an excel file, please check the file and try again")
            return redirect('home')

        messages.success(request, "The file xxxxxxxxvvvvvvvvv")
        return redirect('home')

    context={"title": "XLSX All", "sheetName":sheetName}
    return render(request, 'xls_all/xlsLoad.html', context)


def setDetail(request, pk):
    detailIn = LoadFiles.objects.get(id=pk)

    context={"title": "Detalle", "banner":"Pagina en Construccion"}
    return render(request, 'senadlake/errors/404.html', context)


def csvCall(request, pk):
    fileIn = LoadFiles.objects.get(id=pk)
    nameff = fileIn.file_name.split('.')
    nameOut = nameff[0]

    data = pd.read_json(fileIn.file_link)
    csvout = data.to_csv(nameOut + ".csv", sep=';', encoding='utf-8')

    return redirect('home')
    

def xlsxCall(request, pk):
    fileIn = LoadFiles.objects.get(id=pk)
    nameff = fileIn.file_name.split('.')
    nameOut = nameff[0]

    data = pd.read_json(fileIn.file_link)
    csvout = data.to_excel(nameOut + ".xlsx", sheet_name="Sheet1", index=False)
    return redirect('home')


def jsonCall(request, pk):
    print("jsonCall", pk)
    return redirect('home')


def pdfCall(request, pk):
    print("pdfCall", pk)
    return redirect('home')


def allFiles(request):
    dataSets = []
    setsCount = 0

    allFiles = LoadFiles.objects.all()
    dataSests = LoadFiles.objects.filter(data_set=1)

    for sets in dataSests:
        setsCount += 1

    allcount = allFiles.count()

    context={"title": "All Files", "banner":"Files in DataBase"
    , 'allFiles':allFiles, 'allcount':allcount
    , 'dataSets':dataSets, 'setsCount':setsCount

    }
    return render(request, 'loads/allFiles.html', context)


def setFiles(request):
    csvFiles = LoadFiles.objects.filter(file_ext='csv')
    jsonFiles = LoadFiles.objects.filter(file_ext='json')
    xlsxFiles = LoadFiles.objects.filter(file_ext='xlsx')
    pdfFiles = LoadFiles.objects.filter(file_ext='pdf')

    csvSingles, jsonSingles, xlsxSingles, pdfSingles = singleList(csvFiles, jsonFiles, xlsxFiles, pdfFiles)

    context={"title": "DataSets", "banner":"Single Files For DataSets"
    , 'csvSingles':csvSingles, 'jsonSingles':jsonSingles
    , 'xlsxSingles':xlsxSingles, 'pdfSingles':pdfSingles
    }
    return render(request, 'loads/setFiles.html', context)


def searchFiles(request):
    system = request.POST.get('system', None)

    if system == "csv":
        files = LoadFiles.objects.filter(file_ext='csv')
    elif system == "json":
        files = LoadFiles.objects.filter(file_ext='json')
    elif system == "xlsx":
        files = LoadFiles.objects.filter(file_ext='xlsx')
    elif system == "pdf":
        files = LoadFiles.objects.filter(file_ext='pdf')

    elif system == "Oficial":
        files = LoadFiles.objects.filter(autority='Oficial')
    elif system == "Comunidad":
        files = LoadFiles.objects.filter(autority='Comunidad')
    elif system == "Privado":
        files = LoadFiles.objects.filter(autority='Privado')

    elif system == "Ciencia":
        files = LoadFiles.objects.filter(category='Ciencia')
    elif system == "Comercio":
        files = LoadFiles.objects.filter(category='Comercio')
    elif system == "Cultura":
        files = LoadFiles.objects.filter(category='Cultura')
    elif system == "Educacion":
        files = LoadFiles.objects.filter(category='Educacion')
    elif system == "Medicina":
        files = LoadFiles.objects.filter(category='Medicina')

    elif system == "Nacional":
        files = LoadFiles.objects.filter(territory='Nacional')
    elif system == "Departamento":
        files = LoadFiles.objects.filter(territory='Departamento')
    elif system == "Municipio":
        files = LoadFiles.objects.filter(territory='Municipio')
    elif system == "Pueblo":
        files = LoadFiles.objects.filter(territory='Pueblo')
    elif system == "Zona":
        files = LoadFiles.objects.filter(territory='Zona')
    elif system == "Barrio":
        files = LoadFiles.objects.filter(territory='Barrio')
    
    fileCount = files.count()
   
    context={"title": "Search Files", "banner":"Search Files in DataBase", 'files':files, 'fileCount':fileCount, 'system':system}
    return render(request, 'loads/searchFiles.html', context)

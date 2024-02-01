import os
import json
import openpyxl
import re
import pandas as pd
from datetime import date
from django.conf import settings
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, redirect
from .models import LoadFiles, DataSet, SheetFile
from .forms import loadFileForm, DataSetForm, SheetFileForm
from .utilities import fileList, singleList, newFolder
from senadlake.dbases import extensions

today = date.today()
validExt, validExtPro = extensions()
origen_path = "/home/gabriel/Downloads/"
filepath = os.path.join(settings.BASE_DIR, "FILES/Raw/")


def loadFile(request):
    if request.method == 'POST':
        form = loadFileForm(request.POST, request.FILES)
        if form.is_valid():
            pform = form.save(commit=False)
            inputFile = request.FILES['inputFile']
            namefile = inputFile.name
            filenamex = namefile.split('.')

            entity = request.POST['entity']
            description = request.POST['description']
            quality = request.POST['quality']
            autority = request.POST['autority']
            category = request.POST['category']
            territory = request.POST['territory']

            date_now = today.strftime("%Y_%B_%d")

            if filenamex[-1] == 'csv':
                df = pd.read_csv(inputFile, low_memory=False)
                lastFilepath = filepath + "/" + quality + "/" +  entity + "/" +  date_now + "/"
                endDir = newFolder(lastFilepath)
                jsonFile = df.to_json(endDir + filenamex[0] + ".json.gz", indent=4, orient='records', compression='gzip', force_ascii=False)
                pform.jsonFile = namefile
                pform.file_ext = filenamex[-1]
                pform.file_name = namefile
                pform.file_numcols = df.shape[1] #- To count columns
                pform.file_numrows = df.shape[0] #- To count rows
                pform.data_set = False
                pform.file_link = endDir + filenamex[0] + ".json.gz"
                pform.file_columns = df.columns.tolist()
                pform.save()
                messages.success(request, "The file was saved successfully")

                return redirect("allFiles")

            elif filenamex[-1] == 'xlsx':
                df = pd.ExcelFile(inputFile)
                filesSaved = []
                count = 0

                dsetform = DataSetForm()
                dsetform = dsetform.save(commit=False)
                sheetform = SheetFileForm()
                sheetform = sheetform.save(commit=False)

                if len(df.sheet_names) > 1:
                    lastFilepath = filepath + "/" + quality + "/" +  entity + "/" +  date_now + "/" + filenamex[0] + "/"
                    endDir = newFolder(lastFilepath)
                    dsetform.set_name = namefile
                    dsetform.data_set = True
                    dsetform.sheet_set = df.sheet_names
                    dsetform.description = description
                    dsetform.entity = entity
                    dsetform.zonas = "Raw"
                    dsetform.quality = request.POST['quality']
                    dsetform.autority = autority
                    dsetform.category = category
                    dsetform.territory = territory
                    dsetform.save()

                    for sheet in df.sheet_names:
                        fullSheet = pd.read_excel(inputFile, sheet_name=sheet)
                        jsonOutput_gz = endDir + filenamex[0] + "_" + sheet + ".json" + ".gz"
                        output = fullSheet.to_json(jsonOutput_gz, indent=4, orient='records', compression='gzip', force_ascii=False)
                        filesSaved.append(jsonOutput_gz)

                    for filesave in filesSaved:
                        cleanString = ""
                        count = count + 1
                        json_data = open(filesave) 
                        jsonFile = pd.read_json(filesave)
                        filenamex = filesave.split('.')
                        filenamey = filenamex[-3].split('/')
                        field = filenamey[-1] + str(count)
                        cleanString = re.sub('\W+','_', field )
                        sheetform.id = cleanString
                        sheetform.sheet_id = count
                        sheetform.sheet_link = filesave
                        sheetform.sheet_name = filenamey[-1]
                        sheetform.main_file = namefile
                        sheetform.sheet_columns = jsonFile.columns.tolist() # List columns names
                        sheetform.sheet_numrows = jsonFile.shape[0] #- count rows
                        sheetform.sheet_numcols = jsonFile.shape[1] #- count columns
                        sheetform.data_set = True
                        sheetform.entity = entity # Company name
                        sheetform.zonas = "Raw"
                        sheetform.save()

                    messages.success(request, "The dataset was saved successfully")
                    return redirect("allFiles")

                else:
                    lastFilepath = filepath + "/" + quality + "/" +  entity + "/" +  date_now + "/"
                    endDir = newFolder(lastFilepath)
                    sheet = df.sheet_names[0]
                    df = pd.read_excel(inputFile)
                    jsonOutput_gz = endDir + filenamex[0] + "_" + sheet + ".json" + ".gz"
                    output = df.to_json(jsonOutput_gz, indent=4, orient='records', compression='gzip', force_ascii=False)
                    pform.jsonFile = namefile
                    pform.file_ext = filenamex[-1]
                    pform.file_name = namefile
                    pform.file_numcols = df.shape[1] #- To count columns
                    pform.file_numrows = df.shape[0] #- To count rows
                    pform.data_set = False
                    pform.file_link = endDir + filenamex[0] + "_" + str(sheet)  + ".json.gz"
                    pform.file_columns = df.columns.tolist()
                    pform.save()
                    messages.success(request, "The file was saved successfully")
                    return redirect("allFiles")

            else:
                extMess = "The file has not a valid extension. Please, verify name and extension and try again."
                messages.warning(request, "The file was NOT saved ** WARNING ** " + extMess)
                return redirect("home")
        else:
            messages.error(request, form.errors)
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


def dataSetDetail(request, pk):
    fileData = DataSet.objects.get(id=pk)
    name = fileData.set_name
    sheets_set = SheetFile.objects.filter(main_file=name)

    context={"title": "Detalle", "banner":"DataSet Detail", 'fileData':fileData, 'sheets_set':sheets_set}
    return render(request, 'loads/dataSetDetail.html', context)


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
    allFiles = []
    allcsv = LoadFiles.objects.all()
    allxls = DataSet.objects.all()

    for all in allcsv:
        allFiles.append(all)

    for all in allxls:
        allFiles.append(all)

    allcount = allcsv.count() + allxls.count()

    # pagination
    paginator = Paginator(allFiles, 5)
    page = request.GET.get('page1')
    try:
        allFiles = paginator.page(page)
    except PageNotAnInteger:
        allFiles = paginator.page(1)
    except EmptyPage:
        allFiles = paginator.page(paginator.num_pages)
    index1 = allFiles.number - 1
    max_index1 = len(paginator.page_range)
    start_index1 = index1 - 3 if index1 >= 3 else 0
    end_index1 = index1 + 3 if index1 <= max_index1 else max_index1
    page_range1 = paginator.page_range[start_index1:end_index1]
    
    context={"title": "All Files", "banner":"DataSets in DataBase"
    , 'allFiles':allFiles, 'allcount':allcount
    , 'page_range1': page_range1

    }
    return render(request, 'loads/allFiles.html', context)


def dscsvOut(request, pk):
    sheet_set = SheetFile.objects.filter(id=pk)

    for sheet in sheet_set:
        data = pd.read_json(sheet.sheet_link)
        csvout = data.to_csv(sheet.sheet_name + ".csv", sep=';', encoding='utf-8')

    return redirect('home')


def setFiles(request):
    csvFiles = LoadFiles.objects.filter(file_ext='csv')
    jsonFiles = LoadFiles.objects.filter(file_ext='json')
    xlsxFiles = LoadFiles.objects.filter(file_ext='xlsx')
    pdfFiles = LoadFiles.objects.filter(file_ext='pdf')

    csvSingles, jsonSingles, xlsxSingles, pdfSingles = singleList(csvFiles, jsonFiles, xlsxFiles, pdfFiles)

    context={"title": "DataSets", "banner":"Single DataSets"
    , 'csvSingles':csvSingles, 'jsonSingles':jsonSingles
    , 'xlsxSingles':xlsxSingles, 'pdfSingles':pdfSingles
    }
    return render(request, 'loads/setFiles.html', context)


def searchFiles(request):
    system = request.POST.get('system', None)

    if system == "Abiertos":
        allFiles = LoadFiles.objects.filter(quality='Abiertos')
    elif system == "Privados":
        allFiles = LoadFiles.objects.filter(quality='Privados')
    elif system == "Clasificados":
        allFiles = LoadFiles.objects.filter(quality='Clasificados')

    elif system == "Oficial":
        allFiles = LoadFiles.objects.filter(autority='Oficial')
    elif system == "Publico":
        allFiles = LoadFiles.objects.filter(autority='Publico')

    elif system == "Ciencia":
        allFiles = LoadFiles.objects.filter(category='Ciencia')
    elif system == "Comercio":
        allFiles = LoadFiles.objects.filter(category='Comercio')
    elif system == "Cultura":
        allFiles = LoadFiles.objects.filter(category='Cultura')
    elif system == "Educacion":
        allFiles = LoadFiles.objects.filter(category='Educacion')
    elif system == "Medicina":
        allFiles = LoadFiles.objects.filter(category='Medicina')

    elif system == "Nacional":
        allFiles = LoadFiles.objects.filter(territory='Nacional')
    elif system == "Departamental":
        allFiles = LoadFiles.objects.filter(territory='Departamento')
    elif system == "Municipal":
        allFiles = LoadFiles.objects.filter(territory='Municipio')
    elif system == "Zonal":
        allFiles = LoadFiles.objects.filter(territory='Zonal')
    elif system == "Barrio":
        allFiles = LoadFiles.objects.filter(territory='Barrio')
    
    allcount = allFiles.count()
    # see error -- https://stackoverflow.com/questions/30384458/django-pagination-local-variable-referenced-before-assignment
    # pagination
    paginator = Paginator(allFiles, 5)
    page = request.GET.get('page1')
    try:
        allFiles = paginator.page(page)
    except PageNotAnInteger:
        allFiles = paginator.page(1)
    except EmptyPage:
        allFiles = paginator.page(paginator.num_pages)
    index1 = allFiles.number - 1
    max_index1 = len(paginator.page_range)
    start_index1 = index1 - 3 if index1 >= 3 else 0
    end_index1 = index1 + 3 if index1 <= max_index1 else max_index1
    page_range1 = paginator.page_range[start_index1:end_index1]

    context={"title": "Search Files", "banner":"Search DataSet in DataBase", 'allFiles':allFiles, 'allcount':allcount, 'page_range1':page_range1}
    return render(request, 'loads/searchFiles.html', context)

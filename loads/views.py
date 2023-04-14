import os
from django.contrib import messages
from django.shortcuts import render, redirect
from .models import LoadFiles
from .forms import loadFileForm
from .utilities import fileList, singleList

origen_path = "/home/gabriel/Downloads/"
destiny_path = "/home/gabriel/prog/cleanCsvFlask/docs/"


def loadFile(request):

    if request.method == 'POST':
        form = loadFileForm(request.POST, request.FILES)

        if form.is_valid():
            pform = form.save(commit=False)
            filex = request.FILES.get('file').name
            extent = filex.split('.')
            ext = extent[-1]
            file_name = extent[0]

            if filex == ext:
                extMess = "The file has no extension. Please, verify name and extension and try again."
                messages.warning(request, "The file was NOT saved" + " ** WARNING ** " + extMess)
                return redirect("home")
            elif ext == 'csv':
                pform.file = request.FILES.get('file')
                pform.file_link = destiny_path
                pform.file_ext = ext
                pform.file_name = file_name
                pform.save()
                messages.success(request, "The file was saved successfully")
                return redirect("home")
            elif ext == 'json':
                pform.file = request.FILES.get('file')
                pform.file_link = destiny_path
                pform.file_ext = ext
                pform.file_name = file_name
                pform.save()
                messages.success(request, "The file was saved successfully")
                return redirect("home")
            elif ext == 'xlsx':
                pform.file = request.FILES.get('file')
                pform.file_link = destiny_path
                pform.file_ext = ext
                pform.file_name = file_name
                pform.save()
                messages.success(request, "The file was saved successfully")
                return redirect("home")
            elif ext == 'pdf':
                pform.file = request.FILES.get('file')
                pform.file_link = destiny_path
                pform.file_ext = ext
                pform.file_name = file_name
                pform.save()
                messages.success(request, "The file was saved successfully")
                return redirect("home")

        else:
            messages.error(request + "Something went wrong. " + form.errors)
            return redirect("home")

    else:
        form = loadFileForm()

    context={"title": "Load Files", "banner":"Load Files To Data Lake", 'form':form}
    return render(request, 'loads/loadFile.html', context)


def allFiles(request):
    dataSet = []
    csvSingles = []
    jsonSingles = []
    xlsxSingles = []
    pdfSingles = []

    csvFiles = LoadFiles.objects.filter(file_ext='csv')
    csvcount = csvFiles.count()

    jsonFiles = LoadFiles.objects.filter(file_ext='json')
    jsoncount = jsonFiles.count()

    xlsxFiles = LoadFiles.objects.filter(file_ext='xlsx')
    xlsxcount = xlsxFiles.count()

    pdfFiles = LoadFiles.objects.filter(file_ext='pdf')
    pdfcount = pdfFiles.count()

    total = (csvcount + jsoncount + xlsxcount + pdfcount)

    context={"title": "All Files", "banner":"Files in DataBase"
    , 'csvFiles':csvFiles, 'csvcount':csvcount
    , 'jsonFiles':jsonFiles, 'jsoncount':jsoncount
    , 'xlsxFiles':xlsxFiles, 'xlsxcount':xlsxcount
    , 'pdfFiles':pdfFiles, 'pdfcount':pdfcount
    , 'total':total
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

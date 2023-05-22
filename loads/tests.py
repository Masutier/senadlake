

    df = pd.ExcelFile(inputFile)

    dsetform = DataSetForm()
    dsetform = dsetform.save(commit=False)
    sheetform = SheetFileForm()
    sheetform = sheetform.save(commit=False)

    if len(df.sheet_names) > 1:

        lastFilepath = filepath + "/" + quality + "/" +  entity + "/" +  date_now + "/" + filenamex[0] + "/"
        endDir = newFolder(lastFilepath)
        sheets = []

        for sheet in df.sheet_names:

            fullSheet = pd.read_excel(inputFile, sheet_name=sheet)
            print(fullSheet.id)
            sheetform.sheet_link = endDir + filenamex[0] + "_" + str(sheet)  + ".json.gz"
            sheetform.sheet_name = sheet
            sheetform.main_file = inputFile
            sheetform.sheet_columns = fullSheet.columns.tolist() # List columns names
            sheetform.sheet_numrows = fullSheet.shape[0] #- count rows
            sheetform.sheet_numcols = fullSheet.shape[1] #- count columns
            sheetform.data_set = True
            sheetform.entity = entity # Company name
            sheetform.zonas = "Raw"
            sheetform.save()

            jsonOutput_gz = endDir + filenamex[0] + "_" + sheet + ".json" + ".gz"
            output = fullSheet.to_json(jsonOutput_gz, indent=4, orient='records', compression='gzip', force_ascii=False)


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

        messages.success(request, "The dataset was saved successfully")
        return redirect("allFiles")


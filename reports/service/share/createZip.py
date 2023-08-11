import zipfile
import io

def createZip(filesOfTheZip):
    buffer = io.BytesIO()
    with zipfile.ZipFile(buffer,'w',zipfile.ZIP_DEFLATED) as zipFile:
        for i,file in enumerate(filesOfTheZip,start=1):
            nameFile = file.get('Content-Disposition').split('filename=')[1]
            content = file.content 
            zipFile.writestr(nameFile,content)
    return buffer.getvalue()
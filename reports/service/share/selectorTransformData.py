from dbfread import DBF
import tempfile
from ..sales.formatterSales import formatterDataSales
from ..coeditions.formaterCoeditions import formaterDataCoeditions

def selectorTransformData(file):
    dataClassified = {
        "sales":[],
        "coeditions":[]  
    }

    #se elige a donde mandar los datos
    with tempfile.NamedTemporaryFile(delete=False) as fileTemporary:
        fileTemporary.write(file.read())

        with DBF(fileTemporary.name,encoding='cp850') as dictData:
            for record in dictData:
                if (int(record["TIPO_CORTE"]) == 1):
                    dataAlreadyExists = dataClassified["sales"]
                    dataClassified["sales"] = [
                        *dataAlreadyExists,
                        record
                    ]
                if (int(record["TIPO_CORTE"])== 2):
                    dataAlreadyExists = dataClassified["coeditions"]
                    dataClassified["coeditions"] = [
                        *dataAlreadyExists,
                        record
                    ]

    dataFormattedSale = formatterDataSales(dataClassified["sales"])
    dataFormattedCoeditions = formaterDataCoeditions(dataClassified["coeditions"])

    if len(dataFormattedSale.keys()) > 0 :
        return {
            "sales":dataFormattedSale,
            "type":"sales"
        }
    if len(dataFormattedCoeditions.keys()) > 0 :
        return {
            "coeditions":dataFormattedCoeditions,
            "type":"coeditions"
        }
    # retorna los datos segun el formater usado

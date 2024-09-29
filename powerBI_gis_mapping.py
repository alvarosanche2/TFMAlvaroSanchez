import pandas as pd

barrios_madrid = {
    "ACACIAS": (40.4017, -3.7056),
    "ADELFAS": (40.3965, -3.6765),
    "ALMAGRO": (40.4338, -3.6945),
    "ALMENARA": (40.4719, -3.6923),
    "ARAPILES": (40.4353, -3.7074),
    "ARGÜELLES": (40.4285, -3.7175),
    "ATALAYA": (40.4081, -3.6745),
    "ATOCHA": (40.4068, -3.6904),
    "BELLAS VISTAS": (40.4482, -3.7078),
    "BERRUGUETE": (40.4626, -3.7083),
    "CARMENES": (40.3969, -3.7245),
    "CASA DE CAMPO": (40.4180, -3.7513),
    "CASTELLANA": (40.4516, -3.6888),
    "CASTILLA": (40.4706, -3.6876),
    "CASTILLEJOS": (40.4570, -3.6955),
    "CHOPERA": (40.3952, -3.6931),
    "CIUDAD JARDIN": (40.4462, -3.6697),
    "CIUDAD UNIVERSITARIA": (40.4472, -3.7296),
    "COLINA": (40.4491, -3.6593),
    "CONCEPCION": (40.4361, -3.6543),
    "CORTES": (40.4145, -3.6995),
    "CUATRO CAMINOS": (40.4477, -3.7035),
    "DELICIAS": (40.3986, -3.6909),
    "EL PILAR": (40.4786, -3.7070),
    "EL VISO": (40.4466, -3.6837),
    "EMBAJADORES": (40.4057, -3.7067),
    "ESTRELLA": (40.4143, -3.6631),
    "FUENTE DEL BERRO": (40.4261, -3.6621),
    "GAZTAMBIDE": (40.4330, -3.7160),
    "GOYA": (40.4277, -3.6765),
    "GUINDALERA": (40.4312, -3.6724),
    "HISPANOAMERICA": (40.4580, -3.6773),
    "IBIZA": (40.4201, -3.6760),
    "IMPERIAL": (40.4052, -3.7111),
    "JERONIMOS": (40.4152, -3.6820),
    "JUSTICIA": (40.4230, -3.6972),
    "LA PAZ": (40.4822, -3.7078),
    "LEGAZPI": (40.3906, -3.6935),
    "LISTA": (40.4289, -3.6758),
    "NIÑO JESUS": (40.4147, -3.6667),
    "NUEVA ESPAÑA": (40.4660, -3.6835),
    "PACIFICO": (40.4053, -3.6786),
    "PALACIO": (40.4140, -3.7130),
    "PALOS DE MOGUER": (40.4038, -3.6969),
    "PROSPERIDAD": (40.4415, -3.6719),
    "PUEBLO NUEVO": (40.4301, -3.6458),
    "PUERTA DEL ANGEL": (40.4051, -3.7360),
    "QUINTANA": (40.4311, -3.6545),
    "RECOLETOS": (40.4223, -3.6870),
    "RIOS ROSAS": (40.4457, -3.6941),
    "SAN ISIDRO": (40.3914, -3.7300),
    "SAN JUAN BAUTISTA": (40.4498, -3.6489),
    "SAN PASCUAL": (40.4400, -3.6557),
    "SOL": (40.4167, -3.7038),
    "TRAFALGAR": (40.4302, -3.7034),
    "UNIVERSIDAD": (40.4280, -3.7066),
    "VALDEACEDERAS": (40.4679, -3.6958),
    "VALDEZARZA": (40.4606, -3.7179),
    "VALLEHERMOSO": (40.4407, -3.7132),
    "VENTAS": (40.4312, -3.6640)
}

latitudes = []
longitudes = []

for barrio in dataset['barrio']:
    lat, lon = barrios_madrid.get(barrio, (None, None))
    latitudes.append(lat)
    longitudes.append(lon)

dataset['Latitud'] = latitudes
dataset['Longitud'] = longitudes
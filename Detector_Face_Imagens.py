# Exemplo de código Python usando o SDK do Azure para detectar rostos em uma imagem

from azure.cognitiveservices.vision.face import FaceClient
from msrest.authentication import CognitiveServicesCredentials

# Configuração da chave e endpoint do serviço
KEY = 'sua_chave_de_acesso'
ENDPOINT = 'seu_endpoint'

# Criação do cliente
face_client = FaceClient(ENDPOINT, CognitiveServicesCredentials(KEY))

# Detecção de rostos em uma imagem
image_url = 'URL_da_imagem'
detected_faces = face_client.face.detect_with_url(image_url)
for face in detected_faces:
    print(face.as_dict())

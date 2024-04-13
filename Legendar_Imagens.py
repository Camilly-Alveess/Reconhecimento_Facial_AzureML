# Exemplo de código Python usando o SDK do Azure para gerar legendas para uma imagem

from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import VisualFeatureTypes

# Configuração da chave e endpoint do serviço
KEY = 'sua_chave_de_acesso'
ENDPOINT = 'seu_endpoint'

# Criação do cliente
computervision_client = ComputerVisionClient(ENDPOINT, CognitiveServicesCredentials(KEY))

# Geração de legendas para uma imagem
image_url = 'URL_da_imagem'
image_caption = computervision_client.describe_image(image_url)
print(image_caption.captions[0].text)

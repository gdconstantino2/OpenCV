import xml.etree.ElementTree as ET

# Criar a estrutura do XML no formato Haar Cascade
root = ET.Element("opencv_storage")
cascade = ET.SubElement(root, "cascade")
size = ET.SubElement(cascade, "size", width="24", height="24")  # Exemplo de tamanho fixo (ajustar conforme necessário)

# Adicionar imagens e porcentagem de azul
images_node = ET.SubElement(cascade, "images")

dados_imagens = [
    {"nome": "aquamarine.jpg", "porcentagem_azul": "67.37"},
    {"nome": "Bebe.jpg", "porcentagem_azul": "76.53"},
    {"nome": "capri.jpg", "porcentagem_azul": "76.69"},
    {"nome": "caribe.jpg", "porcentagem_azul": "70.61"},
    {"nome": "Celeste.jpg", "porcentagem_azul": "64.23"},
    {"nome": "cobalto.jpg", "porcentagem_azul": "76.6"},
    {"nome": "grisalho.jpg", "porcentagem_azul": "76.33"},
    {"nome": "indigo.jpg", "porcentagem_azul": "72.01"},
    {"nome": "inverno.jpg", "porcentagem_azul": "77.03"},
    {"nome": "majestic.jpg", "porcentagem_azul": "62.87"},
    {"nome": "marinho.jpg", "porcentagem_azul": "73.21"},
    {"nome": "medio.jpg", "porcentagem_azul": "76.4"},
    {"nome": "mediterraneo.jpg", "porcentagem_azul": "76.13"},
    {"nome": "oxford.jpg", "porcentagem_azul": "67.99"},
    {"nome": "porcelana.jpg", "porcentagem_azul": "73.54"},
    {"nome": "profundo.jpg", "porcentagem_azul": "72.92"},
    {"nome": "royal.jpg", "porcentagem_azul": "77.03"},
    {"nome": "t_claro.jpg", "porcentagem_azul": "73.96"},
    {"nome": "turquesa.jpg", "porcentagem_azul": "77.17"},
]

# Adicionar cada imagem e sua porcentagem de azul
for dados in dados_imagens:
    imagem = ET.SubElement(images_node, "image", nome=dados["nome"])
    ET.SubElement(imagem, "porcentagem_azul").text = dados["porcentagem_azul"]

# Salvar o arquivo XML
tree = ET.ElementTree(root)
tree.write("dados.xml", encoding="utf-8", xml_declaration=True)

print("XML criado com sucesso!")

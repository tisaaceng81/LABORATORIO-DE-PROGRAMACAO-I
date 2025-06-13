import random
from flask import Flask, jsonify

# Criamos uma instância do nosso servidor web
app = Flask(__name__)

# A mesma função que tínhamos antes, agora em sintaxe Python
def gerar_links_de_exemplo(quantidade):
    links = []
    for i in range(1, quantidade + 1):
        link_data = {
            'name': f'Site Exemplo {i}',
            'rating': round(random.uniform(1.0, 5.0), 1),
            'rank': i,
            'criteria': {
                'performance': round(random.uniform(0.0, 5.0), 1),
                'design': round(random.uniform(0.0, 5.0), 1),
                'usability': round(random.uniform(0.0, 5.0), 1),
                'security': round(random.uniform(0.0, 5.0), 1),
                'seo': round(random.uniform(0.0, 5.0), 1)
            }
        }
        links.append(link_data)
    return links

# Criamos uma "rota" ou "endpoint" na nossa API.
# Quando alguém acessar /api/links, esta função será executada.
@app.route('/api/links')
def obter_links():
    # Geramos os dados
    dados_dos_links = gerar_links_de_exemplo(10)
    # Retornamos os dados em formato JSON
    return jsonify(dados_dos_links)

# Linha para rodar o servidor (para teste)
if __name__ == '__main__':
    # host='0.0.0.0' permite que outros dispositivos na rede acessem
    app.run(debug=True, host='0.0.0.0', port=5000)


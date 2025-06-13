import random
from flask import Flask, jsonify

aplicacao = Flask(__name__)

def gerar_links_aleatorios(quantidade):
    lista_de_links = []
    for i in range(1, quantidade + 1):
        dados_do_link = {
            'nome': f'Site Aleatório {i}',
            'avaliacao': round(random.uniform(1.0, 5.0), 1),
            'classificacao': i,
            'criterios': {
                'desempenho': round(random.uniform(0.0, 5.0), 1),
                'design': round(random.uniform(0.0, 5.0), 1),
                'usabilidade': round(random.uniform(0.0, 5.0), 1),
                'seguranca': round(random.uniform(0.0, 5.0), 1),
                'seo': round(random.uniform(0.0, 5.0), 1)
            }
        }
        lista_de_links.append(dados_do_link)
    return lista_de_links

@aplicacao.route('/api/links')
def obter_links_aleatorios():
    dados_aleatorios = gerar_links_aleatorios(10)
    return jsonify(dados_aleatorios)

if __name__ == '__main__':
    aplicacao.run(host='0.0.0.0', port=5000, debug=True)

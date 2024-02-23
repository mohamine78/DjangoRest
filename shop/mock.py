import requests
 
# l'ecoscore est stocké dans une constante et sera réutilisé dans nos tests
ECOSCORE_GRADE = 'd'
 
def mock_openfoodfact_success(self, method, url):
    # Notre mock doit avoir la même signature que la méthode à mocker
    # À savoir les paramètres d'entrée et le type de sortie
    def monkey_json():
    # Nous créons une méthode qui servira à monkey patcher response.json()
        return {
            'product': {
            'ecoscore_grade': ECOSCORE_GRADE
            }
        }
 
    response = requests.Response()
    response.status_code = 200
    response.json = monkey_json
    return response
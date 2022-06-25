import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt # Retira as restrições de csrf

# Comando para execução nem um terminal Bash
# curl -X '<HTTP_METHOD>' -d '<JSON_BODY>' http://127.0.0.1:8000/alunos_<http_method>/ && printf '\n'

# Dicionários python se assemelham a um hashmap
usuarios = {
    1:{'Nome': 'Guilherme', 'Email': 'Guilherme@gmail.com'},
    2:{'Nome': 'Caio', 'Email': 'Caio@gmail.com'},
    3:{'Nome': 'Fabio', 'Email': 'Fabio@gmail.com'},
    4:{'Nome': 'Camila', 'Email': 'Camila@gmail.com'}
}


# Create your views here.
# curl -X 'GET' http://127.0.0.1:8000/alunos_get/1 && printf '\n'
# Retorna todos os usuários
@csrf_exempt
def alunos_get(request, id):
    if request.method == 'GET':
        return JsonResponse({'Metodo': 'GET', 'Usuario_requisitado': usuarios[id], 'Usuarios': usuarios})

# curl -X 'POST' -d '{"Nome": "Maria", "Email": "Maria@gmail.com", "Id": 5}' http://127.0.0.1:8000/alunos_post/ && printf '\n'
# Adiciona um usuário
@csrf_exempt
def alunos_post(request):
    if request.method == 'POST':
        req_obj = json.loads(request.body)
        usuarios[req_obj['Id']] = {'Nome': req_obj['Nome'], 'Email': req_obj['Email']}

        return JsonResponse({'Metodo': 'POST', 'Id':  req_obj['Id'], 'Requisicao': req_obj, 'Usuarios': usuarios})

# curl -X 'PUT' -d '{"Nome": "Antonio", "Email": "Antonio@gmail.com", "Id":1}' http://127.0.0.1:8000/alunos_put/ && printf '\n'
# Modifica com completo uma entrada (usuário)
@csrf_exempt
def alunos_put(request):
    if request.method == 'PUT':
        req_obj = json.loads(request.body)
        usuarios[req_obj['Id']] = {'Nome': req_obj['Nome'], 'Email': req_obj['Email']}

        return JsonResponse({'Metodo': 'PUT', 'Id': req_obj['Id'], 'Requisicao': json.loads(request.body), 'Usuarios': usuarios})

# curl -X 'PATCH' -d '{"Nome": "Antonio da Silva", "Id":1}' http://127.0.0.1:8000/alunos_patch/ && printf '\n'
# Modifica parte de uma entrada
@csrf_exempt
def alunos_patch(request):
    if request.method == 'PATCH':
        req_obj = json.loads(request.body)
        usuarios[req_obj['Id']]['Nome'] = req_obj['Nome']

        return JsonResponse({'Metodo': 'PATCH', 'Id':req_obj['Id'], 'Requisicao': json.loads(request.body), 'Usuarios': usuarios})

# curl -X 'DELETE' -d '{"Id":5}' http://127.0.0.1:8000/alunos_delete/ && printf '\n'
# Deleta uma entrada
@csrf_exempt
def alunos_delete(request):
    if request.method == 'DELETE':
        req_obj = json.loads(request.body)
        usuarios.pop(req_obj['Id'])

        return JsonResponse({'Metodo': 'DELETE', 'Id': req_obj['Id'], 'Requisicao': json.loads(request.body), 'Usuarios': usuarios})
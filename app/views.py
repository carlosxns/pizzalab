from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Nosso "banco de dados" estático
pizzas_db = [
    {'id': 1, 'nome': 'Margherita', 'ingredientes': ['Tomate', 'Mussarela', 'Manjericão']},
    {'id': 2, 'nome': 'Pepperoni', 'ingredientes': ['Pepperoni', 'Queijo']},
    {'id': 3, 'nome': 'Vegetariana', 'ingredientes': ['Tomate', 'Mussarela', 'Cogumelos', 'Espinafre']}
]

@csrf_exempt
def gerenciar_pizzas(request):
    if request.method == 'GET':
        return JsonResponse(pizzas_db, safe=False)
    
    elif request.method == 'POST':
        return JsonResponse({'mensagem': 'Sucesso! Nova pizza adicionada ao cardápio.'}, status=201)

@csrf_exempt
def gerenciar_pizza_id(request, id):
    if request.method == 'GET':
        pizza = next((p for p in pizzas_db if p['id'] == id), None)
        if pizza:
            return JsonResponse(pizza)
        return JsonResponse({'erro': 'Pizza não encontrada.'}, status=404)
        
    elif request.method == 'PUT':
        return JsonResponse({'mensagem': f'Sucesso! Pizza de ID {id} foi atualizada.'})
        
    elif request.method == 'DELETE':
        return JsonResponse({'mensagem': f'Sucesso! Pizza de ID {id} foi removida.'})
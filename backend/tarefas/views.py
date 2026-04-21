from django.http import JsonResponse
from .models import Tarefa

def listar_tarefas(request):
    tarefas = Tarefa.objects.select_related('usuario_responsavel').all()

    data = []
    for t in tarefas:
        data.append({
            "id": t.id,
            "titulo": t.titulo,
            "descricao": t.descricao,
            "status": t.status,
            "prioridade": t.prioridade,
            "data_criacao": t.data_criacao,
            "data_entrega": t.data_entrega,
            "usuario_responsavel": t.usuario_responsavel.nome if t.usuario_responsavel else None
        })

    return JsonResponse(data, safe=False)


def listar_tarefas_abertas(request):
    tarefas = Tarefa.objects.select_related('usuario_responsavel').filter(status='ABERTA')

    data = []
    for t in tarefas:
        data.append({
            "id": t.id,
            "titulo": t.titulo,
            "descricao": t.descricao,
            "status": t.status,
            "prioridade": t.prioridade,
            "data_criacao": t.data_criacao,
            "data_entrega": t.data_entrega,
            "usuario_responsavel": t.usuario_responsavel.nome if t.usuario_responsavel else None
        })

    return JsonResponse(data, safe=False)
# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.db import connection


# Create your views here.

def index(request):
    return render(request, 'index.html')


def retorna_dados_painel(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM TB_MES")
        tb_mes = cursor.fetchall()      

        cursor.execute("SELECT * FROM TB_AREA")
        tb_area = cursor.fetchall()

        cursor.execute("SELECT * FROM TB_MARCA")
        tb_marca = cursor.fetchall()        

    dados_json = {}
    dados_json['marca'] = []
    dados_json['area'] = []
    dados_json['mes'] = []

    for mes in tb_mes:
        dados_mes = {}
        dados_mes['MesAno'] = mes[0]
        dados_mes['ValorTotalFaturado'] = mes[1]
        dados_mes['MargemFaturado'] = mes[2]
        dados_mes['ValorTotalCarteira'] = mes[3]
        dados_mes['MargemCarteira'] = mes[4]
        dados_mes['ValorTotal_FAT_CAR'] = mes[5]
        dados_mes['Margem_FAT_CAR'] = mes[6]
        dados_mes['QuantidadeOrcamento'] = mes[7]
        dados_mes['ValorTotalOrcamento'] = mes[8]
        dados_mes['PrecoMedioOrcamento'] = mes[9]
        dados_mes['MargemOrcamento'] = mes[10]
        dados_mes['ValorTotalRealizar'] = mes[11]

        dados_json['mes'].append(dados_mes)

    for area in tb_area:
        dados_area = {}
        dados_area['AreaNome'] = area[0]
        dados_area['ValorTotalFaturado'] = area[1]
        dados_area['MargemFaturado'] = area[2]
        dados_area['ValorTotalCarteira'] = area[3]
        dados_area['MargemCarteira'] = area[4]
        dados_area['ValorTotal_FAT_CAR'] = area[5]
        dados_area['Margem_FAT_CAR'] = area[6]
        dados_area['ValorTotalOrcamento'] = area[7]
        dados_area['MargemOrcamento'] = area[8]
        dados_area['ValorTotalRealizar'] = area[9]

        dados_json['area'].append(dados_area)            

    for marca in tb_marca:
        dados_marca = {}
        dados_marca['Marca'] = marca[0]
        dados_marca['ValorTotalFaturado'] = marca[1]
        dados_marca['MargemFaturado'] = marca[2]
        dados_marca['ValorTotalCarteira'] = marca[3]
        dados_marca['MargemCarteira'] = marca[4]
        dados_marca['ValorTotal_FAT_CAR'] = marca[5]
        dados_marca['Margem_FAT_CAR'] = marca[6]
        dados_marca['ValorTotalOrcamento'] = marca[7]
        dados_marca['MargemOrcamento'] = marca[8]
        dados_marca['ValorTotalRealizar'] = marca[9]

        dados_json['marca'].append(dados_marca)

    return JsonResponse(dados_json)
    
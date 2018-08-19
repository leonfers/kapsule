"""kpsule URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from core.views import *
from django.urls import path
from django.contrib.auth import views
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Index, name='home'),
    path('projetos/<int:usuario_id>', Projetos, name='projetos'),
    path('dashboard/<int:projeto_id>', Dashboard, name='dashboard'),
    path('changeStatus/<int:capsula_id>', ChangeStatus, name='change-status'),
    path('deleteCapsula/<int:capsula_id>', DeleteCapsule, name='delete-capsula'),
    path('deleteSubproduto/<int:subproduto_id>', DeleteSubProduto, name='delete-subproduto'),
    path('deleteRecurso/<int:recurso_id>', DeleteRecurso, name='delete-recurso'),
    path('novo_projeto/<int:usuario_id>',RegistrarProjeto.as_view(), name="novo_projeto"),
    path('novo_subproduto/', SubprodutoCreateView.as_view(), name='novo_subproduto'),
    path('novo_kpsule/', RegistrarKpsule.as_view(), name='novo_kpsule'),
    path('novo_recurso/', RegistrarRecurso.as_view(), name='novo_recurso'),
]


from django.shortcuts import render
from rest_framework.renderers import JSONRenderer
from rest_framework import viewsets
from .models import *
from .serializers import *
from .grafos import *

from rest_framework import views
from rest_framework.response import Response
import base64

class PaisView(viewsets.ReadOnlyModelViewSet):

    renderer_classes = [JSONRenderer]
    queryset = Pais.objects.all()
    serializer_class = PaisSerializer
    #permission_classes = [permissions.IsAuthenticated,]

class UniversidadView(viewsets.ReadOnlyModelViewSet):
    renderer_classes = [JSONRenderer]
    queryset = Universidad.objects.all()
    serializer_class = UniversidadSerializer

class InstitucionView(viewsets.ReadOnlyModelViewSet):
    renderer_classes = [JSONRenderer]
    queryset = Institucion.objects.all()
    serializer_class = InstitucionSerializer

class PlanEstudioView(viewsets.ReadOnlyModelViewSet):
    renderer_classes = [JSONRenderer]
    queryset = PlanEstudio.objects.all()
    serializer_class = PlanEstudioSerializer

class GuiaView(viewsets.ReadOnlyModelViewSet):
    renderer_classes = [JSONRenderer]
    queryset = Guia.objects.all()
    serializer_class = GuiaSerializer


class NodoCursoView(viewsets.ReadOnlyModelViewSet):
    renderer_classes = [JSONRenderer]
    queryset = NodoCurso.objects.all()
    serializer_class = NodoCursoSerializer

class EnlaceCursoView(viewsets.ReadOnlyModelViewSet):
    renderer_classes = [JSONRenderer]
    queryset = EnlaceCurso.objects.all()
    serializer_class = EnlaceCursoSerializer

class NodoModCursoView(viewsets.ReadOnlyModelViewSet):
    renderer_classes = [JSONRenderer]
    queryset = NodoModCurso.objects.all()
    serializer_class = NodoModCursoSerializer

class EnlaceModCursoView(viewsets.ReadOnlyModelViewSet):
    renderer_classes = [JSONRenderer]
    queryset = EnlaceModCurso.objects.all()
    serializer_class = EnlaceModCursoSerializer

class ComparaGraphView(views.APIView):
    
    def get(self, request, guia=0, plan=0):

        #guia = self.request.query_params.get('guia')
        #plan = self.request.query_params.get('plan')

        #if len(guia) > 0: guia = int(guia)
        #if len(plan) > 0: plan = int(plan)

        if (guia != 0 and plan != 0):
            # Crear grafo G y serializar
            G = factory_graph_guia(guia)
            x = nodos=len(G.nodes)
            y = enlaces=len(G.edges)
            grafoG = Grafo(x,y)
            grafoG_S = GrafoSerializer(grafoG)
            # Crear grafo H y serializar
            H = factory_graph_plan(plan)
            x = nodos=len(H.nodes)
            y = enlaces=len(H.edges)
            grafoH = Grafo(x,y)
            grafoH_S = GrafoSerializer(grafoH)
            # obtener comparacion
            MCS = getMCS(G,H)
            x = nodos=len(MCS.nodes)
            y = enlaces=len(MCS.edges)
            grafoMCS = Grafo(x,y)
            grafoMCS_S = GrafoSerializer(grafoMCS)

            ged = distance(len(MCS.nodes),len(G.nodes), len(H.nodes))

            image = draw_mix_graph(H, plan, MCS, G)

            image_s = base64.b64encode(image.getvalue()).decode()

            #data = ComparaGraph(grafoG, grafoH, MCS, ged, s_image)
            data = ComparaGraph(grafoG, grafoH, grafoMCS, ged, image_s)
            
        results = ComparaGraphSerializer(data, many=False).data

        return Response(results)




    



import unittest
from ..models import Historia
from django.test import Client
import json
import os

class registroHistoria(unittest.TestCase):
    
    def tearDown(self):
        Historia.objects.all().delete()

    def setUp(self):
        self.client = Client()
        self.url = '/api/v1/historias'
        file_path = os.path.join(os.path.dirname(__file__), './response/historia.json')
        self.assert_data = json.loads(open(file_path, encoding='utf-8').read())

    def test_registro_historia(self):
        response = self.client.post(self.url, self.assert_data)
        self.assertEqual(response.status_code, 201)
        
    def test_codigo_longitud(self):
        self.tearDown()
        Historia.objects.create(id=1, codigo='2222', fecha='2023-11-08', nombre_especialista='cristian torres', diagnostico='Prueba', procedimiento='Prueba',tratamiento='Prueba', paciente_id=6)
        self.assert_data['codigo']="22222"
        response=self.client.post(self.url, self.assert_data)
        self.assertEqual(response.status_code, 400)
        
    def test_codigo_campo_obligatorio(self):
        self.tearDown()
        Historia.objects.create(id=1, codigo='2222', fecha='2023-11-08', nombre_especialista='cristian torres', diagnostico='Prueba', procedimiento='Prueba',tratamiento='Prueba', paciente_id=6)
        self.assert_data['codigo']=""
        response=self.client.post(self.url, self.assert_data)
        self.assertEqual(response.status_code, 400)
    
    def test_nombre_especialista_longitud(self):
        self.tearDown()
        Historia.objects.create(id=1, codigo='2222', fecha='2023-11-08', nombre_especialista='cristian torres', diagnostico='Prueba', procedimiento='Prueba',tratamiento='Prueba', paciente_id=6)
        self.assert_data['nombre_especialista'] = "longitud de texto mayor a 20 caracteres"
        response = self.client.post(self.url, self.assert_data)
        self.assertEqual(response.status_code, 400)
    
    def test_campo_obligatorio_nombre_especialista(self):
        self.tearDown()
        Historia.objects.create(id=1, codigo='2222', fecha='2023-11-08', nombre_especialista='cristian torres', diagnostico='Prueba', procedimiento='Prueba',tratamiento='Prueba', paciente_id=6)
        self.assert_data['nombre_especialista'] = ""
        response = self.client.post(self.url, self.assert_data)
        self.assertEqual(response.status_code, 400)
        
    def test_nombre_especialista_solo_caracteres(self):
        self.tearDown()
        Historia.objects.create(id=1, codigo='2222', fecha='2023-11-08', nombre_especialista='cristian torres', diagnostico='Prueba', procedimiento='Prueba',tratamiento='Prueba', paciente_id=6)
        self.assert_data['nombre_especialista'] = 15641
        response = self.client.post(self.url, self.assert_data)
        self.assertEqual(response.status_code, 400)

    def test_actualizar_historia(self):
        self.tearDown()
        historia = Historia.objects.create(id=1, codigo='2222', fecha='2023-11-08', nombre_especialista='cristian torres', diagnostico='Prueba', procedimiento='Prueba', tratamiento='Prueba', paciente_id=6)

        datos_actualizados = {
            "codigo":"2222",
            "fecha":"2023-11-08",
            "nombre_especialista": "Maria Liz",
            "diagnostico":"prueba",
            "procedimiento":"prueba",
            "tratamiento":"prueba",
            "paciente_id":6
        }
        response = self.client.put(f"{self.url}/{historia.id}", datos_actualizados, content_type='application/json')
        print(response.content)
        self.assertEqual(response.status_code, 200)
        
    def test_eliminar_historia(self):
        historia = Historia.objects.create(id=1, codigo='2222', fecha='2023-11-08', nombre_especialista='cristian torres', diagnostico='Prueba', procedimiento='Prueba',tratamiento='Prueba', paciente_id=6)
        response = self.client.delete(f"{self.url}/{historia.id}")
        print(response.content)
        self.assertEqual(response.status_code, 200)
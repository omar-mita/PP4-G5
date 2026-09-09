from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from .models import Animal


class AdopcionYReportesTests(TestCase):
    def setUp(self):
        self.usuario = User.objects.create_user(username='sebastian', password='clave123')
        self.otro_usuario = User.objects.create_user(username='otro', password='clave123')
        self.animal = Animal.objects.create(
            nombre='Milo',
            edad=3,
            raza='Mestizo',
            sexo='Macho',
            tamanio='Mediano',
            descripcion='Busca una familia',
            imagen='imagenes/dogs/milo.jpg',
            owner=self.usuario,
        )
        self.client.login(username='sebastian', password='clave123')

    def test_marcar_como_adoptado_registra_fecha_y_oculta_del_inicio(self):
        respuesta = self.client.post(reverse('marcar_adoptado', args=[self.animal.id]))
        self.assertRedirects(respuesta, reverse('mis_publicaciones'))

        self.animal.refresh_from_db()
        self.assertEqual(self.animal.estado, Animal.ESTADO_ADOPTADO)
        self.assertIsNotNone(self.animal.fecha_adopcion)

        respuesta_inicio = self.client.get(reverse('index'))
        self.assertNotContains(respuesta_inicio, 'Milo')

    def test_usuario_no_puede_adoptar_publicacion_ajena(self):
        animal_ajeno = Animal.objects.create(
            nombre='Tina',
            edad=2,
            raza='Mestiza',
            sexo='Hembra',
            tamanio='Chico',
            descripcion='Busca hogar',
            imagen='imagenes/dogs/tina.jpg',
            owner=self.otro_usuario,
        )
        respuesta = self.client.post(reverse('marcar_adoptado', args=[animal_ajeno.id]))
        self.assertEqual(respuesta.status_code, 404)

    def test_baja_registra_fecha(self):
        respuesta = self.client.post(reverse('dar_baja_publicacion', args=[self.animal.id]))
        self.assertRedirects(respuesta, reverse('mis_publicaciones'))

        self.animal.refresh_from_db()
        self.assertEqual(self.animal.estado, Animal.ESTADO_BAJA)
        self.assertIsNotNone(self.animal.fecha_baja)

    def test_reporte_muestra_publicacion_y_adopcion_del_mes(self):
        self.animal.estado = Animal.ESTADO_ADOPTADO
        self.animal.fecha_adopcion = timezone.now()
        self.animal.save(update_fields=['estado', 'fecha_adopcion'])

        respuesta = self.client.get(reverse('reportes'))
        self.assertEqual(respuesta.status_code, 200)
        self.assertContains(respuesta, 'Reportes de AdoptDog')
        self.assertContains(respuesta, 'Milo')
        self.assertEqual(respuesta.context['total_publicaciones'], 1)
        self.assertEqual(respuesta.context['total_adoptados'], 1)
        self.assertTrue(respuesta.context['reporte_mensual'])

from django.test import TestCase, Client
from django.urls import reverse
from groups.models import Group, GroupMember

import misaka

class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.test_group = Group.objects.create(
            name = 'test-group',
            slug = 'testgroup',
            description = 'description',
            description_html =  misaka.html('description')
        )
        self.group_list_url = reverse('groups:all')
        self.group_detail_url = reverse('groups:single', args=['test-group'])
        self.group_creation_url = reverse('groups:create')
        self.group_join_url = reverse('groups:join', args=['test-group'])
        self.group_leave_url = reverse('groups:leave', args=['test-group'])

    def test_group_list_page_GET(self):
        response = self.client.get(self.group_list_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'groups/group_list.html')

    def test_group_detail_page_GET(self):
        response = self.client.get(self.group_detail_url)
      
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'groups/group_detail.html')

    def test_group_creation_page_GET(self):
        response = self.client.get(self.group_detail_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'groups/group_detail.html')

    def test_group_join_page_GET(self):
        response = self.client.get(self.group_join_url)

        self.assertEquals(response.status_code, 302)
        self.assertRedirects(response, '/accounts/login/?next=/groups/join/test-group/')
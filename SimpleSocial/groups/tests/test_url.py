from django.test import SimpleTestCase
from django.urls import reverse, resolve
from django.views import generic
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    PermissionRequiredMixin
)

from groups.views import (
    CreateGroup, SingleGroup,
    ListGroups, JoinGroup, LeaveGroup,

)

class TestUrls(SimpleTestCase):

    def setUp(self):
        self.group_list_url = reverse('groups:all')
        self.group_detail_url = reverse('groups:single', args=['test_slug'])
        self.group_creation_url = reverse('groups:create')
        self.group_join_url = reverse('groups:join', args=['test_slug'])
        self.group_leave_url = reverse('groups:leave', args=['test_slug'])

    def test_group_list_url_resolves(self):
        self.assertEquals(resolve(self.group_list_url).func.view_class, ListGroups)
    
    def test_group_detail_url_resolves(self):
        self.assertEquals(resolve(self.group_detail_url).func.view_class, SingleGroup)
    
    def test_create_group_url_resovles(self):
        self.assertEquals(resolve(self.group_creation_url).func.view_class, CreateGroup)

    def test_join_group_url_resolve(self):
        self.assertEquals(resolve(self.group_join_url).func.view_class, JoinGroup)

    def test_leave_group_url_resolve(self):
        self.assertEquals(resolve(self.group_leave_url).func.view_class, LeaveGroup)
from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard

class ModelTests(TestCase):
    def setUp(self):
        marvel = Team.objects.create(name='Marvel', description='Marvel superheroes')
        dc = Team.objects.create(name='DC', description='DC superheroes')
        user1 = User.objects.create(name='Spider-Man', email='spiderman@marvel.com', team=marvel)
        user2 = User.objects.create(name='Batman', email='batman@dc.com', team=dc)
        Workout.objects.create(name='Cardio', description='Run fast', suggested_for='Marvel')
        Activity.objects.create(user=user1, type='Running', duration=30, date='2025-11-22')
        Leaderboard.objects.create(team=marvel, points=100)

    def test_user_email_unique(self):
        marvel = Team.objects.get(name='Marvel')
        with self.assertRaises(Exception):
            User.objects.create(name='Duplicate', email='spiderman@marvel.com', team=marvel)

    def test_leaderboard_points(self):
        marvel = Team.objects.get(name='Marvel')
        lb = Leaderboard.objects.get(team=marvel)
        self.assertEqual(lb.points, 100)

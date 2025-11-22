from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard
from django.db import transaction

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        with transaction.atomic():
            # Delete all data (delete each object individually to avoid TypeError)
            for model in [Activity, User, Team, Workout, Leaderboard]:
                for obj in model.objects.all():
                    obj.delete()

            # Create teams
            marvel = Team.objects.create(name='Marvel', description='Marvel superheroes')
            dc = Team.objects.create(name='DC', description='DC superheroes')

            # Create users
            users = [
                User.objects.create(name='Spider-Man', email='spiderman@marvel.com', team=marvel),
                User.objects.create(name='Iron Man', email='ironman@marvel.com', team=marvel),
                User.objects.create(name='Captain America', email='cap@marvel.com', team=marvel),
                User.objects.create(name='Batman', email='batman@dc.com', team=dc),
                User.objects.create(name='Superman', email='superman@dc.com', team=dc),
                User.objects.create(name='Wonder Woman', email='wonderwoman@dc.com', team=dc),
            ]

            # Create workouts
            workouts = [
                Workout.objects.create(name='Cardio', description='Run fast', suggested_for='Marvel'),
                Workout.objects.create(name='Strength', description='Lift heavy', suggested_for='DC'),
            ]

            # Create activities
            Activity.objects.create(user=users[0], type='Running', duration=30, date='2025-11-22')
            Activity.objects.create(user=users[3], type='Weightlifting', duration=45, date='2025-11-22')

            # Create leaderboard
            Leaderboard.objects.create(team=marvel, points=150)
            Leaderboard.objects.create(team=dc, points=120)

        self.stdout.write(self.style.SUCCESS('octofit_db populated with test data'))

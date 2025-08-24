from django.core.management.base import BaseCommand
from django.conf import settings
from djongo import models
from pymongo import MongoClient

# Sample data
USERS = [
    {"name": "Iron Man", "email": "ironman@marvel.com", "team": "Marvel"},
    {"name": "Captain America", "email": "cap@marvel.com", "team": "Marvel"},
    {"name": "Spider-Man", "email": "spiderman@marvel.com", "team": "Marvel"},
    {"name": "Superman", "email": "superman@dc.com", "team": "DC"},
    {"name": "Batman", "email": "batman@dc.com", "team": "DC"},
    {"name": "Wonder Woman", "email": "wonderwoman@dc.com", "team": "DC"},
]
TEAMS = [
    {"name": "Marvel", "members": ["Iron Man", "Captain America", "Spider-Man"]},
    {"name": "DC", "members": ["Superman", "Batman", "Wonder Woman"]},
]
ACTIVITIES = [
    {"user": "Iron Man", "activity": "Running", "duration": 30},
    {"user": "Batman", "activity": "Cycling", "duration": 45},
]
LEADERBOARD = [
    {"team": "Marvel", "points": 120},
    {"team": "DC", "points": 110},
]
WORKOUTS = [
    {"name": "Push Ups", "difficulty": "Medium"},
    {"name": "Squats", "difficulty": "Easy"},
]

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        client = MongoClient(host='localhost', port=27017)
        db = client["octofit_db"]
        db.users.delete_many({})
        db.teams.delete_many({})
        db.activities.delete_many({})
        db.leaderboard.delete_many({})
        db.workouts.delete_many({})
        db.users.insert_many(USERS)
        db.teams.insert_many(TEAMS)
        db.activities.insert_many(ACTIVITIES)
        db.leaderboard.insert_many(LEADERBOARD)
        db.workouts.insert_many(WORKOUTS)
        db.users.create_index("email", unique=True)
        self.stdout.write(self.style.SUCCESS('octofit_db populated with test data'))

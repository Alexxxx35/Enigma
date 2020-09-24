from django.db import models

"""
linux shell delete commands
rm -f path/db.sqlite3
rm -f path/migrations/migration_file
windows shell delete commands
del path/db.sqlite3
del path/migrations/migration_file
"""


# Create your models here.
class Mercenaries(models.Model):
    id = models.IntegerField(primary_key=True, default=None)
    first_name = models.CharField(max_length=30, default=None)
    last_name = models.CharField(max_length=30, default=None)
    age = models.IntegerField(default=None)
    gender = models.CharField(max_length=10, default=None)
    cost = models.IntegerField(default=None)
    number_of_actions = models.IntegerField(default=1)

    def __str__(self):
        return self.id + self.first_name + self.last_name + self.age + self.gender + self.cost + self.number_of_actions

    class Meta:
        ordering = ['id']


class Detective(models.Model):
    id = models.IntegerField(primary_key=True, default=1)
    cover = models.CharField(max_length=30, default=None)
    money = models.IntegerField(default=3000)
    number_of_mercenaries = models.ForeignKey(Mercenaries, default=None, on_delete=models.CASCADE)

    def __str__(self):
        return self.id + self.cover + self.money + self.number_of_mercenaries

    class Meta:
        ordering = ['id']


class Quest(models.Model):
    id = models.IntegerField(primary_key=True, default=None)
    title = models.CharField(max_length=30, default=None)

    def __str__(self):
        return self.id + self.title

    class Meta:
        ordering = ['id']


class Victim(models.Model):
    id = models.IntegerField(primary_key=True, default=None)
    first_name = models.CharField(max_length=30, default=None)
    last_name = models.CharField(max_length=30, default=None)
    autopsia = models.CharField(max_length=100, default=None)
    gender = models.CharField(max_length=10, default=None)
    age = models.IntegerField(default=None)
    ethnic_group = models.CharField(max_length=15, default=None)
    height = models.IntegerField(default=None)
    hair_color = models.CharField(max_length=15, default=None)
    eye_color = models.CharField(max_length=15, default=None)
    profession = models.CharField(max_length=30, default=None)
    resident = models.CharField(max_length=30, default=None)
    income = models.IntegerField(default=None)
    insurance_owner = models.BooleanField(default=None)

    def __str__(self):
        return self.id + self.first_name + self.last_name + self.autopsia + self.gender + self.age + self.ethnic_group + self.height + self.hair_color + self.eye_color + self.profession + self.resident + self.income + self.insurance_owner

    class Meta:
        ordering = ["id"]


class Insurance(models.Model):
    id = models.IntegerField(primary_key=True, default=None)
    victim_insurance = models.ForeignKey(Victim, default=None, on_delete=models.CASCADE)
    value = models.IntegerField(default=None)

    def __str__(self):
        return self.value + self.victim_insurance

    class Meta:
        ordering = ['id']


class Suspect(models.Model):
    id = models.IntegerField(primary_key=True, default=None)
    first_name = models.CharField(max_length=30, default=None)
    last_name = models.CharField(max_length=30, default=None)
    gender = models.CharField(max_length=10, default=None)
    age = models.IntegerField(default=None)
    ethnic_group = models.CharField(max_length=15, default=None)
    height = models.IntegerField(default=None)
    hair_color = models.CharField(max_length=15, default=None)
    eye_color = models.CharField(max_length=15, default=None)
    profession = models.CharField(max_length=30, default=None)
    resident = models.CharField(max_length=30, default=None)
    income = models.IntegerField(default=None)
    bound_with_victim = models.ForeignKey(Victim, default=None, on_delete=models.CASCADE)
    danger_level = models.BooleanField(default=None)
    corruption_cost = models.IntegerField(default=None)

    def __str__(self):
        return self.id + self.first_name + ' ' + self.last_name + self.gender + self.age + self.ethnic_group + self.height + self.hair_color + self.eye_color + self.profession + self.resident + self.bound_with_victim + self.danger_level + self.corruption_cost

    class Meta:
        ordering = ['id']


class Prisoners(models.Model):
    id = models.IntegerField(primary_key=True, default=None)
    prisoner_id = models.ForeignKey(Suspect, default=None, on_delete=models.CASCADE)
    # first_name = models.ForeignKey(Suspect.first_name, default=None, on_delete=models.CASCADE)
    # last_name = models.ForeignKey(Suspect.last_name, default=None, on_delete=models.CASCADE)
    # guilty = models.BooleanField(default=None)
    prime_value = models.IntegerField(default=None)

    def __str__(self):
        return self.id + self.prisoner_id + self.prime_value

    class Meta:
        ordering = ['id']


class Killed(models.Model):
    id = models.IntegerField(primary_key=True, default=None)
    murdered_id = models.ForeignKey(Suspect, default=None, on_delete=models.CASCADE)
    # first_name = models.ForeignKey(Suspect.first_name, default=None, on_delete=models.CASCADE)
    # last_name = models.ForeignKey(Suspect.last_name, default=None, on_delete=models.CASCADE)
    # guilty = models.BooleanField(default=None)
    prime_value = models.IntegerField(default=None)

    def __str__(self):
        return self.id + self.murdered_id + self.prime_value

    class Meta:
        ordering = ['id']


#
# class Investigation(models.Model):
#     id = models.IntegerField(primary_key=True, default=None)
#     examination = models.ForeignKey(Suspect, default=None, on_delete=models.CASCADE)
#     Question1 = models.CharField(max_length=500, default=None)
#     Response1 = models.CharField(max_length=500, default=None)
#     Question2 = models.CharField(max_length=500, default=None)
#     Response2 = models.CharField(max_length=500, default=None)
#     Question3 = models.CharField(max_length=500, default=None)
#     Response3 = models.CharField(max_length=500, default=None)
#     Question4 = models.CharField(max_length=500, default=None)
#     Response4 = models.CharField(max_length=500, default=None)
#     Question5 = models.CharField(max_length=500, default=None)
#     Response5 = models.CharField(max_length=500, default=None)
#
#     def __str__(self):
#         return self.id + self.examination
#
#     class Meta:
#         ordering = ['id']


class Record(models.Model):
    id = models.IntegerField(primary_key=True, default=None)
    suspect_id = models.ForeignKey(Suspect, default=None, on_delete=models.CASCADE)
    antecedent = models.CharField(max_length=100, default=None)

    # investigation = models.ForeignKey(Investigation, default=None, on_delete=models.CASCADE)

    def __str__(self):
        return self.id + self.suspect_id + self.antecedent

    class Meta:
        ordering = ['id']


class Crime_details(models.Model):
    id = models.IntegerField(primary_key=True, default=None)
    crime_quest = models.ForeignKey(Quest, default=None, on_delete=models.CASCADE)
    victim_id = models.ForeignKey(Victim, default=None, on_delete=models.CASCADE)
    estimated_date = models.IntegerField(default=None)
    nature = models.CharField(max_length=30, default=None)
    # weapon_used = models.CharField(max_length=30, default=None)
    autopsia = models.CharField(max_length=100, default=None)

    # optional_clues = models.CharField(max_length=100, default=None)

    def __str__(self):
        return self.id + self.crime_id + self.crime_quest + self.victim_id + self.estimated_date + self.nature + self.weapon_used + self.autopsia

    class Meta:
        ordering = ['id']


class Crime_location(models.Model):
    id = models.IntegerField(primary_key=True, default=None)
    crime = models.ForeignKey(Crime_details, default=None, on_delete=models.CASCADE)
    location = models.CharField(max_length=100, default=None)

    def __str__(self):
        return self.id + self.crime + self.location

    class Meta:
        ordering = ['id']


class Clues(models.Model):
    id = models.IntegerField(primary_key=True, default=None)
    clue = models.CharField(max_length=200, default=None)
    crime_clues = models.ForeignKey(Crime_details, default=None, on_delete=models.CASCADE)

    def __str__(self):
        return self.id + self.clue + self.crime_clues

    class Meta:
        ordering = ['id']

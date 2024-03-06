from django.core.management.base import BaseCommand, CommandError
from competition.models import *
import gspread as gs
from gspread_formatting import *
import os
from random import *
import time

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = '/Users/milkamilicevic/Projects/sherlook/competition/management/commands/service_account.json'
SERVICE_ACCOUNT_CREDENTIALS = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")


class Command(BaseCommand):

    def handle(self, *args, **options):
        sa = gs.service_account(filename=SERVICE_ACCOUNT_CREDENTIALS)
        sh = sa.open('Search Engine v0.1')
        wks = sh.worksheet('Studenti3')
        j = 0
        for i in range(1202, 1300):
            print(i)
            print("j"+ str(j))
            if j < 2:
                j= j +1
            else:
                j = 0
                time.sleep(60)
            first_name = wks.cell(i, 2).value
            last_name = wks.cell(i, 3).value
            university = wks.cell(i, 17).value
            study = wks.cell(i, 8).value # position
            #date_of_birth = models.DateField(blank=True, null=True)
            age = wks.cell(i, 5).value
            if age=="" or age=="/":
                age = None
            email = wks.cell(i, 6).value
            mobile_phone_number = wks.cell(i, 7).value
            country = wks.cell(i, 18).value
            position = wks.cell(i, 8).value
            level = wks.cell(i, 9).value
            estimate_year_of_graduation = wks.cell(i, 10).value
            if estimate_year_of_graduation=="" or estimate_year_of_graduation=="/":
                estimate_year_of_graduation = None
            specialisation = wks.cell(i, 13).value # role in the team
            experience = wks.cell(i, 11).value
            role_bonus = wks.cell(i, 12).value
            driver = wks.cell(i, 14).value
            eso = wks.cell(i, 15).value
            role_at_competition = wks.cell(i, 16).value
            category = wks.cell(i, 19).value

            #first_name = wks.cell(i, 2).value
            if first_name == "Our Faculty Advisors":
                continue
            #last_name = wks.cell(i, 3).value
            # date_of_birth = wks.cell(i, 4).value
            # email = wks.cell(i, 5).value
            # phone_number = wks.cell(i, 6).value
            # study = wks.cell(i, 7).value
            # level = wks.cell(i, 8).value
            # estimate_year_of_graduation = wks.cell(i, 9).value
            # # if "/" in estimate_year_of_graduation:
            # #     estimate_year_of_graduation = None
            # specialisation = wks.cell(i, 10).value
            # role_at_the_competition = wks.cell(i, 13).value
            #
            # university = wks.cell(i, 14).value
            a=1

            student = Students.objects.update_or_create(
                first_name=first_name,
                last_name=last_name,
                defaults={
                    "university": university,
                    "email": email,
                    "mobile_phone_number": mobile_phone_number,
                    "age": age,
                    "study": study,
                    "level": level,
                    "specialisation": specialisation,
                    "country": country,
                    "position": position,
                    "experience": experience,
                    "role_bonus": role_bonus,
                    "driver": driver,
                    "eso": eso,
                    "role_at_competition": role_at_competition,
                    "category": category,
                    "estimate_year_of_graduation": estimate_year_of_graduation,
                    # "date_of_birth": date_of_birth
                }
            )
            b=1

        a=1

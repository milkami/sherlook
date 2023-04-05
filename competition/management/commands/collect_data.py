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
        wks = sh.worksheet('Studenti')
        j = 0
        for i in range(377, 949):
            print(i)
            print("j"+ str(j))
            if j < 5:
                j= j +1
            else:
                j = 0
                time.sleep(60)
            university = wks.cell(i, 2).value
            #team_name = wks.cell(i, 3).value
            first_name = wks.cell(i, 4).value
            last_name = wks.cell(i, 5).value
            email = wks.cell(i, 7).value
            phone_number = wks.cell(i, 8).value
            nationality = wks.cell(i, 9).value
            position = wks.cell(i, 10).value
            level = wks.cell(i, 11).value
            #estimate_year_of_graduation = int(wks.cell(i, 12).value)
            specialisation = wks.cell(i, 13).value
            rating = randint(1, 100)

            student = Students.objects.update_or_create(
                first_name=first_name,
                last_name=last_name,
                defaults={
                    "university": university,
                    "email": email,
                    "mobile_phone_number": phone_number,
                    "nationality": nationality,
                    "position": position,
                    "level": level,
                    "specialisation": specialisation,
                    "rating": rating,
                    #"estimate_year_of_graduation": estimate_year_of_graduation,
                }
            )

        a=1

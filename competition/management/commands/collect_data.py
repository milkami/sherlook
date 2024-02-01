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
        wks = sh.worksheet('Studenti2')
        j = 0
        for i in range(1, 1300):
            print(i)
            print("j"+ str(j))
            if j < 3:
                j= j +1
            else:
                j = 0
                time.sleep(60)
            first_name = wks.cell(i, 2).value
            if first_name == "Our Faculty Advisors":
                continue
            last_name = wks.cell(i, 3).value
            # date_of_birth = wks.cell(i, 4).value
            email = wks.cell(i, 5).value
            phone_number = wks.cell(i, 6).value
            study = wks.cell(i, 7).value
            level = wks.cell(i, 8).value
            estimate_year_of_graduation = wks.cell(i, 9).value
            specialisation = wks.cell(i, 10).value
            role_at_the_competition = wks.cell(i, 13).value

            university = wks.cell(i, 14).value
            a=1

            student = Students.objects.update_or_create(
                first_name=first_name,
                last_name=last_name,
                defaults={
                    "university": university,
                    "email": email,
                    "mobile_phone_number": phone_number,
                    "study": study,
                    "level": level,
                    "specialisation": specialisation,
                    # "role_in_the_team ": role_in_the_team ,
                    # "role_at_the_competition ": role_at_the_competition,
                    "estimate_year_of_graduation": estimate_year_of_graduation,
                    # "date_of_birth": date_of_birth
                }
            )
            b=1

        a=1

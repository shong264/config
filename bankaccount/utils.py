from django.apps import apps
import random
import string

class Helper:
    @staticmethod
    def generate_account_number(prefix=None):
        model = apps.get_model('bankaccount', 'BankAccount')
        while True:
            unique_number = ''.join(random.choices(string.digits, k=20))
            if prefix:
                account_number = f'{prefix}{unique_number}'
            if not model.objects.filter(account_number=account_number).exists():
                return unique_number
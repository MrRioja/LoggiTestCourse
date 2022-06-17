class UserDoesNotExists(Exception):
    def __init__(self, message):
        self.message = f'Não existe nenhum usuário com o email: {message}.'

class PhoneNumberAlreadyExists(Exception):
    def __init__(self, message):
        self.message = f'O telefone {message} já está vinculado a outro usuário.'

class PhoneNumberAlreadyExists(Exception):
    def __init__(self, message):
        self.message = f'O telefone {message} já está vinculado a outro usuário.'

class CompanyAlreadyExists(Exception):
    def __init__(self, user, company_id):
        self.message = f'O usuário {user} já está vinculado a company id {company_id}.'

class CompanyNotFound(Exception):
    def __init__(self):
        self.message = f'A empresa informada não existe'


def change_user_password(
    email: str,
    new_password: str
) -> bool:
    user = LoggiUser.objects.get(email=email)

    if not user:
        raise UserDoesNotExists(message=email)

    else:
        user.set_password(new_password)
        user.save()


def change_phone_number(
    email: str,
    phone_number: str
):
    user = LoggiUser.objects.get(email=email)

    phone = LoggiUser.objects.get(mobile_1=phone_number)

    if phone:
        raise PhoneNumberAlreadyExists(message=phone_number)
    else:
        user.mobile_1 = phone_number
        user.save()


def link_user_to_company(
    email: str,
    company_id: int
):
    user = LoggiUser.objects.get(email=email)
    company = Company.objects.get(id=company_id)

    if user.company_id:
        raise CompanyAlreadyExists(user.email, user.company_id)
    elif not company:
        raise CompanyNotFound()
    else:
        user.company = company
        user.save()



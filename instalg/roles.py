from rolepermissions.roles import AbstractUserRole

class IngCivil(AbstractUserRole):
    available_permissions = {}

class AdminSistema(AbstractUserRole):
    available_permissions = {}

class AdminMateriales(AbstractUserRole):
    available_permissions = {}

class AdminEmpleados(AbstractUserRole):
    available_permissions = {}

class Proveedor(AbstractUserRole):
    available_permissions = {}

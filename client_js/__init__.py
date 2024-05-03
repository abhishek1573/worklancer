# C:\Users\abhishek sahoo\AppData\Roaming\Python\Python312\site-packages\django\db\models\fields\__init__.py
# def get_prep_value(self, value):
#     value = super().get_prep_value(value)
#     if value is None:
#         return None
#     try:
#         return str(value)  #str is set as int defualt change for this product
#     except (TypeError, ValueError) as e:
#         raise e.__class__(
#             "Field '%s' expected a number but got %r." % (self.name, value),
#         ) from e



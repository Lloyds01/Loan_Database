from django.contrib import admin
from .models import Bvn_check, CustomUser, Liberty_Loan_database
from import_export.admin import ImportExportMixin

# @admin.register(Liberty_Loan_database)

class Liberty_Loan_databaseAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ['Full_Name', 'Borrower_Mobile', 'Borrower_Age',
        'Borrower_Gender',
        'BVN',
        'Loan_Duration',
        'Days_Past_Maturity',
        'Last_Repayment',
        'Principal_Amount',
        'Balance_Amount',
        'Loan_Status_Name'
    ]
admin.site.register(Liberty_Loan_database, Liberty_Loan_databaseAdmin)

admin.site.register(CustomUser)
# admin.site.register(Bvn_check)
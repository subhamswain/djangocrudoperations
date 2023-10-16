from django  import forms
from .models import Employee
class EmployeeForm(forms.ModelForm):
    class Meta:
        model=Employee
        fields=('fullname','emp_code','mobileno','position')
        labels={
            'fullname':'Full Name',
            'emp_code':'EMP CODE'
        }
        
    def __init__(self,*arg,**kwargs):
        super(EmployeeForm,self).__init__(*arg,**kwargs)
        self.fields['position'].empty_label="Select"
        self.fields['emp_code'].required=False
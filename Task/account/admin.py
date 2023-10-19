from django.contrib import admin
from account.models import User,Student,Teacher
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

class UserModelAdmin(BaseUserAdmin):
  # The fields to be used in displaying the User model.
  # These override the definitions on the base UserModelAdmin
  # that reference specific fields on auth.User.
  list_display = ('id', 'email', 'name', 'tc', 'is_admin','is_student','is_teacher')
  list_filter = ('is_admin',)
  fieldsets = (
      ('User Credentials', {'fields': ('email', 'password')}),
      ('Personal info', {'fields': ('name', 'tc')}),
      ('Permissions', {'fields': ('is_admin',)}),
  )
  # add_fieldsets is not a standard ModelAdmin attribute. UserModelAdmin
  # overrides get_fieldsets to use this attribute when creating a user.
  add_fieldsets = (
      (None, {
          'classes': ('wide',),
          'fields': ('email', 'name', 'tc', 'password1', 'password2'),
      }),
  )
  search_fields = ('email',)
  ordering = ('email', 'id')
  filter_horizontal = ()

class TeacherAdmin(admin.ModelAdmin):
    list_display = ('get_email', 'get_name', 'get_tc')

    def get_email(self, obj):
        return obj.user.email

    def get_name(self, obj):
        return obj.user.name

    def get_tc(self, obj):
        return obj.user.tc

    get_email.short_description = 'Email'  # Display name for the column
    get_name.short_description = 'Name'
    get_tc.short_description = 'TC'

class StudentAdmin(admin.ModelAdmin):
    list_display = ('get_email', 'get_name', 'get_tc')

    def get_email(self, obj):
        return obj.user.email

    def get_name(self, obj):
        return obj.user.name

    def get_tc(self, obj):
        return obj.user.tc

    get_email.short_description = 'Email'  # Display name for the column
    get_name.short_description = 'Name'
    get_tc.short_description = 'TC'


# Register the custom admin classes for the Teacher and Student models
admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Student, StudentAdmin)
# Now register the new UserModelAdmin...
admin.site.register(User, UserModelAdmin)
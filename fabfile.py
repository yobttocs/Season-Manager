from fabric.api import local

def prepare_push(branch_name):
    local('python manage.py test seasonplanner')
    local('git add -p && git commit')
    local('git push origin')
    

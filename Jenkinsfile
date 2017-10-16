pipeline {
    agent { docker 'python:3.6.3' }
    stages {
        stage('build') {
            steps {
                sh 'python --version'
                pip install -r requirements.txt
                python manage.py migrate
                python manage.py loaddata blahapp
            }
        }
    }
}

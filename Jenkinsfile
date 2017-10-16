pipeline {
    agent { docker 'python:3.6.3' }
    stages {
        stage('build') {
            steps {
                sh 'python --version'
                sh 'pip install -r requirements.txt'
                sh 'python manage.py migrate'
                sh 'python manage.py loaddata blahapp'
            }
        }
    }
}

pipeline {
    agent { docker 'python:2.7.10' }
    stages {
        stage('build') {
            steps {
				sh 'python --version'
				sh 'pwd'
				sh 'ls -Al'
				sh 'ls -Al ..'
				sh 'pip install -r requirements.txt'
				sh 'python manage.py migrate'
				sh 'python manage.py loaddata blahapp'
            }
        }
    }
}

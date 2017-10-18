pipeline {
    agent { 
		docker {
			image 'python:2.7.10'
			args '-u root --expose 8000 -p 33000:8000' 
		}
	}
    stages {
        stage('build') {
            steps {
				sh 'python --version'
				sh 'pwd'
				sh 'pip install -r requirements.txt'
				sh 'python manage.py migrate'
				sh 'python manage.py loaddata blahapp'
            }
        }
    }
}

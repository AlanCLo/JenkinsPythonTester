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
				sh 'sh JenkinsBuild.sh'
				sh 'coverage run manage.py test blahapp -v 2'
				sh 'coverage html'
				archive 'htmlcov/*'
            }
        }
    }
}

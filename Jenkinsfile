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
            }
        }
    }
}

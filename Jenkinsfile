pipeline {
	agent none
    stages {
        stage('build') {
			agent { 
				docker {
					image 'python:2.7.10'
					args '-u root --expose 8000 -p 33000:8000' 
				}
			}
            steps {
				sh 'sh JenkinsBuild.sh'
				sh 'coverage run manage.py test blahapp -v 2'
				sh 'coverage html'
				archive 'htmlcov/*'
            }
        }
		stage('build-container') {
			agent { 
				dockerfile {
					additionalBuildArgs '-t alan/blahapp'
				}
			}
			steps {
				sh 'coverage run manage.py test blahapp -v 2'
			}
		}
		stage('deploy') {
			when {
				expression { currentBuild.result == null || currentBUild.result == 'SUCCESS' }
			}
			agent {
				image 'alan/blahapp'
			}
			steps {
				sh 'ps aux | grep python'
			}
		}
    }
}

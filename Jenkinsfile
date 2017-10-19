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
				sh 'ip -4 route get 8.8.8.8 | awk {'print $7'} | tr -d "\n"'
			}
		}
		stage('deploy') {
			when {
				expression { currentBuild.result == null || currentBUild.result == 'SUCCESS' }
			}
			agent any
			steps {
				sh 'docker stop blahappdeployed || true && docker rm blahappdeployed || true'
				sh 'docker run -d -it -p 33000:8000 -e ALLOWED_HOST `ip -4 route get 8.8.8.8 | awk {'print $7'} | tr -d "\n"` --name=blahappdeployed alan/blahapp'
			}
		}
    }
}
